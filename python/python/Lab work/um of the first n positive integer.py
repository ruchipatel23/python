# (14) Write a python program to sum of the first n positive integers.
r = int(input("enter ur number"))
sum = 0
for i in range(1,r+1):
    sum += i
print(sum)