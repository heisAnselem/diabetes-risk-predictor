# Diabetes Risk Predictor

An end-to-end machine learning pipeline and REST API for predicting diabetes risk using health behavior and demographic data from the CDC BRFSS 2015 survey.

---

## Overview

This project covers the full lifecycle of a machine learning product — from raw survey data through cleaning, exploratory analysis, feature engineering, model training, and a **FastAPI** inference endpoint that returns a risk probability given a set of personal health indicators.

The dataset is the CDC Behavioral Risk Factor Surveillance System (BRFSS) 2015: $\approx 400,000$ adult survey responses across the United States. From the full survey, 22 variables were selected based on established diabetes risk factors documented in the BRFSS codebook — spanning health conditions, lifestyle behaviors, and demographics.

---

## Project Structure

```
diabetes-risk-predictor/
├── data/
│   ├── raw/
│   │   └── 2015.csv.zip        # original BRFSS download (not tracked)
│   └── processed/              # cleaned outputs land here (generated, not tracked)
├── notebooks/
│   └── Data-Cleaning-and-EDA.ipynb
├── pyproject.toml
├── uv.lock
└── README.md
```

Planned additions:

```
├── src/
│   ├── train.py
│   ├── evaluate.py
│   └── schemas.py
├── api/
│   └── main.py
└── models/
```

---

## Pipeline Progress

| Stage | Status |
|---|---|
| Data cleaning | complete |
| Exploratory data analysis | complete |
| Model training and evaluation | in progress |
| FastAPI inference endpoint | upcoming |
| Deployment | upcoming |

---

## Features

22 variables drawn from the BRFSS codebook, selected for their documented relationship with diabetes risk:

| Variable | Description | Type |
|---|---|---|
| `Diabetes` | Target — diabetic vs. non-diabetic | Binary |
| `HighBp` | Ever told has high blood pressure | Binary |
| `HighCholesterol` | Ever told cholesterol is high | Binary |
| `CheckedCholesterol` | How recently cholesterol was checked | Nominal |
| `BMI` | Body mass index | Continuous |
| `Smoke100` | Smoked at least 100 cigarettes in lifetime | Binary |
| `Stroke` | Ever told had a stroke | Binary |
| `HeartDisease` | Ever reported CHD or MI | Binary |
| `PhysicalActivity` | Physical activity in past 30 days | Binary |
| `Fruits` | Consumes fruit ≥1x per day | Binary |
| `Vegetables` | Consumes vegetables ≥1x per day | Binary |
| `HeavyDrinking` | Heavy alcohol consumption | Binary |
| `HealthCareAccess` | Has any health care coverage | Binary |
| `MedicalCost` | Could not see doctor due to cost | Binary |
| `GeneralHealth` | Self-reported general health (1–5) | Ordinal |
| `MentalHealth` | Days mental health was not good (past 30) | Continuous |
| `PhysicalHealth` | Days physical health was not good (past 30) | Continuous |
| `DifficultyWalking` | Serious difficulty walking or climbing stairs | Binary |
| `Sex` | Respondent sex | Binary |
| `Age` | Age group (14-level category) | Ordinal |
| `Education` | Highest education level completed | Ordinal |
| `Income` | Annual household income bracket | Ordinal |

---

## Data Cleaning

Full details in `notebooks/Data-Cleaning-and-EDA.ipynb`. Key steps:

- Loaded only the 22 relevant columns directly from the compressed raw file
- Replaced BRFSS sentinel codes (e.g. `7`, `9`, `77`, `99`) with `NaN` per codebook definitions
- Scaled `BMI` from its encoded integer form by dividing by 100
- Replaced `88` with `0` in `MentalHealth` and `PhysicalHealth` (88 = "none" in the codebook)
- Filtered to binary target: diabetic (`1`) vs. no diabetes (`3`); excluded gestational and pre-diabetes cases
- Removed duplicate rows to prevent data leakage
- Standardised all binary columns to `0 = absence of risk factor`, `1 = presence` — including correcting inversely-coded variables like `HighBp` and `HeavyDrinking`
- Reversed the `GeneralHealth` ordinal scale so that `1 = poor` and `5 = excellent`, for directional consistency across the feature set
- Mapped `CheckedCholesterol` to human-readable labels (`recently`, `not_recently`, `never`, `unknown`)

---

## Exploratory Data Analysis
Full details in `notebooks/Data-Cleaning-and-EDA.ipynb`. Key steps:

### Missing Data

- Computed per-column missing percentages and visualised their distribution by diabetes status
- Removed rows missing ≥50% of columns (too incomplete to be useful)
- Analysed missingness patterns via heatmap — found column-driven missing clusters with no significant row-level missingness after the row threshold step
- Classified columns into **MAR** (structurally missing — impute and add indicator flag) vs **MCAR** (randomly missing — impute only)

After running missing-flag cross-tabulations against the target:
- Only `HighCholesterolMissing` showed a meaningful distribution difference between diabetic and non-diabetic groups — all other flags were retained and later dropped
- The `unknown` category in `CheckedCholesterol` was dropped after correlation analysis confirmed it contributed no meaningful signal

**Imputation strategy:**
- Continuous (`BMI`, `MentalHealth`, `PhysicalHealth`) → median
- Binary and ordinal columns → mode

### Key Findings

**Continuous features**

- `BMI` shows the clearest separation: diabetics have a notably higher median and wider spread — strong predictive signal
- `PhysicalHealth`: diabetics report more unhealthy days, though with overlap
- `MentalHealth`: weak relationship with diabetes; similar distributions across both classes

**Binary features**

- Strong positive association with diabetes: `HighBp`, `HighCholesterol`, `HeartDisease`, `Stroke`, `DifficultyWalking`
- Protective associations: `PhysicalActivity`, `Fruits`, `Vegetables`
- Weak or negligible separation: `HeavyDrinking`, `Sex`, `HealthCareAccess`, `MedicalCost`

**Ordinal features**

- `GeneralHealth`: clear inverse relationship — poorer health strongly associated with higher diabetes rates
- `Age`: monotonically increasing diabetes risk across age groups
- `Education` and `Income`: higher levels associated with lower diabetes prevalence, likely mediated through lifestyle and healthcare access

**Correlation**

- `Sex` correlates below 0.1 with nearly every feature including the target — lowest-priority predictor in the set
- `GeneralHealth`, `PhysicalHealth`, `MentalHealth`, and `DifficultyWalking` are moderately intercorrelated
- `CheckedCholesterol_recently` shows expected negative correlation with `CheckedCholesterol_never`

---

## Modelling

Model selection is open. The target is binary with notable class imbalance — diabetics are a clear minority. Logistic regression will serve as the interpretable baseline; tree-based and ensemble methods will be trained and compared. Primary evaluation metrics will be ROC-AUC and macro F1, given the imbalance. Class imbalance will be addressed through `class_weight` adjustments during training.

---

## API (upcoming)

The trained model will be served via **FastAPI**. Planned endpoint:

```
POST /predict
```

Request body:

```json
{
  "HighBp": 1,
  "HighCholesterol": 0,
  "BMI": 28.4,
  "Smoke100": 0,
  "PhysicalActivity": 1,
  "Age": 7,
  "Income": 5
}
```

Response:

```json
{
  "probability": 0.34,
  "prediction": 0
}
```

Interactive docs available at `/docs` after startup.

---

## Setup

```bash
git clone https://github.com/heisAnselem/diabetes-risk-predictor.git
cd diabetes-risk-predictor

uv sync

# download the BRFSS 2015 dataset and place it at data/raw/2015.csv.zip

uv run jupyter lab
```

---

## Tech Stack

| Layer | Tools |
|---|---|
| Data | Pandas, NumPy |
| Analysis | Matplotlib, Seaborn |
| Modelling | Scikit-learn |
| API | FastAPI, Uvicorn, Pydantic |
| Environment | Python 3.14, uv |