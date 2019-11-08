import requests
import os

def save(number, text):
    f = open("tvibo_streams/{0}.txt".format(number), "x")
    f.write(text)
    f.close()

for i in range(1017289, 10000000):
    response = requests.get("http://api.tvibo.com/api/player/streamurl/{0}".format(i))
    if not "error" in response.text:
        save(i, response.text)
