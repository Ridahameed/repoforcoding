# #functions of list
# vegetables = ["potato", "tomato", "onion"]
# vegetables.append("carrot")          # add carrot at the end
# print(vegetables)

# vegetables.insert(0, "cabbage")     #add cabbage at the beginning
# print(vegetables) 

# vegetables.remove("tomato")      # remove tomato
# print(vegetables) 

# vegetables.pop()        # remove last item
# print(vegetables) 

# vegetables.sort()       # sort the list A-Z
# print(vegetables)

# vegetables.reverse()         # reverse the list
# print(vegetables)  

# vegetables.index("onion")  # find index of onion
# print(vegetables)
# print("------------------------------------")
#practice some basic problems
#1.Write a program that asks the user for their name and then prints a greeting, like "Hello, [Name]!". This problem practices input and output.

# name = input("Enter your name: ")
# print("hello," + name)
# print("------------------------------------")
#2.This is a classic. Write a program that prints numbers from 1 to 100.
# For multiples of 3, print "Fizz".
# For multiples of 5, print "Buzz".
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".
# For all other numbers, print the number itself.
# This problem is great for practicing if/elif/else statements and loops.
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
print("------------------------------------")
#3.Problem 6: Sum of a List . Create a program that takes a list of numbers (you can hardcode it) and calculates the sum of all the numbers in the list. This teaches you how to iterate through a list.

numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("The sum of the list is:", total)
print("------------------------------------")
#4.Write a program that takes a string input from the user and counts the number of vowels (a, e, i, o, u) in the string. This problem helps you practice string manipulation and loops.
user_input = input("Enter a sentence: ")
if user_input == "":
    print("No input provided.")
else:
    vowels = "aeiouAEIOU"
    count = 0
    for char in user_input:
        if char in vowels:
            count += 1  
print("Number of vowels in your sentence is:", count)
print("------------------------------------")


