# CloudOps AI Monitor 🚀

An end-to-end **AI-powered monitoring system** for CloudOps environments.  
This project trains an **anomaly detection model** on system logs, serves predictions via a **FastAPI REST API**, deploys with **Docker**, trains on **AWS SageMaker**, and uses **OpenAI GPT models** for **Generative AI explanations**.  

It’s designed to showcase **AI + CloudOps + MLOps skills** (aligned with roles involving ML for monitoring, incident detection, and automation).

---

## 📂 Project Structure

```
cloudops-ai-monitor/
│
├── data/
│   ├── logs.csv                # Sample synthetic dataset
│   ├── preprocessed_logs.csv   # Generated features
│   └── preprocess.py           # Preprocessing script
│
├── models/
│   └── cloud_monitor_model.py  # PyTorch model
│
├── train/
│   ├── train.py                # Training loop
│   └── sagemaker_train.py      # AWS SageMaker launcher
│
├── api/
│   ├── schema.py               # Pydantic schema
│   ├── inference.py            # Inference logic
│   └── main.py                 # FastAPI server
│
├── genai/
│   └── explain.py              # Generative AI interpretation
│
├── streamlit_app.py            # UI demo
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 📊 Dataset

The included **`data/logs.csv`** simulates log events:  

| timestamp           | level  | message                    | anomaly |
|---------------------|--------|----------------------------|---------|
| 2025-01-01 00:00:00 | INFO   | Service started            | 0 |
| 2025-01-01 01:00:00 | ERROR  | Disk error detected        | 1 |
| 2025-01-01 02:00:00 | WARN   | High memory usage          | 1 |
| …                   | …      | …                          | … |

Run preprocessing:

```bash
python data/preprocess.py
```

This generates **`data/preprocessed_logs.csv`** with engineered features:  
- `error_count`  
- `log_level_score`  
- `event_density`  
- `anomaly`  

---

## 🧠 Training (Local)

⚠️ To avoid Python import issues, always run training from the **project root** with `-m`:

```bash
python -m train.train
```

If you prefer direct execution:

```bash
python train/train.py
```

(but ensure `__init__.py` files exist in `train/`, `api/`, `models/`).

This trains a PyTorch model (`model.pth`) on the preprocessed dataset.  

---

## ☁️ Training (AWS SageMaker)

Upload dataset to S3 and run:

```bash
python train/sagemaker_train.py
```

This uses the `ml.m5.large` instance with the PyTorch container.  

---

## 🚀 FastAPI Inference

Run the API locally:

```bash
uvicorn api.main:app --reload
# OR (recommended to avoid import issues)
python -m uvicorn api.main:app --reload
```

Send a request:

```bash
curl -X POST "http://127.0.0.1:8000/predict"   -H "Content-Type: application/json"   -d '{"error_count":1,"log_level_score":2,"event_density":50}'
```

Response:

```json
{
  "prediction": 1,
  "confidence": 0.87
}
```

Interactive Swagger UI is available at 👉 http://127.0.0.1:8000/docs  

---

## 🧠 Generative AI Explanation

This project uses **OpenAI GPT models** for explanations.

### Setup your API key:

```bash
export OPENAI_API_KEY="sk-your_api_key_here"
```

By default, the project uses **gpt-3.5-turbo** (cheaper, often available).  
You can override with another model (like `gpt-4o-mini`):

```bash
export GENAI_MODEL="gpt-4o-mini"
```

### Example run

```bash
python3 -m genai.explain
```

Example output:

> "The system predicted an anomaly (87% confidence). Likely causes: disk errors or high CPU. Recommended actions: scale affected nodes, restart service, monitor logs."

### FastAPI explained endpoint

You can also call the combined endpoint:

```bash
curl -X POST "http://127.0.0.1:8000/predict_explained"   -H "Content-Type: application/json"   -d '{"error_count":1,"log_level_score":2,"event_density":50}'
```

Response (even if quota is exceeded):

```json
{
  "prediction": 1,
  "confidence": 0.87,
  "explanation": "[GenAI Explanation Unavailable] ..."
}
```

This ensures your demo never crashes.  

---

## 🐳 Docker Deployment

Build and run:

```bash
docker-compose up --build
```

API available at `http://localhost:8080/predict`.

---

## 🎨 Streamlit UI

Launch a simple UI:

```bash
streamlit run streamlit_app.py
```

Interactive sliders let you simulate metrics → prediction → explanation.

---

## ✅ Use Cases Covered

- Failure detection  
- Incident management  
- System health monitoring  
- Anomaly detection  
- CloudOps automation + AI  
