#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random
from colorist import Color
import os
import html


URL= "https://opentdb.com/api.php?amount=10&category=15&difficulty=easy"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    # data= requests.get(URL).json()

    # for question in data["results"]:
    #     print(f"#####################################################\nLEVEL 1\n#####################################################\n")
    #     print(f'Question: {question["question"]}')
    #     print(f'Answer: {question["correct_answer"]}')
    #     print(f'Wrong Answers: {question["incorrect_answers"]}')


    # print(f"#####################################################\nLEVEL 2\n#####################################################\n")
    # print(f"#####################################################\n#####################################################\n")

    # shuffledAnswers = random.shuffle(data["results"])

    # for question in data["results"]:
    #     print(f"#####################################################\n#####################################################\n")
    #     print(f'Question: {question["question"]}')
    #     print(f'Answer: {shuffledAnswers}')
    #     print(f'Wrong Answers: {question["incorrect_answers"]}')


    # print(f"#####################################################\nLEVEL 2\n#####################################################\n")
    # print(f"#####################################################\n#####################################################\n")

    categories = categories= {
        9:  "General Knowledge", 
        10: "Entertainment- Books", 
        11: "Entertainment- Film", 
        12: "Entertainment- Music", 
        13: "Entertainment- Musicals & Theater", 
        14: "Entertainment- Television", 
        15: "Entertainment- Video Games", 
        16: "Entertainment- Board Games", 
        17: "Science- Nature", 
        18: "Science- Computers", 
        19: "Science- Mathematics", 
        20: "Mythology", 
        21: "Sports", 
        22: "Geography", 
        23: "History", 
        24: "Politics", 
        25: "Art", 
        26: "Celebrities", 
        27: "Animals", 
        28: "Vehicles", 
        29: "Entertainment- Comics", 
        30: "Science- Gadgets", 
        31: "Entertainment- - Japanese Anime & Manga", 
        32: "Entertainment- - Cartoon Animations"
        }
    os.system("clear")
    print("\n")
    
    
    
    for key, value in categories.items():
        print(key, value)
    print("\n")
    questionCategory = f"{input('Pick a category by number [listed above]: ').lower()}"
    print("\n")
    questionCount = f"{input('How many questions do you want [1 - 10]? ').lower()}"
    print("\n")
    questionDifficulty = f"{input('What difficulty do you want [easy, medium, hard]? ').lower()}"
    print("\n")
    print(f"Select a type of question:\n1.) Any Type\n2.)Multiple Choice\n3.)True/False")
    questionType = f"{input('What type of question do you want? ').lower()}"

    if questionType == '1':
        questionType = ''
    elif questionType == '2':
        questionType = 'multiple'
    elif questionType == '3':
        questionType = 'boolean'


    userURL = f"https://opentdb.com/api.php?"

    apiInfo = {
        'amount': questionCount,
        'category': questionCategory,
        'difficulty': questionDifficulty,
        'type': questionType,
    }

    for key, value in apiInfo.items():
        if value == '':
            continue
        userURL += f"{key}={value}&"
    
    print(f"\n\n {userURL} \n\n")

    try:
        newResponse = requests.get(userURL).json()
        escapedResponse = html.unescape(newResponse)
        for question in escapedResponse["results"]:
            print(f"#####################################################\Question\n#####################################################\n")
            print(f'{Color.BLUE}Question:{Color.OFF} {question["question"]}')
            print(f'{Color.BLUE}Answer:{Color.OFF} {question["correct_answer"]}')
            print(f'{Color.BLUE}Wrong Answers:{Color.OFF} {question["incorrect_answers"]}')
    except:
        print("Something went wrong. Try again.")

if __name__ == "__main__":
    main()