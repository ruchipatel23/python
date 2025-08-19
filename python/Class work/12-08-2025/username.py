import random

# Dictionary to store user data
d = {}

while True:
    menu = """
Press 1 for Signup
Press 2 for Login
Press 3 for Forget Password
Press 4 for Exit
"""
    print(menu)
    choice = int(input("Enter your choice: "))

    # Signup
    if choice == 1:
        name = input("Enter name: ")
        email = input("Enter email: ")
        mno = input("Enter mobile number: ")
        password = input("Enter password: ")
        cpassword = input("Confirm password: ")

        if password == cpassword:
            d['name'] = name
            d['email'] = email
            d['mno'] = mno
            d['password'] = password
            print("Signup successfully ✅")
        else:
            print("Password and confirm password do not match ❌")

    # Login
    elif choice == 2:
        if not d:
            print("No user found! Please signup first.")
            continue
        email = input("Enter email: ")
        password = input("Enter password: ")

        if d.get('email') == email and d.get('password') == password:
            print("Login successfully ✅")
        else:
            print("Invalid credentials ❌")

    # Forget Password
    elif choice == 3:
        if not d:
            print("No user found! Please signup first.")
            continue
        email = input("Enter your registered email: ")
        if d.get('email') == email:
            otp = random.randint(1000, 9999)
            print(f"Your OTP is: {otp}")  # In real system, this would be sent via email/SMS
            user_otp = int(input("Enter OTP: "))
            if user_otp == otp:
                new_password = input("Enter new password: ")
                confirm_password = input("Confirm new password: ")
                if new_password == confirm_password:
                    d['password'] = new_password
                    print("Password reset successfully ✅")
                else:
                    print("Passwords do not match ❌")
            else:
                print("Invalid OTP ❌")
        else:
            print("Email not registered ❌")

    # Exit
    elif choice == 4:
        print("Exiting program... Bye! 👋")
        break

    else:
        print("Invalid choice! Please try again.")
