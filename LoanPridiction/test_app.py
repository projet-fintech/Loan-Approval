import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client



#def test_predict_api_not_approved(client):
#   test_data = {
#       "data": {
#          "person_age": 50,
#          "person_gender": "Female",
#         "person_education": "High School",
#           "person_income": 30000,
#        "person_emp_exp": 1,
#        "person_home_ownership": "MORTGAGE",
#        "loan_amnt": 20000,
#        "loan_intent": "MEDICAL",
#        "loan_int_rate": 15.0,
#       "loan_percent_income": 0.5,
#        "cb_person_cred_hist_length": 2,
#        "credit_score": 600,
#       "previous_loan_defaults_on_file": 1
#    }
#}
# response = client.post('/predict_api', json=test_data)
# assert response.status_code == 200
# assert b"Not Approved" in response.data

def test_predict_api_invalid_input(client):
    test_data = {
        "data": {
            "invalid_feature": 0.1  # Données invalides pour tester la gestion des erreurs
        }
    }
    response = client.post('/predict_api', json=test_data)
    assert response.status_code == 200
    assert b"error" in response.data