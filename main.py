import requests
import key
import response

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
url = key.HOST_DOMAIN+key.EXERCISE_COMPL
print(url)
# response_online = requests.post(url=f"{url}",
#                          json=params, headers=headers)
# response_online.raise_for_status()
# data = response_online.json()
# print(data)
response_data = response.resp
list_exercises = [item for item in response.resp["exercises"]]
print(list_exercises)
print(list_exercises[0]["nf_calories"])
