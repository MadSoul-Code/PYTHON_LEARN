import random


#collects user input
def collect_user_choice():
    user_untested_choice = input("Please enter rock, paper or scissors:     ").lower()
    return user_untested_choice

#Validates what the user entered
def validate_user_choice(user_untested_choice):
    if user_untested_choice == "rock": 
        return True
    elif user_untested_choice == "paper": 
         return True
    elif user_untested_choice == "scissors": 
         return True
    elif user_untested_choice == "shenia is a tonga girl": 
         return True
    else:
        return False

#
def get_computer_choice():
    computer_value = random.randint(1,3)
    
    if computer_value == 1:
        return "rock"
    elif computer_value == 2:
        return "paper"
    else:
        return "scissors"
    
def evaluate_results(my_choice, computer_choice):
    if my_choice == computer_choice: 
        return "It is a Tie"
    
    if my_choice == "rock" and computer_choice == "paper":
        return "You lost"
    elif my_choice == "paper" and computer_choice == "rock":
        return "You won"
    elif my_choice == "rock" and computer_choice == "scissors":
        return "You won"
    elif my_choice == "scissors" and computer_choice == "rock":
        return "You Lost"
    elif my_choice == "paper" and computer_choice == "scissors":
        return "You Lost"
    elif my_choice == "scissors" and computer_choice == "paper":
        return "You won"
    else:
        return "shenia is a tonga girl"
       
       
       
while True:        
    user_choice = collect_user_choice()
    is_valid = validate_user_choice(user_choice)



    if is_valid:
    
        computer_choice = get_computer_choice()
        result = evaluate_results(user_choice, computer_choice)
        print(result)

    else:
        print("Invalid input")
        
        
    to_continue =int(input("Do you want to continue or exit: use 1 for continue and 0 for exit:    "))
    if to_continue == 1 :
        pass
    else : 
        break