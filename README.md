# 🎯 Deep Learning study project for Time Series dataset

This repository contains a modular **deep learning** project of **time series**, developed using YF'database  

---

## 📘 Project Overview

The project implements major stages of a deep learning pipeline for time series dataset, including:
1. **Preparation:** an historical ticker data + exhogen indexes (S&P, NASDAQ, Oil, Gold, RealEstate, Inflation) formated into a ts table of some 300 "rolling" features
2. **Feature recomandation:** Using ML/XGB to "suggest" best 20 features for each stock
3. **Select NN and X_features:** Testing LSTM, GRU, CNN and mixed combinations with several subsets of features from XGB's recommendation 
4. **Future prediction** – Using best MM and X_features to predict the next few days of the TKL

---

🧩 Project Structure
```
{REPOSITORY_PATH}/
│
├── data/                        # TS dataset for each TKL, incouding exhogen indexs and ~20 XGB-recommended feaures
│   ├── <stock1>.df.csv
|   .
|   .
|   └── <stockn>.df.csv
│
├── notebooks/
│   ├── dataprep_for_train.ipynb      # Data prep and feature recommendation
|   ├── train_models.ipynb            # Select best MM and and X_feature
|   ├── train.ipynb                   # Runing first two notebooks
|   ├── dataprep_for_inference.ipynb  # Refresh dataset with the latest YF infromation
│   ├── predict_future.ipynb          # Using best NN and X_features to predict ticker's future
│   └── predict.ipynb                 # Running the last two notebooks
│
├── src/
│   ├── config.json                   # Global project configuration file
│   ├── my_project_utils.py           # Helper functions (shared across notebooks). For future use, currently empty
│   └──__init__.py
│
├── images/                          # images of tkl graphs (to be used by fastai)
├── output/                          # Logs, results, and generated file
│
├── pickles/                         # Serialized models and dataframes
|   ├── <stock1>.best_model_name.X_features.keras
|   .
|   .
|   └── <stockn>.best_model_named,X_features.keras
|
├── README.md                        # Project documentation (this file)
└── .gitignore                       # Ignored files and folders
```

## 🚀 How to Run

1. **Clone** this repository to your local machine
2. Create `.env` file in the root directory of the Runtime, e.g. `/contect/.env`
5. In `.env` define `PROJECT_PATH` to point to your local copy. e.g. `PROJECT_PATH=/content/drive/MyDrive/Projects/GitHub/Stocks/`
3. In [config.json](src/config.json) define your target TKL, your list of MM models, and other run parameters 
4. Open [train.ipynb](notebooks/train.ipynb) to generate best model for the TKL, **or**
5. Open [predict.ipynb](notebooks/predict.ipynb) to future prediciton for the TKL
6. Click Run All

---

## 📊 Project Deliverables

1. data/*.csv:  a ts dataset each stock, with its ~20 recomanded X_features. Input for the train
2. pickels/*.pkl: a ts dataset for each stock with its ~20 recomanded X_features. Input for the prediciton
3. pickles/*.keras: a best model file for each stock. Input for the prediction
4. images/*.png: image graph files for each stock. Input for fastai
---
