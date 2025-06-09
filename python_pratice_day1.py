#Basic Input/Output & Variables

#Write a program that asks the user for their name and age, then prints a greeting using both.

user=input("enter your name :")
age=input("enter your age :")

print(f'hello {user} and your age is {age}')

#Write a program that checks if a number entered by the user is even or odd.
number=int(input("enter a number: "))
if number%2==0:
    print("even number")
else:
    print("odd number")
#Write a program that asks for a password and only prints "Access granted" if the password is correct.


password=input("enter your password :")
while True:
     if password=="prabhas":
         print("access granted")
     else:
          print("access denied")
     break
#Write a loop that prints numbers from 1 to 10.
for i in range(1,11,1):
    print(i)
#Write a loop that keeps asking the user for a number until they enter 0, then prints "Done".

while True:
    number=int(input("enter a number : "))
    if number == 0:
        print("done")
        break

#Write a function that takes a list of numbers and returns their sum.        
def numbersList():
     count=0
     list=["2","3","5","6","7"]
     
     for num in list:
         count+=int(num)
         print(num)
     print(count)
         
numbersList()
#Write a function that prints your details (name, birthday, favorite movie).
def details():
    name="prasanna laxmi"
    birthday="oct 12"
    favoriteMovie="Darling"
    
    print(f'name is {name}')
    print(f'birthday is on {birthday}')
    print(f'and favorite movie is {favoriteMovie}')
details()

#Given a list of numbers, print only the even numbers.
listNumbers=["3","5","6","2","54"]
list=[]
for num in listNumbers:
    if int(num)%2==0:
        list.append(num)
print(list)
#Swap the first and last elements of a list.
list=["3","5","6","2","54"]
list[0],list[-1]=list[-1],list[0]
print(list)
#Dictionaries

#Create a dictionary with your name, age, and city. Print each key and value.
dictinoary={"name":"prasanna","age":24,"city":"boston"}
print(dictinoary)
#Add a new key-value pair to an existing dictionary.

dictinoary={"name":"prasanna","age":24,"city":"boston"}
dictinoary["height"]=5.4
print(dictinoary)
#String Methods

#Given a string, print it in uppercase and lowercase.
#Given a string, print it in uppercase and lowercase.

name="prasanna laxmi"

print(name.upper())
print(name.lower())
print(name.strip())
#Check if a string starts with "hello".
name="hello prasanna laxmi"

print(name.startswith("hello"))
#Palindrome Check

#Write a program that asks the user for a word and checks if it is a palindrome.
name = input("enter your name : ")
if name == name[::-1]:
    print("its a palindrome")
else:
    print("not a palindrome")
    #ATM Simulation

#Write a simple ATM program that lets the user check balance, deposit, withdraw, and exit.
balance=0
while True:
    print('1.check balance')
    print('2.deposite money')
    print('3.withdraw money')
    print('4.exit')
    choice=int(input('enter your choice :'))
    if choice==1:
        print(' your balance',balance)
    elif choice==2:
         deposite=int(input('enter money to deposite :'))
         balance=balance+deposite
         print('you total balance is',balance)
         
    elif choice==3:
         withdraw=int(input('enter your withdraw money :'))
         if balance>withdraw:
           
             balance=balance-withdraw
             print('now your balance is ',balance)
         else:
             print('you have insufficent amaount')
    elif choice==4:
         print('thank you for using the atm')
         break

 #  List Comprehension/Manipulation

#Remove all occurrences of a specific value from a list. 
numbers=[1,2,3,4,5,6]
numbers=[num for num in numbers if num != 2]
print(numbers)

# Random Module

# Write a function that returns a random fortune from a list of fortunes.

import random
def fortunes():
    numbers=["You will have a great day!",
        "Something unexpected will happen.",
        "Be cautious today.",
        "Happiness is coming your way.",
        "You will achieve your goals."]
        
    return random.choice(numbers)
        
print(fortunes())
#Dictionary Reverse

#Given a dictionary, create a new dictionary that swaps keys and values.
dictnory={"apple":"fruit","onion":"vegtable","laptop":"electric"}

swapDict={v:k for k,v in dictnory.items()}
print(swapDict)

#String Splitting and Joining

#Given a list of words, join them into a single string separated by commas, then split the string back into a list.
words=["apple","mango","pineapple"]
joined="," .join(words)
print(joined)
spilt=joined.split(",")
print(spilt)
Nested Dictionaries

#Create a nested dictionary for two people with their age and gender, then print each person's details.
people = {
    "person1": {
        "name": "Alice",
        "age": 30,
        "gender": "Female"
    },
    "person2": {
        "name": "Bob",
        "age": 25,
        "gender": "Male"
    }
}

for person, details in people.items():
    print(f"{person}:")
    for key, value in details.items():
        print(f"  {key}: {value}")