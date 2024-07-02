import requests
import key
import response
import datetime as dt

date_now = dt.datetime.now()
date = date_now.date()
time = date_now.time()

# Nutritionix
headers = {
    "x-app-id": key.NU_APPL_ID,
    "x-app-key": key.NU_APPKEY
}
params = {
    "query": "I walked 2.4 km",
    "weight_kg": 80,
    "height_cm": 170,
    "age": 66
}
# url = key.HOST_DOMAIN + key.EXERCISE_COMPL

# response_online = requests.post(url=f"{url}",
#                          json=params, headers=headers)
# response_online.raise_for_status()
# data = response_online.json()
# print(data)
#

response_data = response.resp
list_exercises = [item for item in response.resp["exercises"]]
print(list_exercises)
print(list_exercises[0]["nf_calories"])

url = key.SH_ENDPOINT
print(url)

headers_sh = {
    "Authorization": key.SH_BASIC_AUTH,
}


# Date	Time	Exercise	Duration	Calories
params_sh = {
    "workout": {
        "date": str(date),
        "time": str(time),
        "exercise": list_exercises[0]["name"],
        "duration": list_exercises[0]["duration_min"],
        "calories": list_exercises[0]["nf_calories"],
    }
}
response_online = requests.post(url=f"{url}",
                                json=params_sh)
response_online.raise_for_status()
data = response_online.json()
print(data)
