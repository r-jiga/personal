def user_input():
    print((camel_to_snake(input("camelCase: "))))


def camel_to_snake(str):
    snaked = ""
    for i in range(len(str)):
        if str[i].isupper() and i != 0:
            snaked += "_"
        snaked += str[i]
    return snaked.lower()

user_input()
