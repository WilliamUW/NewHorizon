# Import requests library
import requests

# Define the request URL
url = "https://s1.ripple.com:51234/"


def getXRPAccountInfo(account):
    # Define the request payload
    payload = {
        "method": "account_info",
        "params": [{"account": account, "ledger_index": "current", "queue": 1}],
    }
    # Send the request and get the response
    response = requests.post(url, json=payload)
    # Print the response status code and content
    print(response.status_code)
    print(response.content)
    return str(response.content)


# getXRPAccountInfo("rG1QQv2nh2gr7RCZ1P8YYcBUKCCN633jCn")


def makeXRPTransaction(sender, receiver, amount, secret):
    # Define the request payload for making an XRP transaction
    payload = {
        "method": "submit",
        "params": [
            {
                "tx_json": {
                    "TransactionType": "Payment",
                    "Account": sender,
                    "Destination": receiver,
                    "Amount": amount,
                },
                "secret": secret,
            }
        ],
    }
    # Send the request and get the response
    response = requests.post(url, json=payload)
    # Print the response status code and content
    print(response.status_code)
    print(response.content)
    return str(response.content)


def sendXRPMessage(sender, receiver, amount, secret, memos=None):
    # Define the request payload for making an XRP transaction with optional memos
    payload = {
        "method": "submit",
        "params": [
            {
                "tx_json": {
                    "TransactionType": "Payment",
                    "Account": sender,
                    "Destination": receiver,
                    "Amount": amount,
                    "Memos": [{"Memo": {"MemoData": memo}} for memo in memos]
                    if memos
                    else [],
                },
                "secret": secret,
            }
        ],
    }
    # Send the request and get the response
    response = requests.post(url, json=payload)
    # Print the response status code and content
    print(response.status_code)
    print(response.content)
    return str(response.content)
