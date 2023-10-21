# Import requests library
import requests

# Define the request URL
url = "https://s1.ripple.com:51234/"





def getXRPAccountInfo(account):
  # Define the request payload
  payload = {
      "method": "account_info",
      "params": [
          {
              "account": account,
              "ledger_index": "current",
              "queue": 1
          }
      ]
  }
  # Send the request and get the response
  response = requests.post(url, json=payload)
  # Print the response status code and content
  print(response.status_code)
  print(response.content)
  return str(response.content)


# getXRPAccountInfo("rG1QQv2nh2gr7RCZ1P8YYcBUKCCN633jCn")