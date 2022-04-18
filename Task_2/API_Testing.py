import requests
import json

####### CREATE PET API ############

def Create_req(FQDN,ID,name):

    url = "https://"+FQDN+"/api/v3/pet"

    myDict={
      "id": 10,
      "name": "doggy",
      "category": {
        "id": 1,
        "name": "Dogs"
      },
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }

    myDict.update({'id':ID})
    myDict.update({'name':name})

    payload = json.dumps(myDict)
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    if ID and name in (response.text):
        print("Test Case Passed")
    else:
        print("Test Case Failed")

####### UPDATE PET API ############

def Update_req(FQDN,ID,name):

    url = "https://"+FQDN+"/api/v3/pet"

    myDict={
      "id": 10,
      "name": "doggy",
      "category": {
        "id": 1,
        "name": "Dogs"
      },
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }

    myDict.update({'id':ID})
    myDict.update({'name':name})

    payload = json.dumps(myDict)
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)

    if ID and name in (response.text):
        print("Test Case Passed")
    else:
        print("Test Case Failed")

#################### DELETE PET ##################
    
def Delete_req(FQDN,ID):
    url = "https://"+FQDN+"/api/v3/pet/"+str(ID)
    payload={}
    headers = {}
    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)

    if "Pet deleted" in (response.text):
        print("Test Case Passed")
    else:
        print("Test Case Failed")

Create_req("petstore3.swagger.io",20,"Cats")
Update_req("petstore3.swagger.io",20,"Rat")
Delete_req("petstore3.swagger.io",20)
    

