#EASY
#1
print("Easy 1")
str1 = input("Enter your String: ")
str2 = ""
count = 0
vowel = ["a","e","i","o","u","A","E","I","O","U"]
for i in str1:
    if(i not in vowel):
        str2 = str2+i
    else:
        count+=1
print("Output:",str2,count)
print(" ")

#2
print("EASY 2")

def check_Palindrome(str): 
	for i in range(0, int(len(str)/2)): 
		if str[i] != str[len(str)-i-1]: 
			return False
	return True
strng = input("Enter the word: ")
ans = check_Palindrome(strng) 

if (ans): 
	print("TRUE") 
else: 
	print("FALSE") 
print(" ")

#3
print("Easy 3")
str1 = input("Enter your String: ")
str2 = ""
charArray = ["ful","ly"]
if len(str1)<4:
    print("Output:",str1)
else:
    for i in range (len(str1)-2,len(str1)):
            str2=str2+str1[i]
    if str2 in charArray[0]:
            str2 = str1+charArray[1]
            print("Output:",str2)
    else:
        str2 = str1+charArray[0]
        print("Output:",str2)
print(" ")

#Medium
#1
print("Medium 1")
str1 = input("Enter your String: ")
if str1.isalpha()!=True:
    str1 = input("Enter your String with no number or space: ")
ucase = []
lcase = []
for i in str1:
    if i.isupper() == True:
        ucase.append(i)
    else:
        lcase.append(i)
    
if len(ucase)>len(lcase):
        print(str1.upper())
else:
    print(str1.lower())
print(" ")

#2
print("Medium 2")
str1 = input("Enter your String: ")
if str1.isalpha()==True:
    print("Word")
elif str1.isdecimal()== True:
    print("Number")
else:
    print("Mixed")
print(" ")

#3
print("Medium 3")
str1 = input("Enter your String: ")
arr = []
i = 0
while i < len(str1):
    if str1[i].isupper() == True:
        arr.append(i)
    i+=1
if arr[1]-arr[0] == 1:
    print("BLANK")
else:
    j=arr[0]+1
    while j<arr[1]:
        print(str1[j],end =" ")
        j+=1
print(" ")

#4
print("Medium 4")
str1 = input("Enter your String: ")
arr = str1.split()

i = 0

while i < len(arr):
    if arr[i] == "too":
        if arr[i+1] =="good" or arr[i+1] =="good!":
            arr[i] = "excellent"
            arr.pop(i+1)
    i+=1
text = " "
for j in arr:
    text = text+j+" "
print(text)
print(" ")

#Hard1
#1
def concatting(text1,text2):
    
    newstr=''
    for c in text1:
        for d in text2:
            if c==d:
                newstr=newstr+c
                break
    
    for d in text2:
        for c in text1:
            if d==c:
                newstr=newstr+d
                break
    
    if(len(newstr)>0):
        print(newstr)
    else:
        print('Nothing in common')
        
concatting('harry','hermione')
concatting('dean','tom')
print(" ")

#2  
def palindrome_checker(string):

    count=0
    start=''
    end=''
    pal=''
    
    while(count<len(string)):
        start=start+str(string[count])
        end=str(string[len(string)-count-1])+end
        
        if(start==end):
            if(len(start)!=len(string)):
                pal=start
                count+=1
            
        else:
            count+=1
            
    if((string.count(pal))>2):
        print(pal)
    else:
        print("Not Plaindrome Substring")
        
palindrome_checker('fixprefixsuffix')
palindrome_checker('abcdabc')
print(" ")

#3

def passwordChecker(string):
    
    lowerCaseChecker=0
    upperCaseChecker=0
    digitChecker=0
    specialCharChecker=0
    
    for i in string:
        if(i>='A' and i<='Z'):
            upperCaseChecker+=1
        elif(i>='a' and i<='z'):
            lowerCaseChecker+=1
        elif(i=='_' or i=='$' or i=='#' or i=='@'):
            specialCharChecker+=1
        elif(i>='0' and i<='9'):
            digitChecker+=1
    
    warningText=""
    
    if(upperCaseChecker<1):
        warningText=warningText+"Uppercase character missing,"
        
    if(lowerCaseChecker<1):
         warningText=warningText+"Lowercase character missing,"
        
    if(digitChecker<1):
        warningText=warningText+"Digit missing,"
    
    if(specialCharChecker<1):
        warningText=warningText+'Special character missing,'
        
    if(upperCaseChecker>=1 and lowerCaseChecker>=1 and digitChecker>=1 and specialCharChecker>=1):
        print('OK')
    else:
        size=len(warningText)
        position=size-1
        new_Char=''
        
        warningText=warningText[:position]+new_Char+warningText[position+1:]
        print(warningText)
        
passwordChecker('ohMyBR@CU')
passwordChecker('ohmybracu')
passwordChecker('OhMyBR@CU20')















        
