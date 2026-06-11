# AI Language Translator

A modern AI-powered Language Translator built using LangChain, Groq, and Streamlit. This application enables users to translate text into any language with fast and accurate responses powered by Large Language Models (LLMs).

---

## Overview

This project provides a clean and intuitive interface for translating text into any target language. It leverages LangChain for prompt orchestration, Groq for high-speed LLM inference, and Streamlit for the user interface.

---

## Features

* Translate text into any language
* Powered by Groq LLMs for fast inference
* Modern and responsive Streamlit UI
* Character and word count analytics
* Translation history tracking
* Download translated output
* Supports long-form text translation
* User-friendly interface

---

## Tech Stack

* Python
* Streamlit
* LangChain
* Groq API
* Prompt Engineering
* HTML
* CSS

---

## Project Structure

```bash
AI-Language-Translator/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
└── assets/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Language-Translator.git

cd AI-Language-Translator
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## How It Works

1. Enter or paste text into the input area.
2. Specify the target language.
3. LangChain constructs the translation prompt.
4. Groq processes the request using a Large Language Model.
5. The translated text is displayed instantly.
6. Translation history is maintained during the session.

---

## Screenshots

### Home Page

Add a screenshot of the application home page here.

### Translation Output

Add a screenshot of the translated output page here.

---

## Use Cases

* Language Learning
* Document Translation
* Content Localization
* Academic Translation
* Business Communication
* Travel Assistance

---

## Learning Outcomes

This project demonstrates:

* LangChain Fundamentals
* Prompt Engineering
* Groq Integration
* Streamlit Application Development
* Session State Management
* AI-Powered Application Development

---

## Future Enhancements

* Automatic Language Detection
* Voice-to-Text Translation
* Text-to-Speech Output
* PDF Translation
* Multi-Document Translation
* REST API Deployment
* Translation Quality Evaluation

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---


## Author

Kousalya

If you found this project useful, consider giving it a star on GitHub.
