import requests

# {{url}}/contacts/{{contactId}}
url = "https://thinking-tester-contact-list.herokuapp.com/contacts/{{contactId}}"

payload = {}
headers = {
    'Authorization': 'Bearer UserCredentials',
    'Cookie': 'token=UserCredentials'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)
