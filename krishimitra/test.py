import requests

URL = "http://127.0.0.1:8000/krishimitra/yieldpred/"

data = {
    "username": "testuser",
    "name": "Rice",
    "season": "Kharif",
    "state": "Andhra Pradesh",
    "area": 1000,
    "annual_rainfall": 1000,
    "fertilizer_usage": 100,
    "pesticide_usage":100,
}

response = requests.post(URL, data=data)
print(response.json())
