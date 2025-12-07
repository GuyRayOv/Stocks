# 🎯 Deep Learning  Pipeline Project for Time Series

This repository contains a modular **deep learning** project for **time series**, developed using YF stocks datasets.  

---

## 📘 Project Overview

The project implements all major stages of a **deep learning pipeline of time series**, including:

1. **Data Preparation** – loading, cleaning, feature engineering, features selections a stock price dataset
2. **XGB** – develop an XGB model for each stock using the dataset from the first stage 
3. **LSTM** – develop an LSTM model for each stock using the dataset from the first stage 
4. **GRU** – develop a GRU model for each stock using the dataset from the first stage
5. **Cascade LSTM GRU** – develop an hybrid model for each stock, starting with LSTM layers, followed by GRU layers
6. **Parallel LSTM GRU** – develop an hybrid model for each stock, executing LSTM and GRU in parallel, selecting the best features for each stock

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
│   └── __init__.py
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

TBD

Both subsets are processed independently throughout the pipeline. This behavior is controlled via the `split_df` flag in `config.json`.

---

## 🚀 How to Run

1. **Clone** this repository to your local machine.
2. Create `.env` file in the root directory of the Runtime, e.g. `/contect/.env`
3. In `.env` define `PROJECT_PATH` to point to your local copy. e.g. `PROJECT_PATH=/content/drive/MyDrive/Projects/GitHub/Stocks/`
---

## 📊 Project Deliverables

TBD
---
