# The code assigns the value 17 to a variable called age 
# and uses an if-else statement to check if the person is old enough to vote. 
# If the age is 18 or older, it prints an encouraging message asking if they have registered to vote yet. 
# Since the age is 17, the else block runs instead, printing an apology and 
# advising the user to register as soon as they turn 18.



age = 21
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")