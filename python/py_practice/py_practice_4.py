#practice import
import random

secret_number = random.randint(1, 10)
guess_number = int(input("Guess number between 1 and 10: "))

if guess_number == secret_number:
    print(" 🥳 Congratulations! you guessed right")
else:
    print(f"😢 Sorry, the secret number was {secret_number}.")

#practice of mini calculater

num1 = float(input("Enter first number: "))
operater = input("Enter operater (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operater == "+":
    result = num1 + num2
elif operater == "-":
    result = num1 - num2
elif operater == "*":
    result = num1 * num2    
elif operater == "/":
        result = num1 / num2
else:
    result = "Invalid operator"
print(f"The result is: {result}")