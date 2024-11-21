import pandas as pd

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully with {len(df)} rows!")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Example Usage
dataset_path = "/Users/shriyamohite/git/translation_chatbot/LLM_dataset.csv"
dataset = load_dataset(dataset_path)
