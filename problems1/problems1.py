def great_question():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()

    if answer == "42":
        print("Yes")
    elif answer == "forty two":
        print("Yes")
    elif answer == "forty-two":
        print("Yes")
    else:
        print("No")

while True:
    great_question()

    continue_program = input("Do you want to give another answer? (yes/no) ").lower().strip()
    if continue_program != "yes":
        break