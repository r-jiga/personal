def coke_machine():
    due = 50
    paid = 0
    change = 0
    denominations = [25, 10, 5]
    print("Amount Due:", due)

    while paid <= 50:
        payment = int(input("Insert Coin: "))
        if payment in denominations:
            paid += payment
            due -= payment
            if due == 0:
                print("Change Owed:", change)
                break
            if due < 0:
                change = paid - 50
                print("Change Owed:", change)
                break
        print("Amount Due:", due)


coke_machine()
