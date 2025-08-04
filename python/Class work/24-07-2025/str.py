s=input("enter name:")
if len(s)%2==0:
    print("ennter odd length of string")
else:
    mid=len(s)//2 
    print(s[mid-1],s[mid],s[mid+1])
     