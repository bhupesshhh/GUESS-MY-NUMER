import random

# Game Initiation
print("GUESS MY NUMBER!!!\n")
print("Number lies between (1-100)\n")
limit = input("Do you wanna start the game? (yes/no)")

if limit.lower() == "yes":
  # Start the game with Yes only
  gameplay = True
  gameon = True
  print("\nLet's start the game!\n")
else:
  gameplay = False
  gameon = False

# Gameon Condition
while gameon:

  # Random Number Picked
  counts = 0 
  right_number = random.randint(1,100)

  # Gameplay Condition
  while gameplay:

    # Guess Count
    counts += 1

    # Loop to get only in-range integer
    while True:
      guess = input("Pick your number! (1-100)")
      if guess.isdigit():
        if int(guess) > 100 or int(guess) < 1:
          print("Number not in range")
        else:
          break
      else:
        print("Incorrect Number")

    # Check for correct guess
    number = int(guess)
    if number < right_number:
      print("Your guess is too low")
    if number > right_number:
      print("Your guess is too high")
    if number == right_number:
      print("\nCongratulations, Your guess is correct")
      print(f"{right_number} is the correct answer\n")
      gameplay = False
      break


  # Result and Score
  print(f"You took {counts} guesses to get the right answer\n")

  # Replay Game
  replay = input("Do you wanna play the game again? (yes/no)")
  if replay.lower() == "yes":
    gameon = True
    gameplay = True
    print("\n")
  else:
    gameon = False
    break

# Endnote
print("\nThanks for playing the game")
print("We hope to see you soon!\n")