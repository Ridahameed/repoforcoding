# This is python practice 2

# practice of Casting
x = 1.5
y = 2
print(int(x))  # Convert x to int
print(float(y))  # Convert y to float

# practice of String
name = "John"
print(name.upper())  # Convert name to uppercase
print(name.lower())  # Convert name to lowercase
print(name.replace("John", "Doe"))  # Replace 'John' with 'Doe'

# practice of List
fruits = ["apple", "banana", "cherry"]  
print(fruits[0])  # Access first element
fruits.append("orange")  # Add 'orange' to the list
print(fruits)  # Print the updated list

# practice of Dictionary
person = {"name": "Alice", "age": 30}
print(person["name"])  # Access value by key
person["age"] = 31  # Update age
print(person)  # Print the updated dictionary

# practice of  functions
def pizza (*args):
    for topping in args:
        print(topping)
pizza("onions", "olives", "cheese") 
#----------------------------------------

name = "Rida"
age = 27
print(f"My name is {name} and i am {age} years old")

#practice of positive and negative numbers
number = input("Write a number: ")
num = int(number)
if num > 0 :
    print("Number is positive")
elif num < 0 :
    print("Number is negetive")
else:
    print("number is zero")



        
