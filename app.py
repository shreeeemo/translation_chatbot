from flask import Flask, request, jsonify, render_template
from translation_pipeline import translate_text, post_process_translation
from dataset_utils import load_dataset

app = Flask(__name__)

# Load dataset globally at the start
DATASET_PATH = "/Users/shriyamohite/git/translation_chatbot/LLM_dataset.csv"
dataset = load_dataset(DATASET_PATH)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    try:
        print("Received a request to /translate")
        data = request.json
        if not data:
            raise ValueError("No JSON data provided")

        source_text = data.get("text", "")
        source_lang = data.get("source_lang", "en")
        target_lang = data.get("target_lang", "fr")

        if not source_text:
            raise ValueError("No text provided for translation")

        raw_translation = translate_text(source_text, source_lang, target_lang)
        polished_translation = post_process_translation(raw_translation)

        print("Translation result:", polished_translation)
        return jsonify({"translation": polished_translation})

    except Exception as e:
        print("Error in /translate route:", e)
        return jsonify({"error": str(e)}), 500


@app.route("/test_translation/<int:row_id>", methods=["GET"])
def test_translation(row_id):
    # Ensure the dataset is loaded
    if dataset is None:
        return jsonify({"error": "Dataset not loaded"}), 500

    # Validate row_id
    if row_id >= len(dataset):
        return jsonify({"error": "Row ID out of bounds"}), 404

    # Get specific row from the dataset
    row = dataset.iloc[row_id]
    source_text = row['text']
    source_lang = row['language']
    target_lang = "en"  # Translating to English

    # Perform translation
    raw_translation = translate_text(source_text, source_lang, target_lang)
    polished_translation = post_process_translation(raw_translation)

    return jsonify({
        "original": source_text,
        "language": source_lang,
        "chatbot_translation": polished_translation,
        "dataset_response": row['response']
    })

if __name__ == "__main__":
    app.run(debug=True)
