import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

## Load the model
RandomForestModel=pickle.load(open('PredictLoan_Model.pkl','rb'))


def preprocess_data(data):
    # Log transformations
    total_income_log = np.log(data['ApplicantIncome'] + data['CoapplicantIncome'] + 1)
    applicant_income_log = np.log(data['ApplicantIncome'] + 1)
    loan_amount_log = np.log(data['LoanAmount'] + 1)
    loan_amount_term_log = np.log(data['Loan_Amount_Term'] + 1)

    # Map categorical variables
    gender = int(data['Gender'])  # Assuming already encoded (e.g., 0 for Male, 1 for Female)
    married = int(data['Married'])  # Assuming already encoded (e.g., 0 for No, 1 for Yes)
    dependents = int(data['Dependents'])  # Assuming already encoded
    education = int(data['Education'])  # Assuming already encoded (e.g., 0 for Not Graduate, 1 for Graduate)
    self_employed = int(data['Self_Employed'])  # Assuming already encoded (e.g., 0 for No, 1 for Yes)
    credit_history = data['Credit_History']  # Numeric already
    property_area = 0 if data['Property_Area'] == 'Urban' else (1 if data['Property_Area'] == 'Semiurban' else 2)

    # Create standardized input list
    standardized_data = [
        gender,
        married,
        dependents,
        education,
        self_employed,
        credit_history,
        property_area,
        total_income_log,
        applicant_income_log,
        loan_amount_log,
        loan_amount_term_log,
    ]

    return [standardized_data]


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        # Parse JSON request
        data = request.json['data']
        # Preprocess the data
        preprocessed_data = preprocess_data(data)
        # Predict using the model
        predicted_label = RandomForestModel.predict(preprocessed_data)[0]
        # Return the result
        result = "Approved" if predicted_label == 1 else "Not Approved"
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})

# @app.route('/predict_api', methods=['POST'])
# def predict_api():
#     data=request.json['data']
#     print(data)
#     print(np.array(list(data.values())).reshape(1,-1))
#     new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
#     output=regmodel.predict(new_data)
#     print(output[0])
#     return jsonify(output[0])



if __name__ == '__main__':
    app.run(debug=True)
