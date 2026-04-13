# 💳 Credit Card Fraud Detection System

A Machine Learning-powered system that detects fraudulent transactions and alerts bank staff in real-time via SMS.

---

## 🚀 Features

* 🔍 Real-time fraud detection
* 📩 SMS alerts using Twilio
* 🌐 Web interface using Flask
* ⚙️ Data preprocessing (Scaling + PCA)
* 🔗 REST API with CORS enabled

---

## 🧠 Tech Stack

**Programming Language:** Python
**Framework:** Flask

**Libraries Used:**

* pandas
* numpy
* joblib
* scikit-learn
* flask-cors
* twilio

---

## 📦 Dataset

* Kaggle Credit Card Fraud Detection Dataset
* Transactions from European cardholders (September 2013)
* Highly imbalanced dataset

---

## 📁 Project Structure

```
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
```

---

## 🔧 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Ensure Model Files Exist

Make sure these files are inside the `models/` directory:

* fraud_model.pkl
* scaler.pkl
* pca.pkl

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and go to:

http://127.0.0.1:5000/

---

## 📲 SMS Alerts (Twilio Integration)

This system sends SMS notifications when:

* 🚨 A fraudulent transaction is detected
* ✅ A legitimate transaction is approved

### ⚠️ Configuration

Update the following in `app.py`:

* Account SID
* Auth Token
* Twilio Phone Number
* Receiver Phone Number

---

## 👨‍💻 Author

**Anshul Verma**
B.Tech CSE (AI & ML)

---

## 📜 License

This project is licensed under the MIT License.
