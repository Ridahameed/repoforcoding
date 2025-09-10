number = [52, 25, 98, 19, 88, 68] #making a list of numbers

max_num = 0  # variable to store the largest number
second_max = 0 # variable to store the second largest number

for num in number:   #iterating through the list
    if num > max_num:  #if number is greater than the largest number then store it in max_num
        second_max = max_num #assigning the old value of max_num to second_max
        max_num = num    #updating the  max_num 
    elif num > second_max and  num < max_num: #checking if the number is greater than the second largest number and less than the largest number
        second_max = num #updating the second largest number
    
print(f"largest number is: {max_num}" ) #printing the largest number
print(f"second  largest  number is: {second_max}" ) #printing the second largest number