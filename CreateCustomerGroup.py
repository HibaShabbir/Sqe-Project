import jsonpath
import requests
import json

# API URL
url = "https://master.demo.sylius.com/api/v2/admin/customer-groups"

headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Authorization' : 'Bearer TOKEN'
}

#Input converted to json format
data = json.dumps({
  "id" : 0,
  "code": "abc",
  "name": "esha"
})



#make post request with json input body
response = requests.post(url, data=data, headers=headers)

status_code = str(response.status_code)
print(response.text)

# validating response post
if(response.status_code == 201):
    print(status_code + " : Customer group resource created")
elif(response.status_code ==400):
    print(status_code + " : Invalid input")
elif(response.status_code ==404 ):
    print(status_code+ " : Resource not found")
elif(response.status_code == 422):
    print(status_code + " : Unprocessable entity")

