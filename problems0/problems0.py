#INDOOR FUNCTION
def indoor():
    text = str(input("write something using at least one upper char, see what happens "))
    print(text.lower())
    # indooring(text)

# def indooring(a):
#     print(a.lower())


#PLAYBACK FUNCTION
def playback():
    text = str(input("write something, I'll slow it down: "))
    print(spaceto3dots(text))

def spaceto3dots(x):
    return(x.replace(" ", "..."))


#EMOTICONS TO EMOJIS FUNCTION
def emoticons():
    user_input = str(input('Try to write something using ":)" or ":(", see what happens: '))
    print(convert(user_input))

def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x


#EINSTEIN FUNCTION
def einstein():
   m = int(input("Introduce the mass in Kgs: "))
   E = relativity(m)
   print(f"The value of E is : {E}")

def relativity(m):
  c = 300000000
  E = m*c**2
  return E


#TIP CALCULATOR FUNCTION
def tip():
    dollars = dollars_to_float(input("How much was the bill? "))
    percent = percent_to_float(input("How much do you want to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}") #formats the tip to a fixed point of 2 decimals

# def dollars_to_float(d):  #returns the string starting from the first element(which is not included)
#     return float (d[1:])

def dollars_to_float(d): #returns the string removing any $ sign leading or trailing the string
    return float (d.strip("$"))

# def percent_to_float(p): # returns the string (as a float) up until the last element(which is not included)
#     return float(p[:-1])/100

def percent_to_float(p): #returns the string (as a float) without any % sign leading or trailing the string
    return float(p.strip("%"))/100

#yes indeed
if __name__ == "__main__":
    indoor()
    playback()
    emoticons()
    einstein()
    tip()

#test commit
