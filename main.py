# Initial balance
balance = 1000.0

# Main loop
while True:
    print("\nWelcome to Simple ATM")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    # Get user input
    choice = input("Enter your choice: ")
    
    if choice == '1':
        # Check balance
        print(f"Your current balance is: ${balance:.2f}")
        
    elif choice == '2':
        # Deposit money
        deposit_amount = float(input("Enter amount to deposit: $"))
        if deposit_amount > 0:
            balance += deposit_amount
            print(f"${deposit_amount:.2f} has been deposited to your account.")
        else:
            print("Invalid deposit amount.")
        
    elif choice == '3':
        # Withdraw money
        withdraw_amount = float(input("Enter amount to withdraw: $"))
        if 0 < withdraw_amount <= balance:
            balance -= withdraw_amount
            print(f"${withdraw_amount:.2f} has been withdrawn from your account.")
        else:
            print("Invalid withdraw amount or insufficient balance.")
        
    elif choice == '4':
        # Exit
        print("Thank you for using Simple ATM. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")
