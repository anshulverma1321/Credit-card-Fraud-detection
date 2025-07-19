# 💳 Credit Card Fraud Detection System

This is a machine learning-powered Credit Card Fraud Detection system that helps identify suspicious transactions and alerts bank employees in real-time via SMS. It uses a trained model to analyze incoming transaction data and classify them as either **fraudulent** or **legitimate**.

---

## 🚀 Features

- Real-time fraud detection
- SMS alerts using Twilio for both fraud and legitimate transactions
- Web interface for input via Flask
- Data preprocessing with scaling and PCA
- REST API with CORS enabled

---

## 🧠 Tech Stack Used

- **Programming Language**: Python
- **Framework**: Flask
- **Libraries**:
  - `pandas`
  - `numpy`
  - `joblib`
  - `scikit-learn` (for model, scaler, and PCA)
  - `flask-cors`
  - `twilio` (for SMS alerts)

---

## 📦 Dataset

- Sourced from [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- The dataset contains transactions made by credit cards in September 2013 by European cardholders.

---

## 🔧 How to Run Locally

1. **Clone the repository:**
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
Install dependencies:
pip install -r requirements.txt

Ensure the following files are available in the models/ folder:
fraud_model.pkl
scaler.pkl
pca.pkl

Run the Flask app:
python app.py
Visit in browser:
http://127.0.0.1:5000/
📲 SMS Alerts
This project integrates Twilio to send SMS notifications when:

A fraudulent transaction is detected

A legitimate transaction is approved

⚠️ Make sure to configure your Twilio account SID, auth token, and phone numbers correctly in app.py.

**Project Structure**
├── app.py
├── models/
│   ├── fraud_model.pkl
│   ├── scaler.pkl
│   └── pca.pkl
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── requirements.txt

👨‍💻 Contributors
Anshul Verma – Project Lead & Backend Developer

Licence:This project is open-source and available under the MIT License.
