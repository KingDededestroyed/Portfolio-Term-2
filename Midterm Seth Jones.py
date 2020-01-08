#Midterm Exam 2019
#Seth Jones -- 12/02/2019

import sys

from time import sleep

divideLines = "-----------------------------------------------"

def open_file(file_name,mode):
    """Opens file in the given mode"""
    try:
        the_file = open(file_name,mode)
        return the_file
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\nPress the enter key to exit.")
        sys.exit()

def next_line(the_file):
    line = the_file.readline()
    line = line.strip("\n")
    line = line.replace("/","\n")
    return line

def question_block(the_file):
    """Read the question block from the file and return category,
question, answers,correct answers, and explanation."""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation

def welcome(title):
    print("\t\tGreetings. The test is ready. But are you?\n")
    print(str.format("\t\tThis test was created by {}.\n",title))

def main(file_name):
    the_file = open_file(file_name,"r")
    title = next_line(the_file)
    name = input("Please enter your name: ")
    questions = 0
    score = 0
    category,question,answers,correct,explanation = question_block(the_file)
    print(category)
    welcome(title)
    while category:
        print(category)
        print()
        print(question)
        print()
        for i in range(len(answers)):
            print(answers[i])
        userAnswer = input("\nEnter your answer(1, 2, 3, or 4): ")

        if userAnswer == correct:
            score += 1
            questions += 1
            print("Absolute madlad.")
        else:
            questions += 1
            print("\nYou absolute buffoon.")
        print()
        print(explanation)
        category,question,answers,correct,explanation = question_block(the_file)
        print(divideLines)
        
    the_file.close()
    print("You have completed the test. Now relax.\n")
    report_card(name,score,questions)
    write_score(name,score)

def buffoon():
    while True:
            file_name = input("Please enter your test file name: ")
            if (".txt" in file_name) and (" " not in file_name):
                return file_name
            else:
                print("\nYou absolute buffoon.")

def write_score(name,score):
    the_file = open_file("scores.txt","a+")
    pair = name + ":   " + str(score) + "\n"
    line = []
    line.append(pair)
    the_file.writelines(line)
    the_file.close()

def report_card(name,score,questions):
    print(str.format("\nYou got {0} correct out of {1} questions.",score,questions))
    percent = score/questions * 100
    print(str.format("{}%",percent))
    if percent <= 100 and percent >= 90:
        print("Grade: A")
    elif percent <= 89 and percent >= 80:
        print("Grade: B")
    elif percent <= 79 and percent >= 70:
        print("Grade: C")
    elif percent <= 69 and percent >= 60:
        print("Grade: D")
    elif percent <= 50:
        print("Grade: F")
    
file_name = buffoon()
main(file_name)

