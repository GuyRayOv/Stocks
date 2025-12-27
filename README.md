# 📈 Stock Prediction & Investment Strategy System

## 🔍 Project Overview

This project is an **end-to-end AI system for stock market analysis**, combining **time-series forecasting**, **computer vision**, and **LLM** to predict future prices and generate actionable investment recommendations.

The system follows a **hybrid, multi-modal approach**:

1. **Machine Learning for Feature Selection** – XGBoost identifies the most informative features from a rich time-series dataset  
2. **Deep Learning for Time Series Forecasting** – LSTM, GRU, CNN, and hybrid architectures predict future prices  
3. **Computer Vision for Strategy Classification** – A `fastai` CNN classifies price-chart images into BUY / KEEP / SELL  
4. **LLM-Driven Interface** – A Gemini agent interprets natural-language user queries and triggers the prediction pipeline  

---

## 🚀 Key Capabilities

### 1️⃣ Robust Data Pipeline

The system aggregates **historical stock prices** together with **macroeconomic indicators** to capture broader market dynamics.

**Inputs include:**
- **Target assets:** Individual stock tickers  
- **Macroeconomic indicators:**
  - Oil (WTI)
  - Gold
  - S&P 500
  - NASDAQ
  - Real Estate indices
  - Inflation expectations  

### 2️⃣ Advanced Feature Engineering & Selection

- **Feature generation:**  
  Approximately **300 time-series features** per asset, including:
  - Lagged values  
  - Rolling min / max / mean / std / diff, pct_change

- **Feature selection:**  
  An **XGBoost (XGB)** model ranks feature importance and selects the **top 20 most impactful features**, significantly reducing dimensionality while preserving predictive performance.

### 3️⃣ Dual-Model Architecture

#### 🧠 A. Time-Series Regression (Price Forecasting)

- **Models:** LSTM, GRU, CNN, and hybrid / ensemble combinations  
- **Objective:** Predict future stock prices over a configurable horizon  
- **Performance:** best-performing models achieved **~97% predictive performance** (R² / accuracy depending on configuration)


#### 👁️ B. Visual Strategy Classification (Investment Recommendation)

- **Framework:** `fastai` (CNN-based computer vision)  
- **Methodology:**
  1. Convert historical price data into **rolling 1-year chart images**
  2. Label each image according to **future price behavior**
  3. Train a classifier to output:
     - **BUY**
     - **KEEP**
     - **SELL**

- **Performance:** best vision model achieved **~73% accuracy**

This model provides an intuitive, human-interpretable investment signal.


### 4️⃣ LLM-Powered Natural Language Interface

- **LLM:** Google Gemini  
- **Functionality:**
  - Parses natural-language user prompts  
  - Extracts:
    - Target ticker (TKL)
    - Prediction horizon (days)
  - Automatically triggers the inference pipeline  

**Example prompt:**
> *“What is the outlook for NVDA over the next 7 days?”*

---

## 📂 Repository Structure
```

{REPOSITORY_PATH}/
│
├── data/                                  # Time-series datasets (per stock)
│ ├── <stock1>.df.csv
│ └── <stockN>.df.csv
│
├── notebooks/
│ ├── dataprep_for_train.ipynb             # Feature engineering & selection
│ ├── imagesprep_for_train.ipynb           # Chart image generation
│ ├── train_models.ipynb                   # Model selection & training
│ ├── train.ipynb                          # End-to-end training pipeline
│ ├── llm_api.ipynb                        # Gemini-based prompt parsing
│ ├── predict.ipynb                        # Full inference pipeline
│ ├── dataprep_for_inference.ipynb         # Refresh data with latest prices
│ ├── predict_future.ipynb                 # Time-series forecasting
│ └── recommend_investment_strategy.ipynb  # Vision-based recommendation
│
├── src/
│ ├── config.json                          # Global configuration
│ ├── my_project_utils.py                  # Shared helper functions
│ └── init.py
│
├── images/                                # Generated chart images
├── output/                                # Logs and results
│
├── pickles/                               # Serialized models & datasets
│ ├── <stock>.best_model.X_features.keras
│ └── <stock>.df.pkl
│
├── README.md
└── .gitignore
```
---

### `train.ipynb` (Model Training)

<img width="1318" height="969" alt="image" src="https://github.com/user-attachments/assets/ad427a24-3962-4256-a112-f8b78922ade2" />

---

### `predict.ipynb` (Inference & Application)

<img width="1404" height="1055" alt="image" src="https://github.com/user-attachments/assets/cfaa52a4-47a9-4653-9b3b-6b55b8781e6d" />

---

## 📊 Results Summary

| Model Type        | Architecture        | Task                     | Performance      |
|------------------|---------------------|--------------------------|-------------------|
| Time Series      | LSTM / GRU / CNN    | Price Prediction         | ~97%              |
| Computer Vision  | fastai CNN          | Buy / Keep / Sell        | ~73% accuracy     |

---

## ▶️ How to Run

1. **Clone** the repository
2. Create a `.env` file in the runtime root (e.g. `/content/.env`)
3. In `.env` define the project path: e.g. `PROJECT_PATH=/content/drive/MyDrive/Projects/GitHub/Stocks/`
4. Add your Gemini API key: i.e `GEMINI_API_KEY=apikey`
5. Configure training parameters in `src/config.json`
6. Choose one:
- **Train models:** run `notebooks/train.ipynb`
- **Run inference via LLM:** run `notebooks/llm_api.ipynb`
7. Click **Run All**

---

## 📦 Project Deliverables

- `data/*.csv` – Time-series datasets with selected XGB features  
- `pickles/*.pkl` – Serialized inference-ready datasets  
- `pickles/*.keras` – Best trained models per stock  
- `images/*.png` – Chart images for vision-based strategy classification  

---

## 📦 Project Deliverables

- `data/` – Time-series datasets with selected XGB features  
- `pickles/` – Best trained models per stock  
- `images/` – Chart images for vision-based strategy classification

---

⚠️ **Disclaimer:**  this project is for **research and educational purposes only**. It does **not** constitute financial advice.




---

