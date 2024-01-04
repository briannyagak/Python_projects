def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter a valid amount greater than zero.")
        else:
            print("Enter a valid positive integer.")
    return amount

deposit_amount = deposit()
print(f"Deposit successful. You deposited: ${deposit_amount}")
