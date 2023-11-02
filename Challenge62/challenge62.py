#! /usr/bin/env python3

def main():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    userInput = input("Which farm do you want to pull?\n>")

    for farm in farms:
        if farm["name"] == userInput:
            for i in farm["agriculture"]:
                if i != "carrots" and i != "celery":
                    print(i)
            break

if __name__ == "__main__":
    main()
