from typing import Annotated
from pydantic import BaseModel, Field

#  descriptions are questions from the BRFSS 2015 codebook
class PredictionRequest(BaseModel):
    bmi: Annotated[float, Field(gt=0.0,
                                lt=250.0,
                                title="Body Mass Index (BMI) of the individual.",
                                description="What is your BMI?",
                                examples=[25.0])]
    age: Annotated[int, Field(gt=0,
                              le=13,
                              title="Age range of the individual.",
                              description="What is your age range? (1: 18-24, 2: 25-29, 3: 30-34, 4: 35-39, 5: 40-44, 6: 45-49, 7: 50-54, 8: 55-59, 9: 60-64, 10: 65-69, 11: 70-74, 12: 75-79, 13: 80 or older)",
                              examples=[1])]
    income: Annotated[int, Field(
                                gt=0,
                                le=8,
                                title="Income level of the individual.",
                                description="What is the level of your annual income from all sources? (1: < $10,000; 2: $10,000-$14,999; 3: $15,000-$19,999; 4: $20,000-$24,999; 5:$25,000-$34,999; 6: $35,000-$49,999; 7: $50,000-$69,999; 8: $70000 or more )",
                                examples=[2])]
    physical_health: Annotated[int, Field(
                                ge=0,
                                le=30,
                                title="Physical health status of the individual.",
                                description="Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?",
                                examples=[0])]
    general_health: Annotated[int, Field(
                                ge=0,
                                le=10,
                                title="General health status of the individual.",
                                description="How would you rate your general health? (1: poor, 2: fair, 3: good, 4: very good, 5: excellent)",
                                examples=[3])]
    education: Annotated[int, Field(
                                gt=0,
                                le=6,
                                title="Education level of the individual.",
                                description="What is the highest school level you completed? (1:kindergarten or never attended school, 2: primary, 3:junior secondary, 4: senior secondary, 5: currently in University, 6:university or higher levels)",
                                examples=[5])]
    mental_health: Annotated[int, Field(
                                ge=0,
                                le=30,
                                title="Mental health status of the individual.",
                                description="Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?",
                                examples=[0])]
    blood_pressure: Annotated[int, Field(
                                ge=0,
                                le=1,
                                title=" Blood Pressure status of the individual.",
                                description="Have you ever been told by a doctor, nurse or other health professional that you have high blood pressure? (0: no, 1: yes)",
                                examples=[0])]
    blood_cholesterol: Annotated[int, Field(
                                ge=0,
                                le=1,
                                title=" Blood Cholesterol status of the individual.",
                                description="Have you ever been told by a doctor, nurse or other health professional that your blood cholesterol is high? (0: no, 1: yes)",
                                examples=[0])]
    fruits: Annotated[int, Field(
                                ge=0,
                                le=1,
                                title="Fruits consumption status of the individual.",
                                description="Do you consume fruits regularly? (0: no, 1: yes)",
                                examples=[1])]
    smokes: Annotated[int, Field(
                                ge=0,
                                le=1,
                                title="Smoking status of the individual.",
                                description="Have you smoked at least 100 cigarettes in your entire life? (0: no, 1: yes)",
                                examples=[0])]

class PredictionResponse(BaseModel):
    prediction: Annotated[str, Field(description="The prediction risk message.")]
    disclaimer: Annotated[str, Field(default="This is a tool,not a doctor. Please consult a doctor for proper medical diagnosis. ", description="Disclaimer message on consulting tool use")]