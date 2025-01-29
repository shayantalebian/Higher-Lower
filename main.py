import random
from art import vs, logo
from game_data import data

def get_random_account():
    return random.randint(0, len(data) - 1)

game_over = False
round = 0
score = 0
index_A = get_random_account()
index_B = get_random_account()
error = False
while index_A == index_B:
    index_B = get_random_account()

while game_over == False:
    if round > 0:
        print("\n" * 200)
        print(logo)
        print(f"You're right! Current score: {score}")
        index_A = index_B
        index_B = get_random_account()
        
        print(f"Compare A: {data[index_A]['name']}, a {data[index_A]['description']}, from {data[index_A]['country']}")
        print(vs)
        print(f"Against B: {data[index_B]['name']}, a {data[index_B]['description']}, from {data[index_B]['country']}")
    elif error == True:
        True
    else:
        print(logo)
        print(f"Compare A: {data[index_A]['name']}, a {data[index_A]['description']}, from {data[index_A]['country']}")
        print(vs)
        print(f"Against B: {data[index_B]['name']}, a {data[index_B]['description']}, from {data[index_B]['country']}")
    
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    try:
        if user_choice != "a" and user_choice != "b":
            raise ValueError
    except ValueError:
        print("Invalid input. Please type 'A' or 'B'")
        error = True
        continue
    
    round += 1

    if user_choice == "a":
        if data[index_A]["follower_count"] > data[index_B]["follower_count"]:
            score += 1
        else:
            game_over = True

    elif user_choice == "b":
        if data[index_B]["follower_count"] > data[index_A]["follower_count"]:
            score += 1
        else:
            game_over = True

print("\n" * 200)
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")