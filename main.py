import json
import datetime

from functions import geography_quiz

countries_cities = {
    "Albania": "Tirana",
    "Andorra": "Andorra la Vella",
    "Armenia": "Yerevan",
    "Austria": "Vienna",
    "Azerbaijan": "Baku",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "Bosnia and Herzegovina": "Sarajevo",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Georgia": "Tbilisi",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Kazakhstan": "Nur-Sultan",
    "Kosovo": "Pristina",
    "Latvia": "Riga",
    "Liechtenstein": "Vaduz",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg",
    "Malta": "Valletta",
    "Moldova": "Chisinau",
    "Monaco": "Monaco",
    "Montenegro": "Podgorica",
    "Netherlands": "Amsterdam",
    "North Macedonia": "Skopje",
    "Norway": "Oslo",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Russia": "Moscow",
    "San Marino": "San Marino",
    "Serbia": "Belgrade",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Turkey": "Ankara",
    "Ukraine": "Kyiv",
    "United Kingdom": "London",
    "Vatican City": "Vatican City"
}

fileName = "results.json"

with open(fileName, "r") as gameFile:
    gameList = json.loads(gameFile.read())

name = input("Enter your name: ")

correct, wrong = geography_quiz(countries_cities)

print(f"Number of correct answers: {correct}\nNumber of wrong answers: {wrong}")
gameData = {
    "name": name,
    "correct": correct,
    "wrong": wrong,
    "date": str(datetime.datetime.now())
}

gameList.append(gameData)

with open("results.json", "w") as gameFile:
    gameFile.write(json.dumps(gameList))
