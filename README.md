#  🩺 Diabetes Risk Predictor

**A Data-Driven Web App for Predicting Diabetes Risk Using Logistic Regression**

---

## Project Overview

This project predicts the likelihood of diabetes among adults using health behavior data from the **CDC BRFSS 2015** survey.  
It applies a **Logistic Regression** model to identify major risk factors and estimate the probability of diabetes based on lifestyle and health indicators.  

The final version will be deployed as an **interactive Streamlit app**, allowing users to input personal data and receive real-time diabetes risk predictions.

---

## Dataset

- **Source:** [CDC BRFSS 2015 — Behavioral Risk Factor Surveillance System](https://www.cdc.gov/brfss/annual_data/annual_2015.html) 
- **Kaggle Version Used:** [Diabetes Health Indicators Dataset (BRFSS 2015)](https://www.kaggle.com/datasets/cdc/behavioral-risk-factor-surveillance-system) 
- **Size:** 400,000+ survey responses from adults across the United States  
- **Content:** Health behaviors, medical conditions, and demographic information  
- **Note:** The raw dataset is excluded due to its size.  
  The cleaned dataset used for modeling is available at:  
  `data/processed/BRFSS-2015-cleaned.csv`

---

## Processing Steps

- Removed irrelevant columns and duplicate entries  
- Replaced invalid codes (e.g., 88 → 0 in health day columns)  
- Encoded categorical and binary variables for model compatibility  
- Reversed ordinal scale for *GeneralHealth* to maintain consistency  
- Exported cleaned dataset for EDA and modeling  

*(All preprocessing steps are detailed in `notebooks/data_cleaning.ipynb`)*

---

## Key Features

- **Algorithm:** Logistic Regression  
- **Input Data:** Health behavior and demographic indicators  
- **Tech Stack:**  
  - **Python** — Core implementation  
  - **NumPy & Pandas** — Data handling  
  - **Matplotlib & Seaborn** — Visualization  
  - **Scikit-learn** — Modeling  
  - **Streamlit** — App deployment  
- **Objective:** Build an interpretable, lightweight predictive model deployable for real-time diabetes risk analysis  

---

## Result and Next Steps

- **Data Cleaning:** ✅ Completed  
- **Exploratory Data Analysis:** 🔄 In Progress  
- **Model Training & Evaluation:** ⏳ Upcoming  
- **Streamlit App Deployment:** ⏳ Upcoming  

---
---

## Future Work

- Perform Exploratory Data Analysis (EDA)  
- Train and fine-tune the Logistic Regression model  
- Integrate model into Streamlit for deployment  
- Add interpretability tools (feature importance visualization)

---

## Live Demo

**Coming soon on Streamlit!**