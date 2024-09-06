# chatbot.py

import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import pandas as pd

# Import data processing functions from data_processor.py
from data_processor import load_csv, summarize_data, display_column

# Load the model and tokenizer from Hugging Face using your model config
from config.model_config import MODEL_NAME, MAX_LENGTH

# Hugging Face API token (ensure this is set in the environment)
token = os.getenv("HUGGINGFACE_HUB_TOKEN")

# Load the tokenizer and the model with the token
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_auth_token=token)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, use_auth_token=token)

# Function for generating chatbot responses
def chat_with_llama(user_message):
    inputs = tokenizer(user_message, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=MAX_LENGTH)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Main chatbot loop
if __name__ == "__main__":
    print("Llama AI Chatbot is ready! Type your messages below or type 'upload csv' to analyze a CSV file.")
    while True:
        user_message = input("You: ")

        if user_message.lower() == "upload csv":
            file_path = input("Enter the path to your CSV file: ")
            data = load_csv(file_path)

            if isinstance(data, pd.DataFrame):
                print("What would you like to do with the data?")
                print("1. View summary statistics")
                print("2. View a specific column")

                choice = input("Enter 1 or 2: ")

                if choice == "1":
                    result = summarize_data(data)
                    print(f"Data Summary:\n{result}")
                elif choice == "2":
                    column_name = input("Enter the column name: ")
                    result = display_column(data, column_name)
                    print(f"Column Data:\n{result}")
                else:
                    print("Invalid choice!")
            else:
                print(f"Error: {data}")

        elif user_message.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        else:
            response = chat_with_llama(user_message)
            print(f"Chatbot: {response}")
