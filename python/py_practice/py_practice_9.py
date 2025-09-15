
# ------------------------------------------------------------------
# Sorting a list without using sort function

# numbers = [52, 45, 98, 12, 78, 68]        
# sorted_numbers = []
# while numbers:                              
#     min_num = numbers[0]                      
#     for num in numbers:                       
#         if num < min_num:                    
#             min_num = num
#     sorted_numbers.append(min_num)           
#     numbers.remove(min_num)                 
# print(sorted_numbers)

# ------------------------------------------------------------------
# Finding the largest and second largest number in a list

# number = [52, 25, 98, 19, 88, 68]               #making a list of numbers

# max_num = 0                                     # variable to store the largest number
# second_max = 0                                  # variable to store the second largest number

# for num in number:                              #iterating through the list
#     if num > max_num:                           #if number is greater than the largest number then store it in max_num
#         second_max = max_num                    #assigning the old value of max_num to second_max
#         max_num = num                           #updating the  max_num 
#     elif num > second_max and  num < max_num:   #checking if the number is greater than the second largest number and less than the largest number
#         second_max = num                        #updating the second largest number
    
# print(f"largest number is: {max_num}" )                 #printing the largest number
# print(f"second  largest  number is: {second_max}" )     #printing the second largest number

# ------------------------------------------------------------------
# Swapping numbers without swap function

# a = 5
# b = 10
# a = a + b  
# b = a - b  
# a = a - b 
# print("a =", a ,"b =" , b)  

# ------------------------------------------------------------------
# Debugging and Exception Handling practice problems
# practie problem 1

# def safe_divide(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         return "Error: Division by zero is not allowed."
#     else:
#         return result 
# print(safe_divide(10, 0))
# print(safe_divide(10, 2))
# ------------------------------------------------------------------
# practie problem 2

# while True:
#     try:
#         num = int(input("Enter a number: "))
#         print(f"You entered: {num}")
#         print("Thank you!")
#         break
#     except ValueError:
#         print("Invalid input! Try again.")

# ------------------------------------------------------------------
# practie problem 3

# try:
#     with open("data.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     print("Operation complete.")

# ------------------------------------------------------------------
# practie problem 4

# def check_positive(num):
#     if num < 0:
#         raise ValueError("Number must be positive.")
#     return num
# print(check_positive(10))
# print(check_positive(-5))

# ------------------------------------------------------------------
# practie problem 5

# try:
#     text = input("Enter some text: ")
#     with open("output.txt", "w") as file:
#         file.write(text)
#         print("Text written to file successfully.")
# except IOError:
#     print("Could not write to file.")
# finally:
#     print("Writing complete.")

# ------------------------------------------------------------------
# practie problem 6

# try:
#     with open("log.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found. Creating new file.")
#     with open("log.txt", "a") as file:
#         file.write("Log file created.\n")
# finally:
#     print("Opration done.")

# --------------------------------------------------------------------
# practie problem 7 

# def multiply_list(lst):
#     print("Input list:", lst)
#     result = 0
#     for num in lst:
#         result *= num
#     print(num)  # Debugging statement
#     return result
# print(multiply_list([1, 2, 3, 4]))

# --------------------------------------------------------------------
# practie problem 8

# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
#     print(f"Result: {result}")
# except ValueError:
#     print("Not a number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# --------------------------------------------------------------------