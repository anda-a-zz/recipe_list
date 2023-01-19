import sys
from urllib.request import Request, urlopen
import json
import html_to_json
import requests
from bs4 import BeautifulSoup

#pip3 install beautifulsoup4

url_link2 = "https://www.inspiredtaste.net/24412/cocoa-brownies-recipe/"
url_link = "https://www.thewholesomedish.com/the-best-classic-chili/"

# response = urllib.request.urlopen(url)
# data = json.loads(response.read())
# print(data)

req = Request(url_link, headers={'User-Agent': 'Mozilla/5.0'})
s = urlopen(req).read()

# url = urllib.request.urlopen(url_link)
# s = url.read()

soup = BeautifulSoup(s)
html_code = soup.prettify()
print(html_code)

json_var = html_to_json.convert(html_code)
with open("output.json", "w") as file:
    json.dump(json_var, file)


# searchfile = open("file.txt", "r")
# for line in searchfile:
#     if "searchphrase" in line: print line
# searchfile.close()