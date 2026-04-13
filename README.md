💳 Credit Card Fraud Detection System

A Machine Learning-powered Credit Card Fraud Detection system that identifies suspicious transactions and notifies bank staff in real-time via SMS.

This project leverages a trained ML model to classify transactions as fraudulent or legitimate, ensuring faster and smarter fraud prevention.

🚀 Features
🔍 Real-time Fraud Detection
📩 Instant SMS Alerts using Twilio
Fraudulent transactions
Legitimate transaction confirmations
🌐 Web Interface using Flask
⚙️ Data Preprocessing
Feature scaling
PCA (Dimensionality Reduction)
🔗 REST API with CORS enabled
🧠 Tech Stack
💻 Programming Language
Python
🌐 Framework
Flask
📚 Libraries Used
pandas
numpy
joblib
scikit-learn
flask-cors
twilio
📦 Dataset
Source: Kaggle Credit Card Fraud Detection Dataset
Contains real-world transactions made by European cardholders (September 2013)
Highly imbalanced dataset with fraudulent and legitimate transactions
📁 Project Structure
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
🔧 Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Ensure Model Files Exist

Make sure the following files are inside the models/ directory:

fraud_model.pkl
scaler.pkl
pca.pkl
▶️ Run the Application
python app.py

Open your browser and go to:

http://127.0.0.1:5000/
📲 SMS Alerts (Twilio Integration)

This system sends SMS notifications when:

🚨 A fraudulent transaction is detected
✅ A legitimate transaction is approved
⚠️ Important Setup

Before running, configure your Twilio credentials inside app.py:

Account SID
Auth Token
Sender & Receiver Phone Numbers
👨‍💻 Contributor
Anshul Verma
Project Lead & Backend Developer
📜 License

This project is open-source and available under the MIT License.

🌟 Future Improvements (Optional but Powerful)
Add dashboard with analytics (fraud trends 📊)
Deploy on cloud (AWS / Render / Railway)
Add authentication for bank employees
Improve model with deep learning
