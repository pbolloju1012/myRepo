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
    
    l=['prasanna','sweetie','prabhas','jahnavi']
    print(l[2:3])

    l=['prasanna','sweetie','prabhas','jahnavi']
print(l[:])

a=1
b=2
c=[b,a]
c.sort()
print(c)

l=[1,3,5,4,2,7,1,9,5,3,2]
l[0],l[-1] = l[-1], l[0]
print(l)

  
l=[1,2,3,4,5,6,7,8,9,1,2,3]
print(l[::-1])
print(l[::1])



# check if the given string is a palindrome

while True:
    name=input('enter your name :')
    if name==name[::-1]:
       print('it is a palindrome')
       break
    else:
       print('not a palindrome')

      
l=[1,2,3,4,5,6,7,8,9,0,12,13,14,15,16,56,76,45]
to_remove = [7,8,56,45]
# print(1 not in l)
result=[]
r=[]
for i in range(len(l)):   #0-14 for i in range(14)
    if l[i] not in to_remove:
        r.append(l[i])
print(r)


for i in l: #i-1-45
    if i not in to_remove :
        result.append(i)
print(result)

l=[1,2,3,4]
t=(1,2,3,4)
l[1]=6
print(l)

d=list(t)
e=tuple(l)
print(d)
print(e)

import copy
a=42
b=a #b=42
a=21
print(a,b)

c=[1,2,3,4,5]
d=c #d=[1,2,3,4,5]
e=copy.copy(c)
e[1]=6 [1,6,3,4,5]
d[1]=3 #d=[1,3,3,4,5]
print(id(c))
print(id(d))
print(id(e))
print(c,d,e)


#print("string",sep=" ",end="/n")
print("prasanna",end=" ")
print("sweety", end="-")
print("prabhas")

    
print("prasanna","sweety","prabhas","darling",sep=" loves Prabhas ")

l=[1,2,3,12,14,4,5,6,7,8,9,10]
for i in l:
    if i==10:
        break
d=[2,3,1]
print(d==l)
#d={key:value,key:value}
myDetails = {"name":"prasanna","masters":"CS","job":"google_aspirant"}
myDetails2 = {"name":"prasanna","job":"google_aspirant","masters":"CS"}

print(myDetails["name"])
print(myDetails==myDetails2)

birthdays={"prasanna":"oct 12","prabhas":"oct 23","dady":"july 10"}
print("my birthday is on",birthdays["prasanna"])
birthdays["mummy"]="nov 8"

print(birthdays)


for i in birthdays.keys():
    print(i)
for i in birthdays.values():
    print(i)
for i in birthdays.items():
    print(i)

birthdays={"prasanna":"oct 12","prabhas":"oct 23","dady":"july 10"}
print(list(birthdays.keys()))
    
print(list(birthdays.items()))
print("prasanna" in birthdays.keys())

details={"prasanna":{"age":25,"gender":"female"},
         "prabhas":{"age":37,"gender":"male"}}
#print(details.keys())
print(details,)
for key,value in details.items():
    print(key,value,sep=":")

details={"prasanna":{"age":25,"gender":"female"},
         "prabhas":{"age":37,"gender":"male"}}
#print(details.keys())
for key,value in details.items():
    print(key,value,sep=":")

print(details["prasanna"]["gender"])
count+=i

arr=[1,2,3,4,5,6]
def listLength(l):
    return Listlen(l)
    
arr2=[2,3,4,5,6,7,8,9,10]
    

def Listlen(arr):
    count=0
    for i in arr:
        count+=i
    sum=0
    for i in arr:
        sum=sum+i
    return sum
    
    
print(listLength(arr))
print(listLength(arr2))





# i ,count
# 1,count=1
# 2, count=2


name={"names":"prasanna","age":23,"city":"seatle"}
for i in name.items():
    print(i)


data={"prasanna":{"age":23,"father":"srinu","mother":"sunitha"},"prabhas":{"age":33,"father":"prabhas","mother":"mummy"}
    }
print(data["prasanna"]["father"])
print(data.values(),data.keys())
for i in data.items():
    print(i)
#to add a new key-value pair
name={"names":"prasanna","age":23,"city":"seatle"}
name["father"]="srinu"
print(name)
#to change the excisting value
name={"names":"prasanna","age":23,"city":"seatle"}
name["father"]="srinu"
name["names"]="sweetie"
print(name)
 #to delete the existing value
name={"names":"prasanna","age":23,"city":"seatle"}
name["father"]="srinu"
name["names"]="sweetie"

del name["age"]
print(name)
name={"names":"prasanna","age":23,"city":"seatle"}
name["father"]="srinu"
name["names"]="sweetie"

for i in name.items():
    print(i)

print("sweetie" in name.values())
print(max(name.values()))
#to max the values in the dictionary


number={"a":10,"b":20,"c":40}

myValues=max(number.values())
print(myValues)
#to reverse the values in the dictionary
numbers={'a': 1, 'b': 2, 'c': 3}
reverse={v:k for k,v in numbers.items()}
print(reverse)
words = ['apple2', 'banana2', 'apple3', 'orange', 'banana1', 'apple']
keys=  [1,2,2,3,4,5]
values=dict(zip(words,keys))
print(values)

name = 'hello\nthis is prabhas\nprasanna\'s boyfriend' #escape character(\'')
print(name)

name = '''hello


this is prabhas\nprasanna\'s




boyfriend'''
print(name)


spam = "Hello Prasanna"

print(spam[2:])
print(spam[2:5])


# string methods
spam="hello world"
name = "prAsaNna"
print(name.upper())
print(name.lower())

print(name.isupper())

print(spam.startswith('hello'))

list = ["prasanna,prabhas","apple","pineapple"]
string=' '.join(list) #join method for joining
print(string)

list2= string.split(',') #for breaking the string
print(list2)


string2="  hElLo wOrld    "
print(string2)
print(string2.strip())
string2=string2.lower().strip()
print(string2)

if string2=="hello world":
    print("Success, you understood python validations")
    

myDetails = "hi everyone, my name is prasanna and prasanna age is 45 and prasanna boyfriend is prabhas. saying hi again"
details=myDetails.split()
print(details)

details_dict={}
for i in details:
    details_dict[i]=details_dict.get(i,0)+1
    
print(details_dict)
numbers={k:v for k,v in details_dict.items() if v>=2 }
print(numbers)

   








        
          
    
        





        