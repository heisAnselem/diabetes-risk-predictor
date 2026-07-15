# Diabetes Risk Predictor

A machine learning pipeline and FastAPI service that predicts diabetes risk
from health behavior and demographic data, trained on the CDC BRFSS 2015
survey (~400,000 responses).

**Live API:** https://diabetes-risk-predictor.fastapicloud.dev/predict

**Docs:** https://diabetes-risk-predictor.fastapicloud.dev/docs

## Dataset

CDC BRFSS 2015 survey. 22 variables were selected during EDA based on
documented diabetes risk factors — see [./notebooks/Data-Cleaning-and-EDA.ipynb](./notebooks/Data-Cleaning-and-EDA.ipynb)
for the full list and cleaning steps.

## Model

The [V1](./app/artifacts/v1_model.pkl) model  is trained on **11 of the 22**
EDA features:

`BMI`, `Age`, `Income`, `PhysicalHealth`, `GeneralHealth`, `Education`,
`MentalHealth`, `HighBp`, `HighCholesterol`, `Fruits`, `Smoke100`

Class imbalance in the target is handled via resampling (`imbalanced-learn`).
Full training and evaluation process: [./notebooks/model_training.ipynb](./notebooks/model_training.ipynb).

> Note: the API asks for education level using Nigeria's schooling
> categories (primary / junior secondary / senior secondary / university)
> rather than the original BRFSS US education codes, a deliberate
> localization, not a 1:1 codebook mapping.

## API

Built with FastAPI. Two endpoints:

GET /    → {"status": "healthy"}

POST /predict    → risk prediction

**Request** (`PredictionRequest`):
```json
{
  "bmi": 25.0,
  "age": 1,
  "income": 2,
  "physical_health": 0,
  "general_health": 3,
  "education": 5,
  "mental_health": 0,
  "blood_pressure": 0,
  "blood_cholesterol": 0,
  "fruits": 1,
  "smokes": 0
}
```
Field values follow BRFSS-style coded ranges — see [./app/schemas.py](./app/schemas.py) for the
full description and valid range of each field.

**Response** (`PredictionResponse`):
```json
{
  "prediction": "You are currently not at risk of diabetes",
  "disclaimer": "This is a tool, not a doctor. Please consult a doctor for proper medical diagnosis."
}
```


## Setup (local)

```bash
git clone https://github.com/heisAnselem/diabetes-risk-predictor.git

cd diabetes-risk-predictor

uv sync

# to explore the notebooks
uv run jupyter lab

# to run the API locally
uv run fastapi dev app/main.py
```