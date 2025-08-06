# 🛡️ Fraud_Detection_XGBoost  
fraud_detection_xgboost.pptx  
fraud_detection_xgboost.pdf  

📊 Fraud Detection Using XGBoost 📈

This repository contains the **PPT**, **PDF**, and **source code** for my fraud detection project using **XGBoost**. Here's what you'll find:

🧾 **Dataset Overview**: Transaction-level structured data with features like merchant category, customer location, device type, and more.  
⚖️ **Data Imbalance Handling**: Implemented **SMOTE** to synthetically oversample the fraud class for better recall.  
🧠 **Model Building**: Utilized `XGBoostClassifier`, fine-tuned using `GridSearchCV` to maximize AUC and classification performance.  
📈 **Evaluation**: Achieved **98.65% accuracy** and **0.9971 ROC-AUC** score, with excellent fraud class performance as shown below:

| Metric       | Class 0 (Non-Fraud) | Class 1 (Fraud) |
| ------------ | ------------------- | --------------- |
| 🎯 Precision | 0.9751              | 0.9984          |
| ⚖️ Recall    | 0.9985              | 0.9745          |
| 📉 F1-Score  | 0.9867              | 0.9863          |

🔍 **Feature Importance**: Extracted key drivers of fraud including:
- `merchant_category` (0.3142)  
- `previous_transactions` (0.2708)  
- `customer_location` (0.1846)  
- `device_type`, `customer_age`, and `amount`

🚀 **How to Use**:  
Clone the repo, install the dependencies from `requirements.txt`, and run the Jupyter notebooks in the `notebooks/` folder to replicate the entire pipeline.

I genuinely enjoyed working on this high-impact project. It showcases my capability in end-to-end ML pipeline design, handling class imbalance, hyperparameter tuning, and model interpretability.  
Feel free to explore the code, share feedback, or connect with questions!

#MachineLearning #XGBoost #FraudDetection #DataScience #ModelExplainability #Python #SMOTE #AIProjects
