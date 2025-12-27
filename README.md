
# Stock Prediction & Investment Strategy System

## 📈 Project Overview

This project is a comprehensive AI-based system designed to analyze financial markets, predict future stock prices, and recommend investment strategies. It employs a **hybrid approach** combining:

1. **Machin Learning for Time Series:** XGBoost is selecting top features for a TS dataset 
2. **Deep Learning for Time Series:** LSTM, GRU, CNN models and minxed-cobination analyzing numerical data
3. **Computer Vision for Charts:** `fastai` model classifying stock chart images to determine market sentiment
4. **Generative AI:** An integrated LLM (Gemini) agent that parses natural language user prompts to trigger predictions

## 🚀 Key Features

### 1. Robust Data Pipeline

The system aggregates historical data for target stocks alongside key macroeconomic indicators to capture broader market trends:

* **Target Assets:** Specific stock tickers.
* **Macro Indicators:** Oil prices, Gold, S&P 500, NASDAQ, Real Estate indices, and Inflation rates.

### 2. Advanced Feature Engineering

* **Generation:** Creates approximately **300 time-series features**, including lags, min/max, mean, standard deviation, differences, and percentage changes.
* **Selection:** Utilizes **XGBoost (XGB)** to identify the most significant features, reducing the dataset to the **top 20 impactful columns** for efficient training.

### 3. Dual-Model Architecture

#### 🧠 A. Time-Series Regression (Price Prediction)

* **Architectures:** LSTM, GRU, CNN, and ensemble combinations.
* **Goal:** Predict specific future stock prices.
* **Performance:** The best model achieved an ** of ~97%**.

#### 👁️ B. Visual Classification (Strategy Recommendation)

* **Library:** `fastai` (Computer Vision).
* **Methodology:**
* Converts historical data into 1-year window plots.
* Classifies each plot based on future performance into three categories: **BUY, KEEP, SELL**.


* **Performance:** The best vision model achieved an accuracy/metric of **~73%**.

### 4. LLM-Powered User Interface

* Uses a **Gemini Agent** to interpret natural language prompts from the user.
* Automatically extracts the **Target Ticker (TKL)** and the **Prediction Horizon (days)** to run the inference pipeline.

---

## 📂 Repository Structure
---

### `train.ipynb` (Model Training)

<img width="1318" height="969" alt="image" src="https://github.com/user-attachments/assets/ad427a24-3962-4256-a112-f8b78922ade2" />

This notebook handles the entire training lifecycle:

1. Downloads historical data for stocks and macro indicators.
2. Generates and selects features (Top 20 via XGBoost).
3. Trains the Time-Series models (LSTM/GRU/CNN).
4. Generates historical plots and trains the `fastai` image classifier.
5. Saves the best models and the recommended feature set.
---

### `predict.ipynb` (Inference & Application)

<img width="1404" height="1055" alt="image" src="https://github.com/user-attachments/assets/cfaa52a4-47a9-4653-9b3b-6b55b8781e6d" />

This notebook serves as the application entry point:

1. **Input:** Accepts a natural language prompt (processed via Gemini API) to identify the stock and timeframe.
2. **Data Prep:** Downloads data up to the current date ("Today") and reproduces the specific features selected during training.
3. **Price Prediction:** Runs the best Time-Series model to forecast prices for the next few days.
4. **Strategy:** Generates a plot for the most recent year and uses the `fastai` model to classify the investment strategy (Buy/Keep/Sell) for the next quarter.



---

## 🛠️ Requirements

* Python 3.x
* pandas, numpy
* xgboost
* tensorflow / keras (for LSTM/GRU/CNN)
* fastai (for image classification)
* google-generativeai (for Gemini API integration)
* matplotlib / seaborn (for plot generation)

## 📊 Results Summary

| Model Type | Architecture | Task | Performance Metric |
| --- | --- | --- | --- |
| **Time Series** | LSTM/GRU/CNN | Price Prediction | **** |
| **Computer Vision** | fastai (CNN) | Strategy (Buy/Sell) | **Score \approx 73%$** |

---

## 📝 Usage

1. **Train the Models:**
Run `train.ipynb` to download data, process features, and save the trained model artifacts (`.h5`, `.pkl`, etc.).
2. **Make Predictions:**
Open `predict.ipynb` and provide a query (e.g., *"What is the outlook for NVDA for the next 7 days?"*). The system will:
* Parse the ticker and horizon.
* Fetch real-time data.
* Output the predicted price curve and the visual investment strategy.

---

🧩 Project Structure
```
{REPOSITORY_PATH}/
│
├── data/                                   # TS dataset for each stock, including exogen indexs and soem 20 XGB-recommended feaures
│   ├── <stock1>.df.csv
|   .
|   .
|   └── <stockn>.df.csv
│
├── notebooks/
│   ├── dataprep_for_train.ipynb            # Data prep and feature recommendation
│   ├── imagesprep_for_train.ipynb          # Images of graphs of the data
|   ├── train_models.ipynb                  # Select best MM and and X_feature
|   ├── train.ipynb                         # Runing first two notebooks
|   ├── llm_api.ipynb                       # Using Gemini to extract execution parameters from a natural langment proment, runing predit.ipynb with that
|   ├── predict.ipynb                       # Running the last two notebooks
|   ├── dataprep_for_inference.ipynb        # Refresh dataset with the latest YF infromation
│   ├── predict_future.ipynb                # Using best NN and X_features to predict ticker's future
│   └── recommand_invetmnet_strategy.ipynb  # Using best fastai model to generate recomendation from last 260days graph
│
├── src/
│   ├── config.json                         # Global project configuration file
│   ├── my_project_utils.py                 # Helper functions (shared across notebooks). For future use, currently empty
│   └──__init__.py
│
├── images/                                 # images of tkl graphs (used by fastai)
├── output/                                 # Logs, results, and generated file
│
├── pickles/                                # Serialized models and dataframes
|   ├── <stock1>.best_model_name.X_features.keras
|   .
|   .
|   └── <stockn>.best_model_named,X_features.keras
|
├── README.md                               # Project documentation (this file)
└── .gitignore                              # Ignored files and folders
```

## 🚀 How to Run

1. **Clone** this repository to your local machine
2. Create `.env` file in the root directory of the Runtime, e.g. `/contect/.env`
3. In `.env` define `PROJECT_PATH` to point to your local copy. e.g. `PROJECT_PATH=/content/drive/MyDrive/Projects/GitHub/Stocks/`
4. To run [llm_api.ipynb](notebooks/llm_api.ipynb) define your Google API key in `.env` file, i.e `GOOGLE_API_KEY=apikey`
5. To run [train.ipynb](notebooks/train.ipynb) define your target TKL and other train parameters in [config.json](src/config.json)
6. Open [train.ipynb](notebooks/train.ipynb) to train the best model for the TKL, **OR**
7. [llm_api.ipynb](notebooks/llm_api.ipynb) to predict the future of this TKL
8. Click Run All

---

## 📊 Project Deliverables

1. data/*.csv:  a ts dataset each stock, with its ~20 recomanded X_features. Input for the train
2. pickels/*.pkl: a ts dataset for each stock with its ~20 recomanded X_features. Input for the prediciton
3. pickles/*.keras: a best model file for each stock. Input for the prediction
4. images/*.png: image graph files for each stock. Input for fastai
---
