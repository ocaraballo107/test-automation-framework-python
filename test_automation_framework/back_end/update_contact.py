import requests
import json

# {{url}}/contacts/{{contactId}}
url = "https://thinking-tester-contact-list.herokuapp.com/contacts/{{contactId}}"

payload = json.dumps({
    "_id": "64d12cecdbc72b0013a8ab41",
    "firstName": "Peter",
    "lastName": "Pan",
    "birthdate": "1977-07-07",
    "email": "ppan@fake.com",
    "phone": "8005551000",
    "street1": "123 Main St.",
    "street2": "Apartment Q",
    "city": "New York",
    "stateProvince": "NY",
    "postalCode": "12345",
    "country": "USA",
    "owner": "64d11f484f35f3001303ca3c",
    "__v": 0
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer UserCredentials',
    'Cookie': 'token=UserCredentials'
}

response = requests.request("PUT", url, headers=headers, data=payload)
print(response.text)
