## EASY
#1.
print("Answer of Easy Number 1")
count = 0
for i in range(1, 31):
    if(i%3==0) or (i%5==0):
        count +=1
        print(i)
print("Count =",count)
print(" ")

#2.
print("Answer of Easy Number 2")
inputs = []
limit = int(input("Enter the limit"))
for i in range(limit):
    x= int(input("Enter your input"))
    inputs.append(x)

inputs = sorted(inputs)
print("Maximum: ",inputs[limit-1])
print(" ")

#3
print("Answer of Easy Number 3")
marks = []
limit = int(input("Total Courses"))
for i in range(limit):
    x= int(input("Enter your marks"))
    marks.append(x)

for mark in marks:
    grade = ''
    if mark >=90:
        grade = "A"
    if mark >=85 and mark < 90:
        grade = "A-"
    if mark >= 80 and mark < 85:
        grade = "B+"
    if mark >= 75 and mark < 80:
        grade = "B"
    if mark >= 70 and mark < 75:
        grade = "B-"
    if mark >= 65 and mark < 70:
        grade = "C+"
    if mark >= 60 and mark < 65:
        grade = "C"
    if mark >= 57 and mark < 60:
        grade = "C-"
    if mark >= 55 and mark < 57:
        grade = "D+"
    if mark >= 52 and mark< 55:
        grade = "D"
    if mark >= 50 and mark < 52:
        grade = "D-"
    if mark < 50:
        grade = "F"

    print("Grade = ", grade)
print(" ")

#4
print("Answer of Easy Number 4")
number = int(input("Enter your number: "))
for i in range(2,number):
    if(number%i)==0:
        print("Not Prime")
        break
    else:
        print("Prime Number")
        break
print(" ")

##Medium
#1.
print("Answer of Medium Number 1")
limit = int(input("Enter the limit: "))
n1= 0
n2=1
while n1 < limit:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
print(" ")

#2
print("Answer of Medium Number 2")
inpt = input("Enter your input: ")
reverse = ""
for i in inpt:
    reverse = i+reverse
print(reverse)
print(" ")

#3
print("Answer of Medium Number 3")
inpt = int(input("Enter your Input: "))
count=0
for i in range(1,inpt):
    if(inpt%i==0):
        count = count+i
if count==inpt:
    print("Perfect")
else:
    print("Not Perfect")
print(" ")

##Hard
#1.
print("Answer of Hard Number 1")
inpt=input("Enter your input: ")
unique=[]
for i in inpt:
    if i in unique:
        continue
    else:
        unique.append(i)
print(len(unique))
print(" ")

#2
print("Answer of Hard Number 2")
inpt = int(input("Enter your number: "))
n = 0
for i in range(1, inpt + 1):  
    for j in range (1, (inpt - i) + 1): 
        print(end = " ") 
          
    while n != (2 * i - 1): 
        print("*", end = "") 
        n = n + 1
    n = 0
    print()  
  
k = 1
n = 1
for i in range(1, inpt):  
    for j in range (1, k + 1): 
        print(end = " ") 
    k = k + 1
           
    while n <= (2 * (inpt - i) - 1): 
        print("*", end = "") 
        n = n + 1
    n = 1
    print() 
print(" ")

#3
print("Answer of Hard Number 3")
inpt = int(input("Enter your number: "))
binary = bin(inpt)
n = ""
binary = str(binary)
print( binary)
for i in binary:
    if i=="1":
        n=i+n
print(n)
dec = 0
for j in n:
    dec = dec*2+int(j)
print(dec)

