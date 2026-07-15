from pathlib import Path
import joblib
import pandas as pd
from fastapi import FastAPI,Depends, Path,Request
from app import PredictionRequest,PredictionResponse


app = FastAPI(title="Diabetes Risk Prediction API",description="This API predicts the risk of diabetes based on user input data.",version="0.1.0")

_cached_model = None

def get_model():
    """Helper function to load the model into memory only when needed."""
    global _cached_model
    if _cached_model is None:
        # Build absolute path to prevent container path mismatches
        base_dir = Path(__file__).resolve().parent
        model_path = base_dir / "artifacts" / "v1_model.pkl"
        _cached_model = joblib.load(model_path)
    return _cached_model

@app.get("/")
def health_check():
    return {"status": "healthy"}

@app.post(path="/predict",response_model=PredictionResponse)
async def predict_diabetes_risk(data: PredictionRequest):
        model = get_model()
        # mapping inputs to exact feature name model was trained on 
        values = data.model_dump()
        input = {
        "BMI": values["bmi"],
        "Age": values["age"],
        "Income": values["income"],
        "PhysicalHealth": values["physical_health"],
        "GeneralHealth": values["general_health"],
        "Education": values["education"],
        "MentalHealth": values["mental_health"],
        "HighBp": values["blood_pressure"],
        "HighCholesterol": values["blood_cholesterol"],
        "Fruits": values["fruits"],
        "Smoke100": values["smokes"]
        }
        df = pd.DataFrame([input])
        # prediction
        prediction = model.predict(df)
        if prediction == 1:
            # patient is at risk of diabetes 
            prediction_message = "Potential Diabetes risk currently detected"
        else:
            # patient is not at risk of diabetes
            prediction_message = "You are currently not at risk of diabetes "
        return PredictionResponse(prediction=prediction_message)   