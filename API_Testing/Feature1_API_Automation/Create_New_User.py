import jsonpath
import json
import requests

#API URL
url ="https://demo.sylius.com/api/v2/shop/customers"
headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
         }
#Input converted to json format
true: bool = True
data = json.dumps({
  'firstName': 'Hiba',
  'lastName': 'Shabbir',
  'email': 'hibashabbir@gmail.com',
  'password': '123123123',
  'subscribedToNewsletter' : true
})

#make post request with json input body
response= requests.post(url,data =data , headers = headers)

status_code =str(response.status_code)
print(response.text)
#validating response post
if(response.status_code == 204):
    print(status_code +" : Customer resource created")
elif(response.status_code ==400):
    print(status_code +" : Invalid input")
elif(response.status_code ==404 ):
    print(status_code+" : Resource not found")
elif(response.status_code == 422):
    print(status_code +" : Unprocessable entity")