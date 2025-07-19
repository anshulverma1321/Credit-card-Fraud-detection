from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd
from twilio.rest import Client
from flask_cors import CORS



app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
# Load the trained model, scaler, and PCA
model = joblib.load('models/fraud_model.pkl')
scaler = joblib.load('models/scaler.pkl')
pca = joblib.load('models/pca.pkl')

# Twilio configuration (Replace with your actual credentials)
account_sid = 'ACd16b3d39d1f2dd2998a531051fb2bac1'
auth_token = 'd2823af870abd8a5d4a1c6a2a2c9ca5c'
twilio_client = Client(account_sid, auth_token)

@app.route('/')
def home():
    return render_template('index.html')  # Renders the frontend
  


@app.route('/detect_fraud', methods=['POST'])
def detect_fraud():
    
    try:
        # Parse the JSON input from the form
        data = request.get_json()
        print(f"Data received: {data}")
        transaction_time = float(data['transaction_time'])
        transaction_amount = float(data['transaction_amount'])

       

        # Prepare input for prediction
        input_data = pd.DataFrame([[transaction_time, transaction_amount]], columns=['Time', 'Amount'])
        print(f"Input data for prediction: {input_data}")
        scaled_data = scaler.transform(input_data)
        print(f"Scaled data: {scaled_data}")

        pca_data = pca.transform(scaled_data)
        print(f"PCA transformed data: {pca_data}")

        # Make the fraud detection prediction
        prediction = model.predict(pca_data)
        print(f"Prediction: {prediction}")

        # fraudulent_transactions = data[data['Class'] == 1]
        # print(fraudulent_transactions.head())

        # Check if fraud is detected and send corresponding SMS
        if prediction[0] == 1:
            # Fraud detected, send a fraud alert SMS
            send_sms_alert(transaction_time, transaction_amount, fraud_detected=True)
            print("Fraud detected, SMS alert sent.")
            return jsonify({'fraud': True})  # Return fraud detected response
        else:
            # Legitimate transaction, send a legitimate transaction SMS
            send_sms_alert(transaction_time, transaction_amount, fraud_detected=False)
            print("Legitimate transaction, SMS sent.")
            return jsonify({'fraud': False})  # Return no fraud detected response

    except Exception as e:
        return jsonify({'error': str(e)})

# Function to send SMS alerts using Twilio for both legitimate and fraudulent transactions
def send_sms_alert(transaction_time, transaction_amount, fraud_detected):
    try:
        if fraud_detected:
            message_body = f"Fraud Alert! Suspicious transaction detected. Time: {transaction_time}, Amount: {transaction_amount}"
        else:
            message_body = f"Transaction Approved. Time: {transaction_time}, Amount: {transaction_amount}."

        message = twilio_client.messages.create(
            body=message_body,
            from_='+17185784309',  # Your Twilio phone number
            to='+919616670357'      # Recipient phone number
        )
        print(f'SMS sent: {message.sid}')
    except Exception as e:
        print(f'Failed to send SMS: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
