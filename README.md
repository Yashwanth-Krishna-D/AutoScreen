<<<<<<< HEAD
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




=======
# 🚨 Autoscreen  
_Revolutionizing Digital Investigations with AI_

**Autoscreen** is an AI-powered web application designed to assist investigative agencies like the National Investigation Agency (NIA) by streamlining social media parsing and digital forensics. It leverages automation, AI models, and cross-platform capabilities to enhance the efficiency and precision of digital investigations.

---

## 🔑 Key Features

- **🕸 Automated Web Scraping**  
  Extracts posts, messages, timelines, and friend lists from social media platforms using Selenium and WebDriver.

- **🧠 AI-Powered Text Classification**  
  Utilizes the RoBERTa NLP model to detect, filter, and classify sensitive or critical content based on predefined criteria.

- **🖼 Image Captioning**  
  Integrates the BLIP model to generate descriptive captions for images, aiding in visual evidence analysis.

- **📄 PDF Report Generation**  
  Automatically compiles findings, including screenshots and captions, into well-structured PDF reports.

- **📝 AI-Based Content Summarization**  
  Extracts concise insights from large textual datasets to support quick comprehension.

- **📱🖥 Cross-Platform Support**  
  Supports Windows (via CustomTkinter) and Android (via native app, in development) for versatile field use.

---

## ⚙️ How It Helps

- Reduces manual workload in digital investigations  
- Speeds up evidence collection through automation  
- Enhances accuracy with AI-driven classification  
- Efficiently processes large datasets via batch handling  
- Generates legally presentable reports in PDF format  

---

## 🧰 Tech Stack

| Component              | Technology/Tool               |
|------------------------|-------------------------------|
| **Frontend (Windows)** | CustomTkinter (Python GUI)    |
| **Frontend (Android)** | Native Android (Planned)      |
| **Backend**            | Python                        |
| **Web Scraping**       | Selenium, WebDriver           |
| **NLP**                | RoBERTa (Text Classification) |
| **Image Captioning**   | BLIP                          |
| **Reporting**          | FPDF, PIL, other PDF libs     |
| **Summarization**      | Transformers, NLP Models      |

---

## 🚀 How to Use

> **Note:** Currently, only the **Instagram** module is operational. Other modules are under development.

1. Clone the repository or download the ZIP  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt

3. Run the application:

   ```bash
   python front.py
   ```
4. Follow the on-screen instructions via the GUI

---

## 🙌 Acknowledgements

This project was a rewarding learning experience — combining machine learning, web scraping, and UI/UX development to solve critical problems in cyber forensics.

**Special thanks to my amazing teammates:**

* Gokul Nishandh S T
* Kirthic Adhithya J
* Katherine Olivia
* Prashanth Samkumar
* Anushna

---

>>>>>>> 78fc6fcae974923c61ed006a1f2f6c7db8cf17d5
