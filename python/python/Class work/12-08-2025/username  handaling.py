import random

# Dictionary to store user data
d = {}

while True:
    try:
        menu = """
Press 1 for Signup
Press 2 for Login
Press 3 for Forget Password
Press 4 for Exit
"""
        print(menu)

        # Taking user choice safely
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number (1-4)!")
            continue

        # Signup
        if choice == 1:
            try:
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
                    print("Signup successfully")
                else:
                    print("Password and confirm password do not match")
            except Exception as e:
                print(f"Error in signup: {e}")

        # Login
        elif choice == 2:
            try:
                if not d:
                    print("No user found! Please signup first.")
                    continue
                email = input("Enter email: ")
                password = input("Enter password: ")

                if d.get('email') == email and d.get('password') == password:
                    print("Login successfully")
                else:
                    print("Invalid credentials")
            except Exception as e:
                print(f"Error in login: {e}")

        # Forget Password
        elif choice == 3:
            try:
                if not d:
                    print("No user found! Please signup first.")
                    continue
                email = input("Enter your registered email: ")
                if d.get('email') == email:
                    otp = random.randint(1000, 9999)
                    print(f"Your OTP is: {otp}")  # In real-world, send via email/SMS

                    try:
                        user_otp = int(input("Enter OTP: "))
                    except ValueError:
                        print("OTP must be a number!")
                        continue

                    if user_otp == otp:
                        new_password = input("Enter new password: ")
                        confirm_password = input("Confirm new password: ")
                        if new_password == confirm_password:
                            d['password'] = new_password
                            print("Password reset successfully")
                        else:
                            print("Passwords do not match")
                    else:
                        print("Invalid OTP")
                else:
                    print("Email not registered")
            except Exception as e:
                print(f" Error in forget password: {e}")

        # Exit
        elif choice == 4:
            print("Exiting program... Bye!")
            break

        else:
            print("Invalid choice! Please try again.")
 
    except KeyboardInterrupt:
        print("\n Program stopped by user.")
        break
    except Exception as e:
        print(f" An unexpected error occurred: {e}")
