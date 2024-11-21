# translation_chatbot

A simple AI-powered chatbot built using Flask and Hugging Face's `transformers` library for real-time language translation. This project demonstrates the integration of machine learning models with a web-based interface.

## Features
- Translate text between multiple languages.
- Simple and interactive user interface (HTML and JavaScript).
- Uses `Helsinki-NLP` models for accurate translations.
- Extensible: Add more languages or improve UI/UX.

## Technologies Used
- **Python**: For backend server and translation logic.
- **Flask**: Lightweight framework for building the web application.
- **Hugging Face Transformers**: For machine learning-based translations.
- **HTML/CSS/JavaScript**: For the front-end user interface.
- **Git**: For version control.

## Requirements
To run this project locally, ensure you have the following installed:
- Python 3.7 or later
- `pip` (Python package installer)
- A web browser

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/shreeeemo/translation_chatbot.git

Navigate to the project directory:
cd translation_chatbot

Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

Install the required Python libraries:
pip install -r requirements.txt

Start the Flask server:
python app.py

Open your browser and navigate to:
http://127.0.0.1:5000

The chatbot currently supports the following languages:

English (en)
French (fr)
Spanish (es)
German (de)
Italian (it)
Chinese (zh)
Arabic (ar)

Feel free to add more languages by modifying the source_lang and target_lang dropdowns in index.html.

## Folder Structure
translation_chatbot/
├── app.py                 # Main Flask app
├── translation_pipeline.py # Translation logic
├── dataset_utils.py       # Dataset utilities
├── templates/
│   └── index.html         # Frontend HTML
├── venv/                  # Virtual environment
├── requirements.txt       # Python dependencies
├── README.md              # Documentation
└── LLM_dataset.csv        # Dataset file (if applicable)

## Contributing
Contributions are welcome, feel free to open an issue or submit a pull request to improve the project.
