import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Bowling_Green_State_University"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")
img_tags = soup.find_all("img")

img_links = [img["src"] for img in img_tags]

for i, img_link in enumerate(img_links):
    print(
        f"{i + 1}: https://en.wikipedia.org/wiki/Bowling_Green_State_University{img_link}"
    )
    print()

print("There are", len(img_links), "image links on the page.")
