#practice of for_loop
for i in range(50):
    if i % 2 != 0:
        print(i)

#practice of break and continue
#for num in range(30):
#    if num % 3 == 0:
#        continue
#    print(num)

#practice of positive and negative numbers
number = input("Write a number: ")
num = int(number)
if num > 0 :
    print("Number is positive")
elif num < 0 :
    print("Number is negetive")
else:
    print("number is zero")
# even and odd numbers
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")