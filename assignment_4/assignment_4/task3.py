import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/coronavirus/"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")
tbody = soup.find("tbody")  # get each row containing movie data
tr = tbody.find_all("tr")  # get all of the table rows within the table body


colIndexes = {
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
}

countries = [] # this will be the index of the dataframe


for r in tr:
    countryName = r.find("a")
    
    if countryName:
      countries.append(countryName.text)
    else:
      countryName = r.find('span')
      if countryName:
        countries.append(countryName)
      
# print(len(countries))

for i in range(8, len(tr)):
    data = tr[i].find_all("td")
    
    # loop through the column data for each country
    for i in range(2, 15):
        colIndexes[i].append(data[i].text)
# print(len(colIndexes[2]))      

# totalCases = colIndexes[2]
# newCases = colIndexes[3]
# totalDeaths = colIndexes[4]
# newDeaths = colIndexes[5]
# totalRecovered = colIndexes[6]
# newRecovered = colIndexes[7]
# activeCases = colIndexes[8]
# seriousCritical = colIndexes[9]
# totCasesPerMillion = colIndexes[10]
# totDeathsPerMillion = []
# totalTests = []
# testsPerMillion = []
# population = []

dfData = {
  'totalCases': colIndexes[2],
'newCases': colIndexes[3],
'totalDeaths': colIndexes[4],
'newDeaths': colIndexes[5],
'totalRecovered': colIndexes[6],
'newRecovered': colIndexes[7],
'activeCases' : colIndexes[8],
'seriousCritical': colIndexes[9],
'totCasesPerMillion': colIndexes[10],
'totDeathsPerMillion': colIndexes[11],
'totalTests': colIndexes[12],
'testsPerMillion': colIndexes[13],
'population': colIndexes[14]
}
df = pd.DataFrame(dfData, countries)
print(df)

# print(countries)