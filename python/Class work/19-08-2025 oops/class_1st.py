class MyClass:
    def pattern1(self):
        for i in range(1, 6):  # Loop from 1 to 5
            print("*" * i)      # Print '*' i times

    def pattern2(self):
        for i in range(1, 6):  # Loop from 1 to 5
            print(" " * (6 - i) + "*" * i)  # Print spaces and then '*'

    def pattern3(self):
        for i in range(1, 6):  # Loop from 1 to 5
            print(" " * (6 - i) + "*" * i)  # Print spaces and then '*'

# Example usage
my_class = MyClass()
print("Pattern 1:")
my_class.pattern1()

print("\nPattern 2:")
my_class.pattern2()

print("\nPattern 3:")
my_class.pattern3()
