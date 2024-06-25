import requests

URL = "http://127.0.0.1:8000/krishimitra/endpoint1/"

data = {
    "name": "rice",
    "season": "kharif",
    "state": "Andhra Pradesh",
    "annual_rainfall": 1000,
    "fertilizer_usage": 100,
    "pesticide_usage":100,
}

response = requests.post(URL, data=data)
print(response.json())
