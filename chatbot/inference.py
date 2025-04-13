from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
model_path = r"C:\Monkify_Bert\bert-intent-chatbot\checkpoint-2850"  
tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
# Create inference pipeline
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

def get_chatbot_response(query: str):
    result = classifier(query)
    return result[0]  # label + score
