from art import logo, vs
from game_data import data
import random
import os

def clear():
  os.system('cls')

def right_answer(A, B):
  if A["follower_count"] > B["follower_count"]:
    return "A"
  else:
    return "B"
  
def guess_check():
  print(logo)
  A = random.choice(data)
  B = random.choice(data)
  if B == A:
        B = random.choice(data)
  end_game = False
  score = 0
  while not end_game:
    print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']} from {B['country']}.")
    guess = input("Who has more followers?  A or B? \n").upper()
    answer = right_answer(A, B)
    if guess == answer:
      score += 1
      A = B
      B = random.choice(data)
      if B == A:
        B = random.choice(data)
      clear()
      print(f"You're right! Score: {score}\n")
    else:
      print(f"You lose!")
      end_game = True
  if end_game:
    print(f"Final score: {score}")
    play_again = input("Do you want to play again? y/n? \n").lower()
    if play_again == "y":
      clear()
      guess_check()
    else:
      print("Thanks for playing!")


guess_check()