import requests


parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,

}

quiz_response = requests.get(url="https://opentdb.com/api.php", params=parameters)
quiz_response.raise_for_status()
quiz_data = quiz_response.json()
question_data = quiz_data["results"]
