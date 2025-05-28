# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#*- multiplication 
#** -  exponentional
#print(23//3) #quotient
#print(23%3) #remainder
#print('hello')
#print('hello'+" Bolloju")
# print("hello" + 42)
#print('prabhas ' * 3)

#myName = input() #Camelcase 
#print("Myself Prabhas, its nice to meet you " + myName)
#myAge =int(input())
#print('my name is'+ myName +'and my age is' + str(myAge))

#print(42==42)
#print(42<100)

# print(4<5 or 5>6)
'''
name = input('enter your username :')
password = input('enter your password :')
if (name=="prasanna" and password=="prabhas is love") :
    print('you entered name and password is correct')
else:
    print("please enter correct name and password")

age = 24
if age<25:
    print("you are too young for me")
elif age<30 and age>=25:
    print("I might think about you")
else:
    print("you are too old for me")

name = ""
while name != "prasanna":

    print("please type your name")
   
print("you entered correct name")
print("new line")

myName=int(input("enter a number : "))
if myName % 2==0:
 print("it is evn number")
else:
 print("it is odd")
 myAge=int(input('what  is your age :'))
myName=input('what is your name : ')
if myAge <13 :
    print('you are a kid',myName)
elif myAge <=13 :
    print('you are a teenager',myName)
else :
    print('you are adult',myName)
    myScore=int(input('enter you exam score  :'))
if myScore ==0 or myScore>100:
    print('invalid number enter between 1 and 100')
  
if myScore>=90 or myScore ==100:
    print('you passed you got A grade')
elif myScore>=80:
    print('you passes you got B grade')
elif myScore>=70:
    print('you passes you got c grade')
else :
    print('you failed better luck next time')
'''
while True:
    myName=input('enter your name : ')
    myPassword=input('enter your password :')
    if myName =="prasanna" and myPassword =="sweetie123":
        print('login sucessfully')
        break
    else:
        print('try again')

print("%d,sum")
    #Write a loop that keeps asking for a number until the user types 0. Then print “Done.”
balance=0
while True:
    print("1.Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4.exit")
    choice=int(input('enter your choice :'))
    
    if choice==1:
        print("your blance is",balance)
        break
    elif choice==2:
        deposite=int(input('enter your deposite amount :'))
        balance +=deposite
        balance = balance + deposite
        print("$",deposite,'deposited successfully.')
    elif choice==3:
        withdraw=int(input('enter your amount to withdraw :'))
        if balance<withdraw:
            print('you have unsuficient amount')
        else:
            balance -=withdraw
            print("₹", withdraw, "withdrawn successfully.")
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please try again.")
    

#range(i=0,i<5,i++)

#range(start,end,+/-)


print('my nick name is ')
for i in range(5):
    print('Prasanna name',str(i))

print('name is')
for i in range(0,5,1):
    print('Sweetie name ',str(i))



print('my nick name is ')
for i in range(5):
    print('Prasanna name',str(i))

print('name is')
for i in range(5,0,-1):
    print('Sweetie name ',str(i))
    
    
#write python code to print even numbers in 0-10

for i in range(1,10):
    if (i%2==0):
        print(i)


def mydetails():
    print("prasanna")
    print("birhtday 1012")
    print("boyfriend:prabhas")

mydetails()
mydetails()
mydetails()

import random

def guessnumber(answer):
    if answer==1:
        return "its certain"
    if answer==2:
        return 'you guessed it right'
    if answer==3:
        return "ask gain later"
        
        
r = random.randint(1,3)
fortune=guessnumber(r)






def a():
    print('a() starts')
    b()
    d()
def b():
    print('b() starts')
    c()
    print('b() returns')
def c():
    print('c() starts')
    print('c() returns')
def d():
    print('d() starts')
    print('d() returns')
    
    
    
a()
def a():
    print('a() starts')
    b()
    d()
def b():
    print('b() starts')
    c()
    print('b() returns')
def c():
    print('c() starts')
    print('c() returns')
def d():
    print('d() starts')
    print('d() returns')
    
    
    
a()

def finalCode():
    for i in range(10):
        if i%2==0:
            print(i**2)
        else :
            print(i**3)
            
finalCode()

a=['hello','prasanna','sweetie','abcd','prabhas','python','salaar']
print(a[1],"loves",a[4],"her favorite movie is",a[-1])
print(f'{a[1]} loves {a[4]} her favorite movie is {a[-1]}')

a=['hello','prasanna','sweetie','abcd','prabhas','python','salaar']
a[0],a[1],a[2],a[3]


print(a)
for i in range(len(a)):
    print(a[i])

for i in a:
    print(i)

b=['jahnavi kapoor','aishwarya rai']
b=b+['Katrina Kaif']

print(a+b)
print(b*3)

d=['ashwik','prasanna']
teacher,trainee=d
print(teacher)
print(trainee)

# list,tuple,set,dictionary
#lists are mutable(changable)

balance=0
while balance<1000:
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
             
            # withdraw=int(input('enter how much you want to withdraw :'))
             balance=balance-withdraw
             print('now your balance is ',balance)
         else:
             print('you have insufficent amaount')
    elif choice==4:
         print('thank you for using the atm')
         break