# Loan Approval Prediction

This repository contains a Flask-based web application 
for predicting loan approval decisions. The application 
uses a trained machine learning model to classify whether a 
loan application will be approved or not, based 
on user-provided inputs. The model was trained using the [Loan Approval Dataset](https://www.kaggle.com/datasets/zeyadmohamadezzat/loan-approval-dataset)

## Dataset Overview

The dataset consists of 45,000 samples and 14 attributes. 
Below is a brief description of the attributes:

- `person_age`: Age of the applicant.

- `person_gender`: Gender of the applicant (e.g., male, female).

- `person_education`: Education level of the applicant (e.g., high school, bachelor's, master's).

- `person_income`: Annual income of the applicant.

- `person_emp_exp`: Employment experience of the applicant (in years).

- `person_home_ownership`: Homeownership status (e.g., own, rent).

- `loan_amnt`: Requested loan amount.

- `loan_intent`: Purpose of the loan (e.g., education, medical, home improvement).

- `loan_int_rate`: Interest rate of the loan.

- `loan_percent_income`: Percentage of income allocated to the loan.

- `cb_person_cred_hist_length`: Length of credit history (in years).

- `credit_score`: Credit score of the applicant.

- `previous_loan_defaults_on_file`: did the user have already a previous loan ( Yes or Not )  .

- `loan_status`: Target variable indicating whether the loan was approved (1) or not (0).

![LoanData](https://github.com/user-attachments/assets/04b5b3fb-d4db-4ed6-b69b-9ce18eb82099)


---

## Project Structure

# 📁 LoanPrediction
```
├── 📂.venv
├── 📂 template
├── 📄 app.py
├── 📄 loan_data_Finale.csv
├── 📄 Loan_Prediction_Finale_Model.pkl 
├── 📄 Finale_Loan_Approval.ipynb
├── 📄 requirements.txt
└── 📄 FinaleScaler.pkl
```
---

## Installation and Setup

### Prerequisites
- Python 3.8 or later
- Pip for managing dependencies
- Virtual environment (recommended)

### Steps

1. Clone this repository:
```bash
   git clone <repository-url>
   cd LoanPrediction
```
```bash   
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
```bash 
    pip install -r requirements.txt
```
```bash
    python app.py
```



## Data Processing 

<div style="text-align:center;">
  <img src="https://github.com/user-attachments/assets/a67e7846-b690-4664-9c9d-75f659b4ff16" alt="DataInfo" width="350" height="300" />
</div>

The dataset was already clean, so no additional preprocessing steps, 
such as handling missing values or encoding categorical variables, 
were required. However, 
the following steps were taken to prepare the data for training the prediction model :


### 1. Encoding Categorical Variables :

To prepare the dataset for training, categorical features were encoded as follows:

➡️ `previous_loan_defaults_on_file` : Yes ➔ 1 , No ➔ 0

➡️ `loan_intent` : EDUCATION ➔ 0 , MEDICAL ➔ 1 , VENTURE ➔ 2 , PERSONAL ➔ 3 , 

DEBT_CONSOLIDATION ➔ 4 , HOME_IMPROVEMENT ➔ 5

➡️ `person_home_ownership` : OTHER ➔ 3 , OWN ➔ 2 , MORTGAGE ➔ 1 , RENT ➔ 0 

➡️ `person_education` : Bachelor ➔ 0 , Associate ➔ 1 , High School ➔ 2 , Master ➔ 3
  
  Doctorate ➔ 4

➡️ `person_gender` : male ➔ 1 , female ➔  0

These transformations ensured that all categorical features were numerical, 
enabling the model to process them effectively

🚨 **Feature selection was not performed, as it did not significantly
improve the model's accuracy. All features were retained to maximize 
the model's access to the dataset's information .**

## Model Training and Evaluation

This project uses a Logistic Regression model to predict the approval 
status of loan applications. 
Below is an overview of the process and functionality:

### Data Preprocessing

- **Feature Scaling** : Input data was standardized using a scaler to ensure consistent scaling across features.

- **Categorical Encoding** : Non-numerical features such as property area were encoded for compatibility with the model.

- **Train-Test Split** : The dataset was divided into training and testing sets to evaluate model performance.


### Model Selection and Training

➡️ `Model Used`: Logistic Regression

➡️ `Training`: The model was trained on the processed training dataset (`X_train`, `y_train`) using labeled data to predict the target variable (loan approval status).

### Model Evaluation
## Model Evaluation

The trained Logistic Regression model was evaluated on the test dataset using the following metrics:

### Classification Report
The `classification_report` provides a detailed breakdown of the model's performance, including precision, recall, and F1-score for each class:

```plaintext
              precision    recall  f1-score   support

           0       0.92      0.94      0.93      6990
           1       0.77      0.73      0.75      2010

    accuracy                           0.89      9000
   macro avg       0.85      0.83      0.84      9000
weighted avg       0.89      0.89      0.89      9000
```
et aussi **Accuracy : 0.8911 (89.11%)**


# Flask API for Loan Prediction

This project includes a **Flask API** that serves the trained 
Logistic Regression model to predict loan approval status based on user input.

## API Overview

The API is built using Flask, a lightweight Python web framework. 
It provides endpoints for making predictions:

1. Loading the Model and Scaler

The trained Logistic Regression model (`Loan_Prediction_Finale_Model.pkl`) and the scaler (`FinaleScaler.pkl`) 
are loaded using the pickle module.

3. Prediction Endpoint (`/predict_api`)

**Method**: `POST`
**Input**: Accepts `JSON` data with the following format:

```json
{
    "data": {
        "person_age": 20.0,
        "person_gender": 0,
        "person_education": 2,
        "person_income": 55000000.0,
        "person_emp_exp": 5,
        "person_home_ownership": 1,
        "loan_amnt": 200000.0,
        "loan_intent": 2,
        "loan_int_rate": 12.5,
        "loan_percent_income": 0.35,
        "cb_person_cred_hist_length": 4,
        "credit_score": 650,
        "previous_loan_defaults_on_file": 0
    }
}
```

## Process:
Parses the input `JSON` data.
Converts the data into a `Pandas DataFrame` for compatibility with the model.
Preprocesses the data using the `scaler`.

Makes a prediction using the `trained model`.

`Output`: Returns a JSON response with:

`prediction`: `Approved` or `Not Approved`


  
## Example Usage
### Request : 
![RequestData](https://github.com/user-attachments/assets/f56c27f5-6dee-4d24-b10b-1815984e4acc)

### Responce : 

![ResponseData](https://github.com/user-attachments/assets/3989ead5-91d1-41a8-a48b-4d47ef3c7c52)
