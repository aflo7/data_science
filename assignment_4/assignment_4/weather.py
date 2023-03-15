import requests
from bs4 import BeautifulSoup

url = "https://weather.com/weather/today/l/f06848d98b2de6e4c8e057e63fa6ba308ead9c397626e2dbab996d0c687bf5a6"
# city: Bowling Green, KY

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")
section1 = soup.find("section", {'class': "card"})  # get the section containing the weather today in Bowling Green, KY

# temperature
print("Current temp:", section1.find('span', {'data-testid': "TemperatureValue"}).text)

section2 = soup.find("div", {"class": "TodayDetailsCard--detailsContainer--2yLtL"})
print("Wind Speed:", section2.find("span", {'data-testid': "Wind"}).text[14:])
print("Humidity:", section2.find("div", {"class": "WeatherDetailsListItem--wxData--kK35q"}).find_all("span")[1].text)
print("UV Index:", section2.find_all("div", {"data-testid": "WeatherDetailsListItem"})[5].find('span', {'data-testid':"UVIndexValue"}).text)