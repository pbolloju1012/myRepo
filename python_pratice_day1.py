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