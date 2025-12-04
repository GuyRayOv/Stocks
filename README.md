# 🎯 Machine Learning Pipeline Project

This repository contains a modular **deep learning of time seroiues** project, developed using YF stocks database.  

---

## 📘 Project Overview

The project implements all major stages of a **deep learning pipeline of time seriuses**, including:

1. **Data Preparation** – loading, cleaning, structuring a stock price dataset for XGB learning and for feature selection for deep learning 
2. **LSTM** – develop an LSTM model for each stock using the dataset from the first stage 
3. **GRU** – develop a GRU model for each stock using the dataset from the first stage
4. **Cascade LSTM GRU** – develop an hybrid model for each stock, starting with LSTM layers, followed by GRU layers
5. **Parallel LSTM GRU** – develop an hybrid model for each stock, executing LSTM and GRU in parallel, selecting the best features for each stock

Each stage is implemented in a dedicated **Jupyter notebook (.ipynb)** to ensure modularity, clarity, and reproducibility.

---

🧩 Project Structure
```
{REPOSITORY_PATH}/
│
├── data/
│   ├── README.md                # Kaggle dataset description
│   └── ProjectPresentation.pptx # Project presentation with visualizations
│
├── notebooks/
│   ├── 1stocks_dataprep_xgb.ipynb
│   ├── 2stocks_lstm.ipynb
│   ├── 3stocks_gru.ipynb
│   ├── 4stocks_cascade_lstm_gru.ipynb
|   ├── 5stocks_parallel_lstm_gru.ipynb
│   └── 6stocks_prediction.ipynb
│
├── src/
│   ├── config.json              # Global project configuration file
│   ├── my_project_utils.py      # Helper functions (shared across notebooks). For future use, currently empty
│   └── __init__.py
│
├── output/                      # Logs, results, and generated files
├── pickles/                     # Serialized models and data
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

TBD

Both subsets are processed independently throughout the pipeline. This behavior is controlled via the `split_df` flag in `config.json`.

---

## 🚀 How to Run

TBD

---

## 📊 Project Deliverables

TBD
---
