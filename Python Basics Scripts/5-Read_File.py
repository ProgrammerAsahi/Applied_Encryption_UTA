# For this script you will read lines from "input.txt"
# If we refer to lines 1,2,3, and 4 as a,b,c, and d respectively
# then you will calculate and print (a*b) + (c*d)
f = open("input.txt", "r")
a = int(f.readline())
b = int(f.readline())
c = int(f.readline())
d = int(f.readline())
f.close()
print((a*b) + (c*d))