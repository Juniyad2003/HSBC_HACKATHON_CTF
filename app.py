from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load("Fraud_Detection_System.joblib")
scaler = joblib.load("scaler.pkl")  # StandardScaler used during training

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Extract input values from the form
    merchant_category = float(request.form["merchant_category"])
    previous_transactions = float(request.form["previous_transactions"])
    customer_location = float(request.form["customer_location"])
    device_type = float(request.form["device_type"])
    customer_age = float(request.form["customer_age"])
    amount = float(request.form["amount"])

    # Prepare and scale data
    features = np.array([[merchant_category, previous_transactions, customer_location,
                          device_type, customer_age, amount]])
    scaled_features = scaler.transform(features)

    # Make prediction
    prediction = model.predict(scaled_features)[0]
    probability = model.predict_proba(scaled_features)[0][1]

    result = "Fraudulent" if prediction == 1 else "Not Fraudulent"
    
    return render_template("index.html", prediction=result, prob=round(probability * 100, 2))

if __name__ == "__main__":
    app.run(debug=True)
