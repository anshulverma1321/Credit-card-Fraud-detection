💳 Credit Card Fraud Detection System

A Machine Learning-powered system that detects fraudulent transactions and alerts bank staff in real-time via SMS.

🚀 Features
🔍 Real-time fraud detection
📩 SMS alerts using Twilio
🌐 Web interface using Flask
⚙️ Data preprocessing (Scaling + PCA)
🔗 REST API with CORS enabled
🧠 Tech Stack

Language: Python
Framework: Flask

Libraries:

pandas
numpy
joblib
scikit-learn
flask-cors
twilio
📦 Dataset
Kaggle Credit Card Fraud Detection Dataset
Transactions from European cardholders (Sept 2013)
Highly imbalanced dataset
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
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
▶️ Run the App
python app.py

Open: http://127.0.0.1:5000/

📲 SMS Alerts (Twilio)

Configure in app.py:

Account SID
Auth Token
Phone numbers
👨‍💻 Author

Anshul Verma
B.Tech CSE (AI & ML)

📜 License

MIT License
