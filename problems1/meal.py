def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    if time.lower().endswith(("a.m.", "am", "p.m.", "pm")):
        time_int, period = time.split()
        period = period.lower().replace(".", "") #removes dots
        hours, minutes = time_int.split(":")
        hours = int(hours)
        minutes = int(minutes)
        if period.lower() == "pm" and hours != 12:
            hours += 12
        elif period.lower() == "am" and hours == 12:
            hours = 0
        return hours + minutes/60
        # print(f"Hours are {hours}, minutes are {minutes}, and the period is {period}")    
    else:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)
        return(hours + minutes/60)




if __name__ == "__main__":
    # convert('12:30 pm')
    main()



