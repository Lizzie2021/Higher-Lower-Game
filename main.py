from art import *
from game_data import data
import random
import os


def print_detail(item):
    return f"{item['name']}, a {item['description']}, from {item['country']}"


def more_followers(a, b):
    if a['follower_count'] > b['follower_count']:
        return 'A'
    else:
        return 'B'


# Repeat the process until answer is wrong
score = 0
print(logo)
# Generate two random items
item_a = random.choice(data)
while True:
    item_b = random.choice(data)
    if item_a == item_b:
        item_b = random.choice(data)
    # Compare the follower count
    correct_answer = more_followers(item_a, item_b)
    print(f"Compare A: {print_detail(item_a)}.")
    print(vs)
    print(f"Against B: {print_detail(item_b)}")
    # Ask for choice
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    os.system("clear")
    print(logo)
    # Check the answer , track the score and give feedback
    if answer == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}.")
        item_a = item_b
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break

