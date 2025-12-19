# 🎯 Deep Learning Pipeline Project for Time Series

This repository contains a modular **deep learning** project for **time series**, developed using YF stocks datasets.  

---

## 📘 Project Overview

The project implements all major stages of a **deep learning pipeline of time series**, including:

1. **Data preparation** – Download ticker data + exhogen indexes (S&P, NASDAQ, Oil, Gold, RealEstate, Inflation) into a table of ~300 ts features
2. **Feature recomandation** – Using ML/XGB to suggest 20 best features for each stock. Saving final table to a csv
3. **Select best NN and X_features** – Testing LSTM, GRU, CNN and Mix-combinations with few combination of X_features against the csv file
4. **Future prediction** – Using best MM and X_features to predict the next few days of the TKL

[notebooks/1spotify_dataprep.ipynb](notebooks/1spotify_dataprep.ipynb)
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
│   ├── dataprep.ipynb          # Data prep and Feature recommandation  
|   ├── racing_models.ipynb     # Select best MM and and X_feature 
│   ├── predict_future.ipynb    # Using best NN and X_features to predict the ticker's future
│   └── stocks.ipynb            # Running by order all notebooks
│
├── src/
│   ├── config.json              # Global project configuration file
│   ├── my_project_utils.py      # Helper functions (shared across notebooks). For future use, currently empty
│   └──__init__.py
│
├── images/                      # images of tkl graphs (to be used by fastai)
├── output/                      # Logs, results, and generated file
│
├── pickles/                     # Serialized models and dataframes
|   ├── <stock1>.best_model_name.X_features.keras
|   .
|   .
|   └── <stockn>.best_model_named,X_features.keras
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

1. **Clone** this repository to your local machine
2. In config.json define the target TKL, list of MM models, and other run parameters 
3. Open notebooks/stokcs.ipynb for a full execution, or any notebook for a partial run
4. Create `.env` file in the root directory of the Runtime, e.g. `/contect/.env`
5. In `.env` define `PROJECT_PATH` to point to your local copy. e.g. `PROJECT_PATH=/content/drive/MyDrive/Projects/GitHub/Stocks/`
6. Click Run All

---

## 📊 Project Deliverables

TBD
---
