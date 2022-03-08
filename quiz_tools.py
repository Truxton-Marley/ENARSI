import random
import time

from os import system

###################################
###      Multiple Choice        ###
###################################

def print_encouragement():
    encouragement = ["Great Job!", "Good Work!", "That's the answer :)", "Yeap.", "Bon Travail, mon ami!",
                    "That's the stuff, pal!", "Merde, vous etes trop fort, mon capitaine!!!", "Volltreffer!"]
    print("\n" + encouragement[random.randint(0, (len(encouragement) - 1))])

def clear_screen_slowly(wait=1):
    time.sleep(wait)
    system("cls")

def ask_question(question):
    #TODO: clean up clear screen; adjust for Linux
    if question.get("clear_screen"):
        clear_screen_slowly()
    print(question["question"], end="")

def get_answer(question):
    answer = ""
    #TODO: Alternative logic or implementation might be cleaner here.
    split_question = question["answer"].split("\n")
    for line in split_question:
        answer += input(question["prompt"])
        # Only add new line to answer if not the last line in answer
        if line != split_question[-1]:
            answer += "\n"
    return answer

def check_answer(answer, question):
    if answer == question["answer"]:
        if question.get("suppress_positive_affirmation"):
            return
        elif question.get("post_task_output"):
            print(question["post_task_output"])
            print_encouragement()
            wait = input("\nHit enter when you're ready for the next question.")
            return
        print_encouragement()
    elif answer == "hint":
        print(answer)
    else:
        print("Better luck next time.\nThe correct answer was:\n")
        for line in question["answer"].split("\n"):
            print(question["prompt"] + line)
        # Pause to give user time to view the correct answer
        wait = input("\nHit enter when you're ready for the next question.")
        ask_question(question)
        answer = get_answer(question)
        check_answer(answer, question)

def preview_answer(question):
    print("\n#################")
    print("###  answer:  ###", end="")
    print("\n#################")
    print(question["answer"], "\n")

def ask_questions(questions, training_mode=False):
    for question in questions:
        ask_question(question)
        if training_mode:
            preview_answer(question)
        answer = get_answer(question)
        check_answer(answer, question)

#####################################
###      Fill in the Blank        ###
#####################################

def get_text(file):
    text = ""
    with open(file, "r") as f:
        for line in f.readlines():
            text += line
    return text

def get_blanks(text):
    len_text = text.count( "\n" ) + 1
    number_of_blanks = len_text // 4
    blanks = [random.randint(0, len_text) for ran in range(0, number_of_blanks)]
    blanks = sorted(set(blanks))
    return blanks

def get_fib_question(file):
    text = get_text(file)
    blanks = get_blanks(text)
    for i, line in enumerate(text.split("\n")):
        if i not in blanks:
            print(line)
        elif line.strip().startswith("!"):
            continue
        else:
            solution = line.strip()
            response = input()
            while solution != response:
                print("Answer:", line)
                response = input()