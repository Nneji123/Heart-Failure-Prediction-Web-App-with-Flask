import joblib
import numpy as np


def predict_price(age,anaemia, creatinine_phos,diabetes,ejection,hbp,plat,serum_creatinine,serum_sodium,sex,smoking,time):
    test_data = np.array([[age,anaemia, creatinine_phos,diabetes,ejection,hbp,plat,serum_creatinine,serum_sodium,sex,smoking,time]])
    trained_model = joblib.load("heart_predictor_model.pkl")
    predictions = trained_model.predict(test_data)

    return predictions

