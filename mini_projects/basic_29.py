# basic http request

import requests

class Joke:
    def __init__(self):
        self.url = "https://icanhazdadjoke.com/"
        self.headers = {"Accept": "application/json"}

    def getJoke(self):
        while True:
            res = requests.get(self.url, headers=self.headers)
            data = res.json()
            print(data["joke"])

            ask = input("Want to get another joke?").lower()
            if ask == "n":
                break


joke = Joke()

print(joke.getJoke())
