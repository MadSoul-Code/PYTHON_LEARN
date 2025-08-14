print("-------User Input-------")
print("-------Welcome to MASEVEN's BANK-------")

balance = 0.0
max_attempts = 5

while True:
    name_password = input("Enter username and password (format: username-password): ")

    if '-' not in name_password:
        print("Invalid format. Please use username-password.")
        continue

    username, password = name_password.split('-', 1)

    print("Username:", username)

    while len(password) < 8:
        print("The password must be at least 8 characters long.")
        password = input("Enter password again: ")

    attempts = 0
    while attempts < max_attempts:
        input_password = input("Enter password: ")
        if password == input_password:
            print("You have logged in successfully!!!!!")
            break
        else:
            print("Incorrect password.")
            attempts += 1

    if attempts == max_attempts:
        print("Too many incorrect attempts. Try again later.")
        break

    while True:
        print("\n--------MASECHA's Banking balance--------")
        print("Choose options:")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Balance")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            withdrawal = float(input("How much do you want to withdraw?: "))
            if balance >= withdrawal:
                balance -= withdrawal
                print(f"Your remaining balance is:R {balance:.2f}")
            else:
                print("Insufficient Funds! Please deposit.")
        elif choice == 2:
            deposit = float(input("How much do you want to deposit?: "))
            balance += deposit
            print(f"Your new balance is:R {balance:.2f}")
        elif choice == 3:
            print(f"Your current balance is:R {balance:.2f}")
        elif choice == 4:
            print("Thank you for using MASEVEN's BANK!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")

    continue_prompt = input("Do you want to login again? (yes/no): ").lower()
    if continue_prompt != "yes":
        print("Goodbye!")
        break
