from pip._vendor import requests 

response = requests.get("https://goweather.herokuapp.com/weather/accra")
print(response.status_code)
data_json = response.json()
print("The temperature for tomorrow is: " ,data_json['forecast'][0]['temperature'])
#print("The temperature right now is: ", data_json["temperature"])