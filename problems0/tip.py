def dollars_to_float(d):
    # return float(d.strip("$"))
    return float(d[1:])

def percent_to_float(p):
    # return float(p.strip("%"))
    return float(p[:-1])/100



dollars = dollars_to_float(input("How much was the meal? "))
percent = percent_to_float(input("How much do you want to tip? "))
tip = dollars * percent
print(f"Leave ${tip:.2f}")
