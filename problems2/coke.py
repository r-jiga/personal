# def coke_machine():
#     due = 50
#     paid = 0
#     change = 0
#     denominations = [25, 10, 5]
#     print("Amount Due:", due)

#     while paid <= 50:
#         payment = int(input("Insert Coin: "))
#         if payment in denominations:
#             paid += payment
#             due -= payment
#             if due == 0:
#                 print("Change Owed:", change)
#                 break
#             if due < 0:
#                 change = paid - 50
#                 print("Change Owed:", change)
#                 break
#         print("Amount Due:", due)

# def coke_machine():
#     due = 50
#     paid = 0
#     denominations = [25, 10, 5]
#     print("Amount Due:", due)

#     while paid < due:
#         coin = int(input("Insert Coin: "))
#         if coin in denominations:
#             paid += coin
#             remaining_due = due - paid
#             if remaining_due > 0:
#                 print("Amount Due:", remaining_due)
#     change = paid - due
#     print("Change Owed:", change)

# coke_machine()

def coke_machine():
    due_amount = 50
    paid_amount = 0
    denominations = [25, 10, 5]
    print("Amount due:", due_amount)

    while paid_amount < due_amount:
        coin = int(input("Insert coin:"))
        if coin in denominations:
                paid_amount += coin
                remaining_due = due_amount - paid_amount
                if remaining_due >= 0:
                     print("Amount due:", remaining_due)
                elif remaining_due < 0:
                     print("Amount owed:", paid_amount - due_amount)

coke_machine()