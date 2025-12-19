# 🎯 Deep Learning Pipeline Project for Time Series

This repository contains a modular **deep learning** project for **time series**, developed using YF stocks datasets.  

---

## 📘 Project Overview

The project implements all major stages of a **deep learning pipeline of time series**, including:

1. **Data preparation** – Download a TKL from YF + Exhogen indexes. Format as a table with some some 300 TS features
2. **Feature selection** – Using ML/XGB model to select best 20 features for each stock. Saving final table to a csv
3. **Select best NN model** – Testing LSTM, GRU, CNN and Mix-combinations of the three model agains the csv file
4. **Select best features for the NN** - Each MM is tested for 1) all features selected by XGB 2) Exhogen only features 3) TKL only data
5. **Future prediction** – Using best MM and X_features to predict the next few days of the TKL


---

🧩 Project Structure
```
{REPOSITORY_PATH}/
│
├── data/
│   ├── <stock1>.df.csv #(e.g. aapl.df.csv)
|   .
|   .
|   └── <stockn>.df.csv #(e.g. intc.df.csv)
│
├── notebooks/
│   ├── dataprep.ipynb
|   ├── racing_models.ipynb
│   ├── predict_future.ipynb
│   └──stocks.ipynb
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

Data prep and Feature selection are implemented in **dataprep.ipynb** notebook to ensure modularity, clarity, and reproducibility.
Selecintg NN model and X_features are implementd in  **race_mmodels.ipynb** 
Future prediciton is implemented in **predic_future.ipynb**


---

## 🧠 Data Leakage Prevention
We used seperate normalizaition/scalers for the y and for X

---

## 🚀 How to Run

1. **Clone** this repository to your local machine.
2. Create `.env` file in the root directory of the Runtime, e.g. `/contect/.env`
3. In `.env` define `PROJECT_PATH` to point to your local copy. e.g. `PROJECT_PATH=/content/drive/MyDrive/Projects/GitHub/Stocks/`
---

## 📊 Project Deliverables

TBD
---
