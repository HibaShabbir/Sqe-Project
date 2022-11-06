import jsonpath
import json
import requests

#API URLs
AdminTokenUrl ="https://master.demo.sylius.com/api/v2/admin/authentication-token"
UserTokenUrl ="https://master.demo.sylius.com/api/v2/shop/authentication-token"
cartUrl = "https://master.demo.sylius.com/api/v2/shop/orders"
prodVariantsUrl ="https://master.demo.sylius.com/api/v2/shop/product-variants?page=1&itemsPerPage=30"
addToCartUrl = "https://master.demo.sylius.com/api/v2/shop/orders/rl1KwtiSLA/items"

#generally used header
headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
         }
#data input passed to api get admin token
AdminData = json.dumps({
  'email': 'api@example.com',
  'password': 'sylius-api'
})

#data input passed to api get user token
UserData = json.dumps({
  'email': 'shop@example.com',
  'password': 'sylius'
})

#data input passed to api get cart token
CartData = json.dumps({
})

#requests.post() api get admin token parses it to json format and picks up token
response= requests.post(AdminTokenUrl, data = AdminData , headers=headers)
response_json =json.loads(response.text)
adminToken = jsonpath.jsonpath(response_json,'token')
# print(adminToken[0])
# status_code =str(response.status_code)

#requests.post() api get user token parses it to json format and picks up token
response= requests.post(UserTokenUrl, data = UserData , headers=headers)
response_json =json.loads(response.text)
userToken = jsonpath.jsonpath(response_json,'token')

#header updated with authorization of user token as it will be used later on ...
headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': "Bearer {}".format(userToken[0])
           }
# print(headers)

#requests.post() api to get cart token value. Parses it to json format and picks up token value
response = requests.post(cartUrl,data=CartData, headers=headers)
response_json =json.loads(response.text)
tokenValue= jsonpath.jsonpath(response_json,'tokenValue')
# print(tokenValue)

#requests.get() api to get a product variant so as to add it to cart . Parses it to json format and picks up  code
response = requests.get(prodVariantsUrl, headers= headers )
response_json =json.loads(response.text)
prodId = jsonpath.jsonpath(response_json[0],'code')

#form complete prod id
productId="/api/v2/shop/product-variants/"+prodId[0]

#add to cart api input data
addToCartData =json.dumps({
  'productVariant': productId ,
  "quantity": 1

})

#form a Url for add to cart the item . Token Value is the value taken from create cart api
addToCartUrl = "https://master.demo.sylius.com/api/v2/shop/orders/"+tokenValue[0]+"/items"

#requests.post() api finally add to cart
response = requests.post(addToCartUrl,data = addToCartData, headers= headers )
status_code =str(response.status_code)

#validating response post
if(response.status_code == 201):
    print(status_code +" : Order resource created")
elif(response.status_code ==400):
    print(status_code +" : Invalid input")
elif(response.status_code ==404 ):
    print(status_code+" : Resource not found")
elif(response.status_code == 422):
    print(status_code +" : Unprocessable entity")

