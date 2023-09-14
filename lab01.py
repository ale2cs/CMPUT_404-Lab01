import requests

# print(requests.__version__)

resp = requests.get("https://raw.githubusercontent.com/ale2cs/CMPUT_404-Lab01/main/lab01.py")

print(resp.text)
