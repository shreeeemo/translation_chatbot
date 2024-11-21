from transformers import pipeline

def translate_text(text, source_lang="en", target_lang="fr"):
    try:
        model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
        translator = pipeline("translation", model=model_name)
        translation = translator(text, max_length=512)
        return translation[0]["translation_text"]
    except Exception as e:
        print(f"Error loading model for {source_lang} to {target_lang}: {e}")
        return "Translation not available for this language pair."


def post_process_translation(translation):
    # Example: Adjust common issues in French translations
    if "fr" in translation:
        translation = translation.replace("Mr.", "Monsieur").replace("Mrs.", "Madame")
    return translation.capitalize()
