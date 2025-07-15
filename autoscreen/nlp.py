import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

# Load the tokenizer and model with error handling
try:
    model_name = "unitary/unbiased-toxic-roberta"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Create a pipeline for text classification
    nlp = pipeline("text-classification", model=model, tokenizer=tokenizer)
    print("Model and tokenizer loaded successfully.")
except Exception as e:
    print(f"Error loading model or tokenizer: {e}")
    nlp = None

def NLP(messages):
    if nlp is None:
        print("NLP pipeline is not available.")
        return 0

    try:
        for text in messages:
            result = nlp(text)

            # Debugging: Print the result for each message
            print(f"Text: {text} | Classification Result: {result}")

            if result[0]["score"] > 0.8:
                print("Toxic content detected.")
                return 1
        return 0
    except Exception as e:
        print(f"Error processing text: {e}")
        return 0

# Example usage
# messages = ["Your example text here", "Another text to classify"]
# toxic_flag = NLP(messages)
# print(f"Toxic flag: {toxic_flag}")
