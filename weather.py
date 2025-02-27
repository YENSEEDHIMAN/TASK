import requests
api_key="9533d8063ffe47daa1460625252702"
location="Ambala"
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
response=requests.get(url)
data=response.json()
if response.status_code==200:
    print("Location",data['location']['name'])
    print("Region",data['location']['region'])
    print("Country",data['location']['country'])
    print("Temperature (C):", data['current']['temp_c'])
    print("Condition:", data['current']['condition']['text'])
else:
    print("Failed to fetch data")


