# Test Automation Framework with Page Object Model, PyTest, and Requests

This is a test automation framework that combines frontend testing using Selenium WebDriver and backend API testing using the `requests` library. The framework automates tests for the "https://www.dish.com" website and interacts with a sample RESTful API for CRUD operations on contacts.

## Project Structure

test_automation_framework/
│
├── tests/
│ ├── init.py
│ ├── test_homepage.py
│ ├── test_backend.py
│
├── pages/
│ ├── init.py
│ ├── homepage.py
│
├── conftest.py
├── pytest.ini
└── README.md

## Requirements

- Python 3.x
- PyTest
- Selenium
- Requests

## Install the required dependencies using the following command

bash
pip install pytest selenium requests

## Front End Testing

- Define page objects under the pages directory using the Page Object Model.
- Write frontend test cases in the tests directory using PyTest syntax.

## Running Frontend Tests

Run the frontend tests using the following command: pytest

## Running Backend Testing

Run the backend tests using the following command: pytest

## Example Backend Test Case

Here's an example of a backend test case using the requests library to interact with a sample API:

tests/test_backend.py:

import requests

def test_get_contact():
    url = "https://thinking-tester-contact-list.herokuapp.com/contacts/{{contactId}}"
    headers = {
        'Authorization': 'Bearer UserCredentials',
        'Cookie': 'token=UserCredentials'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert "contact details" in response.text
    # Add more assertions or validations here

## Contribute

Contributions are welcome! If you find any issues or want to enhance the framework, feel free to submit a pull request.

## License

This project is licensed under the MIT License
