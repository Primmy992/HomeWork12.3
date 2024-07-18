import json


def geography_quiz(countries_cities):
    correct = 0
    wrong = 0

    for country, city in countries_cities.items():
        answer = input(f"What is the capital of {country}: ")
        if answer != city:
            print("Wrong!")
            wrong += 1
        else:
            print("Correct!")
            correct += 1

    return correct, wrong


