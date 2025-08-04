while True:
    print("\nMenu:")
    print("1. Reverse string")
    print("2. Fibonacci series")
    print("3. Check prime")
    print("4. Exit")
    
    choice = input("Choose (1-4): ")
    
    if choice == '1':
        print("Reversed:", input("Enter text: ")[::-1])
    
    elif choice == '2':
        n = int(input("How many terms? "))
        a, b = 0, 1
        print("Fibonacci:", end=" ")
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()
    
    elif choice == '3':
        num = int(input("Check number: "))
        if num <=1:
            print("Not prime")
        else:
            prime = True
            for i in range(2, int(num**0.5)+1):
                if num%i == 0:
                    prime = False
                    break
            print("Prime" if prime else "Not prime")
    
    elif choice == '4':
        print("thank you")
        break
    
    else:
        print("Invalid choice")
