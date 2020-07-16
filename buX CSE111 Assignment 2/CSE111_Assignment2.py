#Easy
#1
print("Answer of Easy Number 1")
def retFraction(x , y):
    if y==0:
        print("Output = ",0)
    else:
        z1 = x/y
        z2 = int(x/y)
        output = z1 - z2
        if(output>1):
            print("Output = ",0)
        else:
            print("Output = ",output)
retFraction(5,2)
retFraction(5,0)
retFraction(0,5)
print(" ")

#2
print("Answer of Easy Number 2")
def bmi(height, weight):
    height = height*0.01
    BMI = weight/(height**2)
    BMI = round(BMI,1)
    if BMI<18.5:
        print("Score is",BMI)
        print("You are Underweight")
    elif BMI>18.5 and BMI<24.9:
        print("Score is",BMI)
        print("You are Normal")
    elif BMI>25 and BMI<30:
        print("Score is",BMI)
        print("You are Overweight")
    elif BMI>30:
        print("Score is",BMI)
        print("You are Obese")
bmi(175,96)
bmi(152,48)
print(" ")

#3
print("Answer of Easy Number 3")
def sumOfDivisible(min, max, divisor):
    count = 0
    for i in range(min, max):
        if i%divisor==0:
            count+=i
    print(count)
sumOfDivisible(0,10,2)
sumOfDivisible(3,16,3)
print(" ")

#Medium
#1
print("Answer of Medium Number 1")
def totalPrice(burger,address="Mohakhali"):
    price = 0
    delivery_charge = 0
    tax = 0
    total = 0
    if burger == "BBQ Chicken Cheese Burger":
        price = 250
    elif burger == "Beef Burger":
        price = 170
    elif burger == "Naga Drums":
        price = 200
    if address != "Mohakhali":
        delivery_charge = 60
    else:
        delivery_charge = 40
    total = price+delivery_charge+(price*0.08)
    print(total)
totalPrice("Beef Burger","Dhanmondi")
totalPrice("Beef Burger",)
print(" ")
#2
print("Answer of Medium Number 2")
def replace_domain(email, new_doamin="sheba.xyz",old_domain="kaaj.com"):
    new_email = ''
    for c1, c2 in zip(email, email[1:]):
        new_email = new_email+c1
        if c1 == "@":
            if c2 == "s":
                print("Unchanged:",email)
            else:
               new_email = new_email+  new_doamin
               print("Changed:", new_email)
replace_domain("alice@kaaj.com","sheba.xyz","kaaj.com")
replace_domain("bob@kaaj.com","sheba.xyz",)
replace_domain(input("Enter the email"),input("Enter the new domain"),input("Enter the old domain"))
print(" ")      

#3
print("Answer of Medium Number 3")
def no_of_vowels(name):
    vowels = ["a","e","i","o","u"]
    count = 0
    name_vowels = []
    for i in name:
        if i in vowels:
            name_vowels.append(i)
            count +=1
    if len(name_vowels)==0:
        print("No vowel in the name")
    else:
        print("Vowels: ",end=" ")
        for i in name_vowels:
            print(i,end=" ")
        print("Total number of vowels:",count)
no_of_vowels("Steve Jobs")
no_of_vowels(input("Enter the name: "))
print(" ")

#4
print("Answer of Medium Number 4")

def check_Palindrome(str): 
	for i in range(0, int(len(str)/2)): 
		if str[i] != str[len(str)-i-1]: 
			return False
	return True
strng = input("Enter the word: ")
ans = check_Palindrome(strng) 

if (ans): 
	print("Palindrome") 
else: 
	print("Not a palindrome") 
print(" ")

#Hard
#1
print("Answer of Hard Number 1")
from datetime import date
from datetime import datetime, timedelta

def extra_pay(name,salary,dates):
    extra = 0
    today = date.today()
    date_join = datetime.strptime(dates, '%Y-%m-%d' ).date()
    difference = today - date_join
    years = int(int(difference.days)/365)
    if years<5:
        extra = salary*0.1
      
    elif years> 5 and years<10:
        extra = salary*0.1+5000
    elif years>10:
        extra = salary*0.15+15000
        
    print(name, ":", extra)
extra_pay('Alice', 20000, '2017-03-21')
print(" ")

#2
def find( number_of_days ): 
    y = int(number_of_days/365)
	
    ndays = number_of_days-(365*y)
		
    m =int( ndays/30)
	
    d = ndays-(m*30)
    print(y,"years,", m, "months and",d,"days")
find(4320)
	
    
