i = 0
while i < 3:
    print("meow")
    i += 1

for i in [0, 1, 2]:
    print("meow")

for i in range(3): #starts from 0 and goes < 3
    print("meow")

for _ in [0, 1, 2]: # we use _ in python if we do not use the variable anywhere else(this is called being PYTHONIC)
    print("meow")

print("meow\n" * 3, end="")

while True:
    n = int(input("What's n?"))
    if n > 0:
        break

for _ in range(n):
    print("meow")

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            return n #return the result


def meow(n):
    for _ in range(n):
        print("meow")

main()


