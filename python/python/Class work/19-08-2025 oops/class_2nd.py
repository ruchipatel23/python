# Class to demonstrate Loop, List, Tuple, Dictionary using Methods and Objects

class Demo:
    def __init__(self, name):
        self.name = name
        print(f"Object created for {self.name}")

    # Method to demonstrate Loop
    def loop_demo(self, n):
        print("\n🔹 Loop Demo:")
        for i in range(1, n+1):
            print(f"Number: {i}")

    # Method to demonstrate List
    def list_demo(self):
        print("\n🔹 List Demo:")
        fruits = ["apple", "banana", "cherry"]
        print("Fruits List:", fruits)
        fruits.append("mango")
        print("After Adding Mango:", fruits)

    # Method to demonstrate Tuple
    def tuple_demo(self):
        print("\n🔹 Tuple Demo:")
        colors = ("red", "green", "blue")
        print("Colors Tuple:", colors)
        print("First Color:", colors[0])

    # Method to demonstrate Dictionary
    def dict_demo(self):
        print("\n🔹 Dictionary Demo:")
        student = {"name": "Ruchi", "age": 21, "marks": 88}
        print("Student Dictionary:", student)
        student["age"] = 22
        print("After Updating Age:", student)


# ------------------------------
# Main Program
# ------------------------------

# Creating object
obj = Demo("Python Demo")

# Calling methods
obj.loop_demo(5)
obj.list_demo()
obj.tuple_demo()
obj.dict_demo()
