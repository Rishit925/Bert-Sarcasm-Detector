# 😏 Sarcasm Detection using BERT

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red?logo=pytorch)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-FF4B4B?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)

---

## 📌 Project Overview

This project is an end-to-end NLP application that detects whether a news headline is **Sarcastic** or **Not Sarcastic** using a fine-tuned **BERT (bert-base-uncased)** model. The project includes an interactive Streamlit web interface, a FastAPI REST API with Swagger documentation, and Docker support for containerized execution.

The application provides:

- 🖥️ Interactive Streamlit Web Application
- 🚀 FastAPI REST API
- 📖 Swagger API Documentation
- 🐳 Docker & Docker Compose Support
- 📊 Prediction Confidence Levels
- 🤖 Deep Learning based inference using BERT

---

# 🔗 Project Links

- **GitHub Repository:** https://github.com/Rishit925/Bert-Sarcasm-Detector
- **Hugging Face Model:** https://huggingface.co/Rishit925/Bert-Sarcasm-Detector
- **Live Demo:** Not deployed (Model size exceeds free cloud hosting limits)

# 🏗 Project Architecture

```mermaid
flowchart LR

A[User] --> B[Streamlit Web App]
B --> C[BERT Prediction Model]
C --> D[Prediction Result]

C --> E[FastAPI]
E --> F[Swagger Documentation]

B --> G[Docker]
E --> G
```

---

# ✨ Features

- Fine-tuned BERT model for sarcasm detection
- Streamlit based user interface
- FastAPI REST API
- Automatic Swagger Documentation
- Dockerized application
- Docker Compose support
- Confidence level visualization
- Clean project structure

---

# 🖼 Screenshots

## Home Page

![Home](assets/home.png)

---

## Prediction

![Prediction](assets/prediction.png)

---

## FastAPI Swagger

![Swagger 1](assets/swagger-ui-1.png)

![Swagger 2](assets/swagger-ui-2.png)

---

# 🛠 Tech Stack

### Programming Language

- Python

### Deep Learning

- PyTorch
- Hugging Face Transformers

### API

- FastAPI
- Pydantic

### Frontend

- Streamlit

### Deployment

- Docker
- Docker Compose

---

# 📂 Project Structure

```text
Sarcasm-Detection/

│── app.py
│── api.py
│── model.py
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── README.md
│── .gitignore
│── bert_sarcasm_classifier.pth

│── tokenizer/

│── assets/

│     ├── home.png
│     ├── prediction.png
│     ├── swagger-ui-1.png
│     └── swagger-ui-2.png

│── notebooks/
│     └── text_classification.ipynb
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Rishit925/Bert-Sarcasm-Detector.git
```

Move inside the folder

```bash
cd Bert-Sarcasm-Detector
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

> **Note**
>
> The trained BERT model (~439 MB) is hosted separately on Hugging Face because GitHub repositories have a 100 MB file size limit.

---

# 🚀 Running the Streamlit App

```bash
streamlit run app.py
```

Application:

```
http://localhost:8501
```

---

# 🔌 Running the FastAPI Server

```bash
uvicorn api:app --reload
```

Swagger UI

```
http://localhost:8000/docs
```

---

# 🐳 Docker

Build

```bash
docker build -t sarcasm-detector .
```

Run

```bash
docker run -p 8501:8501 sarcasm-detector
```

---

# 🐳 Docker Compose

Start

```bash
docker compose up --build
```

Stop

```bash
docker compose down
```

---

# 📌 Deployment Status

The application has been successfully tested locally using:

- ✅ Streamlit
- ✅ FastAPI
- ✅ Docker
- ✅ Docker Compose

The trained model is hosted separately on Hugging Face due to its size (~439 MB). Therefore, a public cloud deployment is not included in this repository.

# 📡 API Endpoint

### POST

```
/predict
```

Request

```json
{
  "text":"Scientists Discover Water On Mars"
}
```

Response

```json
{
  "headline":"Scientists Discover Water On Mars",
  "prediction":"Not Sarcastic",
  "confidence":92.21
}
```

---

# 🧠 Model Details

| Parameter | Value |
|-----------|-------|
| Model | BERT Base Uncased |
| Framework | PyTorch |
| Tokenizer | BertTokenizer |
| Task | Binary Text Classification |
| Output | Sarcastic / Not Sarcastic |

---

# 📈 Future Improvements

- Improve model accuracy through hyperparameter tuning.
- Train on a larger and more diverse sarcasm dataset.
- Experiment with RoBERTa, DistilBERT, and DeBERTa.
- Add batch prediction support.
- Deploy using cloud infrastructure with persistent model storage.
- Improve inference speed through model optimization.

---

# 👨‍💻 Author

**Rishit Mahindru**

---

# ⭐ If you found this project useful

Please consider giving the repository a ⭐ on GitHub.
