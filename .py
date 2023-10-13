import random
#import random so we can use the random generator
"""
-First, generate a random number between 0 and 100.  
-Use while loop to let the user have 10 guesses.
-If the guess is correct, print to screen "you guessed it, the number was:...",
-If the guess was too high or too low, tell the user which and take another guess. print to screen
-If the user does not guess it in 10 guesses, print to screen "you lose, the number was:..." """

num = random.randint(0, 100)
guesscount = 0

while guesscount < 10:
    guess = int(input("Guess a number between 0 and 100: "))
    guesscount += 1

    if guess == num:
      print("You guessed it! The number was: ", num)
      #return

    if guess < num:
      print("Too low!")
    else:
      print("Too high!")

print("You lose! The number was: ", num)
