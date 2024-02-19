import random
name= str(input("Enter your name:-"))
# Taking Inputs
lower = int(input("Enter Lower bound:- "))

# Taking Inputs
upper = int(input("Enter Upper bound:- "))
# generating random number between the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only 7 chances to guess the number!\n")

# Initializing the number of guesses.
count = 0

#While loop so that guesses can be limited
while count < 7:
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations",name,"you did it in",count,"try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")
# If Guessing is more than required guesses
if count >= 7:
	print("\nThe number is %d" % x)
	print("\tSorry",name,",Better Luck Next time!")
