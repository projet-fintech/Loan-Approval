import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

## Load the model
Model = pickle.load(open('Loan_Prediction_Finale_Model.pkl','rb'))
Scaler = pickle.load(open('FinaleScaler.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        data = request.json['data']
        # Convert input to a DataFrame for compatibility
        input_df = pd.DataFrame([data])
        # Preprocess the data using Scaler's transform method
        preprocessed_data = Scaler.transform(input_df)
        # Predict using the model
        predicted_label = Model.predict(preprocessed_data)[0]
        # Return the result
        result = "Approved" if predicted_label == 1 else "Not Approved"
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
