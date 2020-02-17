# For this script I want you to prompt for user input, and put that information to use

# First you will prompt the user for their favorite number
my_num = input("Please enter your favorite number:")
# Python interprets all user input as STRINGs, meaning if you want to do any math with input numbers,
# you will need to first convert that input into a number using either "int()" like we did in class,
# or by using "float()" which does the same thing, but also preserves decimal values if necessary
my_num = int(my_num)
# Next you will need to use a conditional statement (if statement) to identify if
# the user input is odd or even
parity = ""
if(my_num % 2 == 1):
	parity = "odd"
else:
	parity = "even"
# Finally, print a message telling the user which (odd or even) their favorite number is
print("Your favorite number is " + parity)
