import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')
rows = soup.find_all('tr') # get each row containing movie data

for row in rows:
  movieName = ""
  releaseYear = None
  rating = ""
  
  titleTd = row.select_one('.titleColumn')
  if titleTd:
    movieName = titleTd.find("a").text
    releaseYear = titleTd.find("span", {'class': "secondaryInfo"}).text.replace("(", "").replace(")", "")
  ratingTd = row.select_one('.ratingColumn.imdbRating')
  if ratingTd:
    strongTag = ratingTd.find('strong')
    rating = strongTag.text
  
  # if we successfully scraped all data...
  if movieName and releaseYear and rating:
    if int(releaseYear) >= 1990 and int(releaseYear) <= 1999 and float(rating) > 8.5:
      print(movieName, rating)  