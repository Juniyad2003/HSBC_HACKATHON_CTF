Here's your enhanced and visually appealing README, now with thoughtful emoji placement for better engagement and clarity!

# 💳 Fraud Detection Using Machine Learning (XGBoost)

**📅 Date:** 27.07.2025  
**👤 Author:** Juniyad Tamboli, Kapurhol, Pune

## 🌟 Overview

This project delivers a comprehensive, end-to-end machine learning pipeline to detect fraudulent transactions in financial data, leveraging the power of the **XGBoost** classifier. It covers everything from preprocessing to model deployment, with top-notch accuracy and AUC, ensuring robust fraud detection for real-world applications.

## 🎯 Goals

- 🔍 **Accurate Fraud Prediction:** Build a robust ML model for identifying fraudulent transactions.
- ⚖️ **Imbalance Handling:** Use SMOTE to boost recall for fraud cases (minority class).
- 🛠️ **Model Optimization:** Tune XGBoost for optimal ROC-AUC performance.
- 💡 **Interpretability:** Highlight and explain the most influential fraud features.
- 🚀 **End-to-End Pipeline:** Deliver a ready-to-deploy model and web application.

## 📂 Dataset

- **📄 File:** `fraud_dataset.csv`
- **🔢 Records:** ~10,000 transactions
- **🧩 Features:**
  - **Categorical (encoded):**  
    - `merchant_category`
    - `customer_location`
    - `device_type`
  - **Numerical (scaled):**  
    - `previous_transactions`
    - `customer_age`
    - `amount`
  - **🚫 Dropped:**  
    - `transaction_id`, `customer_id`, `timestamp`

## 🧹 Data Processing Steps

1. 🔠 **Label Encoding:** All categorical features
2. 📏 **Feature Scaling:** Normalize numerical values (StandardScaler)
3. ⚖️ **Class Balancing:** SMOTE for fraud rate <15%

## 🤖 Model & Training

- **Algorithm:** XGBoost Classifier
- **Hyperparameter Tuning:** GridSearchCV on:
  - `n_estimators`: [150,max_depth`: [4,  - `learning_rate`: [0.03, 0.07, 0.1]
- **Validation:** Stratified 3-fold Cross-Validation
- **Data Split:** 80/20 stratified (class preservation)

## 📊 Evaluation Metrics

### **Classification Report:**
```
precision    recall  f1-score   support

0   0.9751     0.9985    0.9867   1963
1   0.9984     0.9745    0.9863   1962

Accuracy:                     0.9865   3925
Macro avg:                    0.9868   3925
Weighted avg:                 0.9868   3925
```

- **🏅 ROC-AUC Score:**  
  `0.9971659708797549`

## 🏆 Best Model Hyperparameters

```python
{
  'learning_rate': 0.1,
  'max_depth': 8,
  'n_estimators': 200,
  'scale_pos_weight': 0.99
}
```

## 🔑 Top Features (XGBoost Importance)

| Rank | Feature                | Importance |
|------|------------------------|------------|
| 🥇   | merchant_category      | 0.31       |
| 🥈   | previous_transactions  | 0.27       |
| 🥉   | customer_location      | 0.18       |
| 4️⃣   | device_type            | 0.14       |
| 5️⃣   | customer_age           | 0.05       |
| 6️⃣   | amount                 | 0.03       |

## 🌐 Web App Deployment

A user-friendly Flask-based web interface enables **real-time fraud detection**:

- **🔑 Required Features:**
  - `merchant_category`
  - `previous_transactions`
  - `customer_location`
  - `device_type`
  - `customer_age`
  - `amount`
- **⚡ Instant Results:**
  - Predicts **Fraudulent** or **Not Fraudulent** 🟢🔴 with a probability score!
- **🖥️ File Structure:**
  - `app.py` – Flask server
  - `index.html` – User interface
  - `Fraud_Detection_System.joblib` – Trained model
  - `scaler.pkl` – StandardScaler
  - `fraud_dataset.csv` – Dataset reference

## ⚙️ Setup & Usage

1. **📦 Requirements**
    - Python 3.7+
    - Libraries: flask, numpy, scikit-learn, xgboost, joblib

2. **▶️ Run the App**
    ```bash
    python app.py
    ```
    Open your browser to [`http://127.0.0.1:5000`](http://127.0.0.1:5000) 🚀

3. **🗃️ Deployment**
    - Place `Fraud_Detection_System.joblib` & `scaler.pkl` in the working directory

## 🏁 Conclusion

🎉 Your fraud detection system is ready for use!  
Built with XGBoost, the model demonstrates **exceptional accuracy and transparency**, fit for real-world banking and finance needs.  
For questions or collaboration, reach out to the author.

**👨💻 Author:**  
Juniyad Tamboli, Kapurhol, Pune

*Feel free to share, star, or reach out for partnerships! 🚀*

---
