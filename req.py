#!usr/bin/python3

import requests
import webbrowser

session = requests.session()
url="https://thedummysite.com/login"
#username=zero&password=12345

data= {"username":"testuser",
       "password":"Test1234!"}

session.post(url,data=data)

r= session.get("https://thedummysite.com")
file=open("file.html",'wb')
file.write(r.content)
file.close()

webbrowser.open("file.html")