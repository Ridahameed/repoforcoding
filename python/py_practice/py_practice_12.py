# class student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def study(self):
#         print(f"{self.name} is studing")
    
#     def take_exam(self):
#         print(f"{self.name} is taking an exam")

# student_1 = student("Aliya", 21, "A+")
# student_2 = student("Samia", 24, "B+")

# student_1.study()
# student_2.take_exam()
#
#-------------------------------------------------
# from abc import ABC, abstractmethod
# class account(ABC):
#     def __init__(self, owner, account_no, balance):
#         self.owner = owner
#         self.account_no = account_no
#         self.balance = balance
    
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposit of Rs. {amount} is successful. New balance is {self.balance}")

#     @abstractmethod
#     def withdraw(self, amount):
#         pass

#     @abstractmethod    
#     def monthly_process(self):
#         pass

# class savingAccount(account):
#     def __init__(self, owner, account_no, balance, interest_rate):
#         super().__init__(owner, account_no, balance)
#         self.interest_rate = interest_rate

#     def withdraw(self, amount):
#         if self.balance - amount >= 0:
#             self.balance -= amount
#             print(f"withdrawal scessful of Rs. {amount}. New balance is Rs. : {self.balance}")
#             return True
#         else:
#             print("withdrawal fail")
#             return False
    
#     def monthly_process(self):
#         monthly_interest = self.balance * (self.interest_rate / 12)
#         self.balance += monthly_interest
#         print(f"monthly interest is {monthly_interest}. New balance is {self.balance}")

# class currentAccount(account):
#     def __init__(self, owner, account_no, balance, loan_limit, fees):
#         super().__init__(owner, account_no, balance)
#         self.loan_limit = loan_limit
#         self.fees = fees
 
#     def withdraw(self, amount):
#         if self.balance - amount >= -self.loan_limit:
#             self.balance -= amount
#             print(f"withdrawal scessful of Rs. {amount}. New balance is Rs. : {self.balance}")
#             return True
#         else:
#             print(f"withdrawal fail because the loan limit exceeded of Rs. : {self.loan_limit}")
#             return False
        
    
#     def monthly_process(self):
#         if self.balance < 0:
#             self.balance -= self.fees
#             print(f"balance is negitive. deducted a fee of rs. : {self.fees}")

# import csv

# class bank:
#     def __init__(self, name):
#         self.name = name
#         self.accounts = {}

#     def add(self, account):
#         pass

#     def get(self, account_no):
#         pass

#     def transfer(self, account_no_from, account_no_to, amount):
#         pass

#     def show(self):
#         pass
