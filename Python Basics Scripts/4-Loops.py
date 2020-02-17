# For this script you will make use of for-loops and while-loops



# Using a for-loop print every number from 1-10 in ascending order
for num in range(1, 11):
	print(num, end=" ")
print("\n")
# Using a while-loop print every number from 1-10 in descending order
i = 10
while i >= 1:
	print(i, end=" ")
	i -= 1
# Using nested for-loops, print a basic multiplication table for number 1-10
print("\n\n")
for i in range(1, 11):
	for j in range(1, 11):
		print("%4d"%(i*j), end="")
	print()


