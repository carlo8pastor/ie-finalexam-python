from iebank_api import app
from iebank_api.models import Account
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€'})
    assert response.status_code == 200

def test_update_account(testing_client):
    """
    GIVEN a Flask application and an existing Account
    WHEN a PUT request is made to '/accounts/<id>' with a new name
    THEN check that the response contains the updated name
    """
    # Create an account for testing
    account = Account('John Doe', '€')
    testing_client.post('/accounts', json={'name': account.name, 'currency': account.currency})

    # Update the account's name
    new_name = 'Jane Smith'
    response = testing_client.put(f'/accounts/{account.id}', json={'name': new_name})

    # Retrieve the updated account from the response
    updated_account = response.json['account']

    # Check that the response contains the updated name
    assert response.status_code == 200
    assert updated_account['name'] == new_name
