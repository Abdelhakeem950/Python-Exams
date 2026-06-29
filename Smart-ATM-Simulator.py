password = 2037
Balance = 10000

PIN = int(input("Please Enter your PIN : "))

if PIN == password:

    Operation = input ('Withdraw / Check Balance : ').strip().capitalize()

    if Operation == "Check balance": print(f"Current Balance : {Balance:,}")
       
    elif Operation == "Withdraw":
        amount = int(input("Enter Amount : "))
        if amount > Balance:
            print("Sorry! Balance is insufficient")
        else:
            Balance -= amount
            print("Withdrawal Successful")
            print(f"Your Remaning Balance is {Balance:,}")

    else: print("Invalid Operation")

else: print(" PIN is Incorrrect ")