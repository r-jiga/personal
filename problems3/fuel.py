def main():
    percentage = round(fraction_calculator()*100)
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    elif 1 < percentage < 99:
        print(f"{percentage}%")


def fraction_calculator():
    while True:
        try:
            prompt = input("Fraction: ")
            x, y = prompt.split("/")
            x = int(x)
            y = int(y)
            if x <= y:
                return x / y
        except(ValueError, ZeroDivisionError):
            pass


main()