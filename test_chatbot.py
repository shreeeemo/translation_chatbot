from translation_pipeline import translate_text, post_process_translation
from dataset_utils import load_dataset

# Load the dataset
dataset = load_dataset("LLM__dataset.csv")

# Test translations
if dataset is not None:
    for index, row in dataset.iterrows():
        source_text = row['text']
        source_lang = row['language']
        target_lang = "en"  # Translating to English
        
        chatbot_translation = post_process_translation(
            translate_text(source_text, source_lang, target_lang)
        )
        
        print(f"Row {index}")
        print(f"Original: {source_text}")
        print(f"Language: {source_lang}")
        print(f"Chatbot Translation: {chatbot_translation}")
        print(f"Dataset Response: {row['response']}")
        print("=" * 50)
