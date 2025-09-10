#practice of *args 
def numbers(*args):
    for number in args:
        print ("Step:", number)
numbers(1, 2, 3, 4, 5)
#----------------------------------
print("-----------------------------------")

#practice of **kwargs
def info(**kwargs):
    for key, value in kwargs.items():
        print (key, ":", value)
info(name= "Rida", age=27, city="Lahore❤️")
#-----------------------------------
print("-----------------------------------")
#practice of *args and **kwargs together
def items(*args, **kwargs):
    print("*args: ", args )
    print("**kwargs: ", kwargs)
items(1,2,3,4,5, name="Asma" , age=34)
#-----------------------------------
print("-----------------------------------")    
#practice of practice of local and global variables
x = 10  # Global variable

def function():
    global x 
    x = 20  # Local variable
    print("Changed x: ", x)
#-----------------------------------
#practice of tuples
shopping_list = ("bag", "shoes", "dress")
print(shopping_list[0])  #can't change value of tuple
#-----------------------------------
#practice of lists
shopping_list = ["bag", "shoes", "dress"]
shopping_list[0] = "hat" # Can change value of list
print(shopping_list[0])  # Access first element
#-----------------------------------
