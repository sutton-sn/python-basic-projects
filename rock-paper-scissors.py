# Import random
import random as rd

# Define variables
user_choice = input("What do you choose? Rock, Paper or Scissors? ")
machine_choice = rd.choice(['Rock', 'Paper', 'Scissors'])

# Print variable
print(f"Your decision is {user_choice}, the machine's decision is {machine_choice}")