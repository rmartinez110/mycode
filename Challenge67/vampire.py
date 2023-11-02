#! /usr/bin/env python3
import csv

def main():
    with open("dracula.txt", "r") as csv_file:
        lineCount = 0
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            for word in row:
                if "vampire" in word.lower():
                    print(row)
                    lineCount += 1
                    break
        print(f"Total lines with vampire: {lineCount}")
    csv_file.close()
    print("Done")
    return 0

if __name__ == "__main__":
    main()
