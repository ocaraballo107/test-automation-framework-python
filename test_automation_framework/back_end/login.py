import requests
import json

# {{url}}/users/login
url = "https://thinking-tester-contact-list.herokuapp.com/users/login"

payload = json.dumps({
    "email": "user@email.com",
    "password": "UserPassword123"
})
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'token=UserCredentials'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
