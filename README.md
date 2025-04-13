# 🤖 BERT-Based Intent Chatbot with Django API

This project is a simple yet powerful chatbot built using a fine-tuned BERT model for intent classification. It is deployed on Hugging Face for public access and integrated into a Django REST API server for real-time interaction.

---

## 📌 Features

- 🔍 **Intent Recognition** using a fine-tuned BERT model
- 🧠 **Context-aware** and **custom-trained** responses
- 📁 **File-aware queries** and extendable file analysis support
- ☁️ **Model deployed on Hugging Face**
- 🔗 **Django REST API** for seamless frontend/backend integration

---

## 🛠️ Tech Stack

- Python 3.9+
- [Transformers (Hugging Face)](https://huggingface.co/docs/transformers/index)
- PyTorch
- Django
- Django REST Framework
- Hugging Face Hub

---

## 🚀 Hugging Face Model

The chatbot model is publicly available on Hugging Face:

🔗 **[DocExtract/bert-intent-chatbot](https://huggingface.co/DocExtract/bert-intent-chatbot)**

> Fine-tuned on a small intent classification dataset to handle user queries like booking flights, checking weather, playing music, and more.

---

## 📂 Project Structure

```bash
bert_chatbot_project/
├── chatbot/                  # App for chatbot logic
│   ├── inference.py         # Loads and runs the BERT model
│   ├── views.py             # Django API endpoint logic
│   └── ...
├── bert_chatbot_project/    # Django project settings
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Setup Instructions
1. Clone the Repository

git clone https://github.com/Sriram-Kanungo/bert-chatbot-django.git
cd bert-chatbot-django
2. Set Up Virtual Environment

python -m venv bert_finetune
source bert_finetune/bin/activate        # On Linux/Mac
bert_finetune\Scripts\activate.bat       # On Windows
3. Install Dependencies

pip install -r requirements.txt
4. Run Django Server

python manage.py runserver
💬 API Usage
Endpoint

POST /api/chat/
Request Body (JSON)

{
  "query": "how can I book a flight?"
}
Sample Response

[
  {
    "label": "BookFlight",
    "score": 0.9821
  }
]
