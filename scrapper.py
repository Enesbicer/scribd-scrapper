import os
import time
import requests
import img2pdf
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def download_scribd_pdf(url, output_pdf_name="document.pdf"):

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print(f"Navigating to: {url}")
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)  

        print("Scrolling down (Waiting for images to load)...")
        
        last_height = driver.execute_script("return document.body.scrollHeight")
        
        while True:
            driver.execute_script("window.scrollTo(0, window.scrollY + 500);")
            time.sleep(0.5) 
            
            new_height = driver.execute_script("return window.scrollY + window.innerHeight")
            if new_height >= driver.execute_script("return document.body.scrollHeight"):
                time.sleep(2)
                break

        print("Scrolling complete. Collecting image links...")

        images = driver.find_elements(By.CSS_SELECTOR, "img.absimg")
        
        img_urls = []
        for img in images:
            src = img.get_attribute('src')
            if src:
                img_urls.append(src)

        seen = set()
        unique_urls = [x for x in img_urls if not (x in seen or seen.add(x))]
        
        print(f"Total {len(unique_urls)} pages found.")

        if not os.path.exists("temp_images"):
            os.makedirs("temp_images")

        downloaded_files = []
        
        for i, img_url in enumerate(unique_urls):
            try:
                print(f"Downloading: Page {i+1}/{len(unique_urls)}")
                response = requests.get(img_url, stream=True)
                if response.status_code == 200:
                    filename = f"temp_images/page_{i+1:03d}.jpg"
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                    downloaded_files.append(filename)
                else:
                    print(f"Error: Page {i+1} could not be downloaded. Status: {response.status_code}")
            except Exception as e:
                print(f"Error: {e}")

        if downloaded_files:
            print("Creating PDF...")
            with open(output_pdf_name, "wb") as f:
                f.write(img2pdf.convert(downloaded_files))
            print(f"Success! File saved: {output_pdf_name}")
        else:
            print("No images downloaded.")

        # Clean up temporary files (Uncomment if you want to delete temp files)
        # for f in downloaded_files:
        #    os.remove(f)
        # os.rmdir("temp_images")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

# USAGE
target_link = "target_scribd_document_link_here"
download_scribd_pdf(target_link, "output_document.pdf")
