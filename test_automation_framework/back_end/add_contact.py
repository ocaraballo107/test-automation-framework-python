import requests
import json

# {{url}}/contacts
url = "https://thinking-tester-contact-list.herokuapp.com/contacts"

payload = json.dumps({
  "firstName": "Amy",
  "lastName": "Smith",
  "birthdate": "1977-07-07",
  "email": "pprunewhip@fake.com",
  "phone": "8005551000",
  "street1": "123 Main St.",
  "street2": "Apartment Q",
  "city": "New York",
  "stateProvince": "NY",
  "postalCode": "12345",
  "country": "USA"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer UserCredentials',
  'Cookie': 'token=UserCredentials'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
