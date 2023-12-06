expression = input("Expression: ")
x, y, z = expression.split()

z = int(z)
x = int(x)

if y == "+":
    result  = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
else:
    print("Sorry buddy, for now I can only use +, -, *, and /")

print("{:.1f}".format(result))