try:
     n= int(input("Enter Nonber 1 : ")) 
     n1=int(input("Enter Nuabar 2: "))

     print("Addition: ",n+n1) 
except ValueError as e:
    print(e)
else:
    print("Try execute") 
finally:
    print("Finally executed")