answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

if answer == "42":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "forty two":
    print("Yes")
else:
    print("No")