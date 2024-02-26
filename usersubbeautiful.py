from bs4 import BeautifulSoup;
import requests

response = requests.get("https://www.codechef.com/users/mithun3")

content = BeautifulSoup(response.text, 'html.parser')
practice = content.find("section", class_="rating-data-section problems-solved")

h3 = practice.find("h3").text
openbrac = h3.index("(")
closebrac = h3.index(")")

count = h3[openbrac + 1:closebrac]
count = int(count)
if count > 0:
    span = practice.find("span")
    solvedprblm = span.findAll("a")
    for i in solvedprblm:
        print("-----------------------------------")
        prblm = (i['href'])
        index = str(i['href']).rfind("/")
        prblm = prblm[index + 1:]
        print(prblm)
