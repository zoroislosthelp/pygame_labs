import random
from art import higherlower_logo, vs_logo
from info import data
import os

def random_choice():
    return random.choice(data)

def change_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return(f"{name}, a {description}, from {country}")

def check(guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"

def compare():
    print(higherlower_logo)
    count = 0
    should_continue = True
    account_a = random_choice()
    account_b = random_choice()
    
    while should_continue:
        account_a = account_b
        account_b = random_choice()
        
        while account_a == account_b:
            account_b = random_choice()
        
        print(f"Compare A: {change_data(account_a)}.")  
        print(vs_logo)
        print(f"Against B: {change_data(account_b)}.")

        guess = input("Who had more followers? Type 'A' or 'B'. ").lower()
        follower_a = account_a["follower_count"]
        follower_b = account_b["follower_count"]
        is_correct = check(guess, follower_a, follower_b)
        
        os.system('cls')
        print(higherlower_logo)
        if is_correct:
            count += 1
            print(f"You're right! Current score: {count}")
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {count}")


compare()


