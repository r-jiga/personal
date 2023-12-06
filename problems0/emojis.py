def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x

text = str(input('Try to write something using ":)" or ":(", see what happens: '))
print(convert(text))