# write a Python program to get the Factorial number of given numbers.
r = int(input("enter ur number"))
if r < 0:
    print("enter positive number")
else :
    factorial = 1
    for i in range (1,r+1):
           factorial*= i
    print("factorial of  given number is :",factorial)