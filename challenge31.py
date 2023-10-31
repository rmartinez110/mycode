#! /usr/bin/python3
import random

def main():
    wordbank = ["indentation", "spaces"]
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
    
    wordbank.append(4)

    print(wordbank)
    print(tlgstudents)
    
    randomNum = random.randint(0, len(tlgstudents))

    print(tlgstudents[randomNum] + " always uses " + str(wordbank[2]) + " " + wordbank[1] + " to indent" )
main()
