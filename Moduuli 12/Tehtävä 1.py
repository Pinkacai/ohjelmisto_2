import requests
import json

answ = input("Do you want to hear a Chuck Norris joke? Y/N: ").capitalize()
while answ == "Y":
    print("Here you go! ")
    request = "https://api.chucknorris.io/jokes/random"
    response = requests.get(request).json()

    print("")
    print(response["value"])
    answ = input("Do you want to hear another Chuck Norris joke? Y/N: ").capitalize()
else:
    print("Never mind then.. BYE!")
    quit()


