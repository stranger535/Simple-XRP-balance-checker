from xrpl.clients import JsonRpcClient
from xrpl.models.requests.account_info import AccountInfo
import json



check_account = str(input("Input your wallet to get Balance:"))


# RPC of main net
JSON_RPC_URL = "https://s1.ripple.com:51234/"

client = JsonRpcClient(JSON_RPC_URL)


# Info about your account
acct_info = AccountInfo(
    account=check_account,
    ledger_index="validated",
    strict=True,
)
response = client.request(acct_info)
result = response.result
#print("response.status: ", response.status)


bal1 = response.result["account_data"]["Balance"]
bal = int(bal1)
bal2 = bal / 1000000


print(f"Balance XRP: {bal2}")