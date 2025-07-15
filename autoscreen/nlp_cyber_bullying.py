from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

# Load the tokenizer and model
model_name = "unitary/unbiased-toxic-roberta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create a pipeline for text classification
nlp = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Run the classification
for text in texts:
    result = nlp(text)
    print(f"Text: {text}\nClassification: {result}\n")