import random

print("This is a Number Guessing Game")

number = random.randint(1,9)
chances = 0

print("Guess a number between 1 and 9: ")

#while statement to check how many chances are utilised

while chances<5:
    guess = int(input("enter your guess:"))

    if guess==number:
        print("CONGRATULATIONS! You have a smart mind!!")

    elif guess>number:
        print("A large number, guess something less than ", guess)

    else:
      print("A small number, guess something more than ", guess)

      #incrementing the number of chances by 1

    chances+=1

    #game over

    if chances>5:
        print("You lose! The number was ", number)

        