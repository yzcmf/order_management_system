import requests,pprint

# payload = {
#     'username': 'zyx',
#     'password': '12345678'
#     # 'password': '9999999'
# }

# response = requests.post('http://localhost/api/mgr/signin',
#               data=payload)


payload = {
    'action': 'list_customer'
}

response = requests.get('http://localhost/api/mgr/customers',
              params=payload)

pprint.pprint(response.json())