# 6)Write a Python program to get the Fibonacci series of given range.
num=int(input("enter ur range"))
r = [0,1]
for i in range (num):
    c = r[-1]+r[-2]
    r.append(c)

print(r)