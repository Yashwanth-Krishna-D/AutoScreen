# Autoscreen

## Revolutionizing Digital Investigations with AI

**Autoscreen** is an AI-powered web application built to assist investigative agencies like the **National Investigation Agency (NIA)** by streamlining social media parsing and digital forensics. This tool integrates **AI**, **automation**, and **cross-platform compatibility** to improve the accuracy and speed of digital investigations.

---

## Key Features

- Automated Web Scraping using Selenium
- AI-Powered Text Classification (RoBERTa NLP)
- Image Captioning (BLIP model)
- PDF Report Generation
- Content Summarization
- Cross-Platform Support (Windows, Android)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/autoscreen.git
   cd autoscreen
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Install as a package:
   ```bash
   pip install .
   ```

---

## Usage

- To run the main Instagram scraping tool:
  ```bash
  python -m autoscreen.instagram_main
  ```
  Or, if installed as a package:
  ```bash
  autoscreen-instagram
  ```
- For the GUI, run:
  ```bash
  python -m autoscreen.front
  ```

---

## Project Structure

- `autoscreen/` - All source code modules
- `instagram_screenshots/` - Saved screenshots and images
- `requirements.txt` - Python dependencies
- `setup.py` - Packaging script

---

## Acknowledgements

This project was a huge learning experience, blending **machine learning**, **web scraping**, and **UX/UI design** to solve real-world problems in cyber forensics.

Special thanks to my incredible teammates:  
**Gokul Nishandh S T**, **Kirthic Adhithya J**, **Katherine Olivia**, **Prashanth Samkumar** and **Anushna**




