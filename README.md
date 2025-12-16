# 📄 Scribd to PDF Downloader

A lightweight Python tool to download Scribd documents as images and merge them into a single PDF using Selenium. 
Scribd: https://www.scribd.com

## 🚀 Features
* **Auto-Scroll:** Automatically scrolls to load all pages.
* **High Quality:** Captures full-resolution document images.
* **PDF Conversion:** Merges images into a PDF using `img2pdf`.
* **Easy Setup:** Automatically manages Chrome driver installation.

## 🛠️ Installation
Requires **Google Chrome**. Install dependencies:

```bash
pip install requests img2pdf selenium webdriver-manager
```

## 💻 Usage

<img width="488" height="69" alt="image" src="https://github.com/user-attachments/assets/9723afb2-8e7f-4f3f-be02-039775055665" />


1.  Open `scrapper.py` and update the `target_link` variable with your Scribd URL.
2.  Run the script:

```bash
python scrapper.py
```

*Note: Do not close the Chrome window while the script is running.*

## ⚠️ Disclaimer
For **educational purposes only**. Please respect copyright laws and Scribd's Terms of Service.
