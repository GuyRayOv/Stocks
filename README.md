# 🎯 Deep Learning Pipeline Project for Time Series

This repository contains a modular **deep learning** project for **time series**, developed using YF stocks datasets.  

---

## 📘 Project Overview

The project implements all major stages of a **deep learning pipeline of time series**, including:

1. **Data Preparation** – Download a TKL from YF + Exhogen indexes, data prep as time series table for ML/XGB (total of ~300 features)
2. **Feature Selection** – Using ML/XGB model to select best 20 features for each stock. Saving the 
3. **Racing NN models** – Testing LSTM, GRU, CNN and Mix-combinations of the three model. Each model is tested for: 1) all features selected bu XGB 2) only exhogen features 3) only the TKL data
4. **Prediction** – Using best MM model and best features (selecetd by the next NN model) to predict next few days for the TKL

Each stage is implemented in a dedicated **Jupyter notebook (.ipynb)** to ensure modularity, clarity, and reproducibility.

---

🧩 Project Structure
```
{REPOSITORY_PATH}/
│
├── data/
│   ├── <stock1>.df.csv #(e.g. aapl.df.csv)
|   .
|   .
|   .
|   └── <stockn>.df.csv #(e.g. intc.df.csv)
│
├── notebooks/
│   ├── stocks_dataprep.ipynb
|   ├── stocks_xgb.ipynb
│   ├── stocks_lstm.ipynb
│   ├── stocks_gru.ipynb
│   ├── stocks_cascade_lstm_gru.ipynb
|   ├── stocks_parallel_lstm_gru.ipynb
│   └── stocks_prediction.ipynb
│
├── src/
│   ├── config.json              # Global project configuration file
│   ├── my_project_utils.py      # Helper functions (shared across notebooks). For future use, currently empty
│   └──__init__.py
│
├── output/                      # Logs, results, and generated files
├── pickles/                     # Serialized models and dataframes
│
|
├── README.md                    # Project documentation (this file)
└── .gitignore                   # Ignored files and folders
```

---

## ⚙️ Notebook Workflow

TBD
---

## 🧠 Data Leakage Prevention
Seperate normalizaiton for the exhoges features and for target based time series features (rolling window etc)

---

## 🚀 How to Run

1. **Clone** this repository to your local machine.
2. Create `.env` file in the root directory of the Runtime, e.g. `/contect/.env`
3. In `.env` define `PROJECT_PATH` to point to your local copy. e.g. `PROJECT_PATH=/content/drive/MyDrive/Projects/GitHub/Stocks/`
---

## 📊 Project Deliverables

TBD
---
