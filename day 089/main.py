import requests
from bs4 import BeautifulSoup

response = requests.get("https://jsonplaceholder.typicode.com/users")
print(" response =",response.text)


PostUrl = "https://jsonplaceholder.typicode.com/posts"
headers = {
    'Content-type': 'application/json; charset=UTF-8',
}
body = {
    "userId": 1,
    "name":"Amit"
}

res = requests.post(PostUrl, headers=headers, json=body)
print("Post Response =",res.text)


response = requests.get("https://jsonplaceholder.typicode.com/guide/")
print(" response =",response.text)

soup = BeautifulSoup(response.text,"html.parser")
print(" BeautifulSoup ", soup)

for heading in soup.find_all("h3"):
    print("h3 =",heading.text)