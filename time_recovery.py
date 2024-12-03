import joblib
import numpy as np

# Load the trained Random Forest model
model = joblib.load("rfr_model.sav")

def predict_recovery(max_knee_angle):

    try:
        # Ensure input is in the correct shape for prediction
        input_data = np.array([[max_knee_angle]])
        # Make prediction
        prediction = model.predict(input_data)[0]
        return prediction
    
    except Exception as e:
        raise ValueError(f"Prediction error: {str(e)}")
