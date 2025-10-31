str1="Hello Python"
str2="Madhu"



def hello():
        return "Hello Python"

def name(myname):
        return("Hello" +" "+ myname)

def add(x , y):
        return x+y

def mul(a , b):
    result = a*b
    return result

def even_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

def stri(name):
    return(name.upper())   

def st_add():
    outcome=str1.join(str2)
    return outcome   

def num(n):
    if n<0:
        return "Negative"
    elif n==0:
        return "Zero"
    else:
        return "Positive"     

def greatest_two(x ,y):
    if x>y:
        return x
    elif y>x:
        return y
    else:
        return "Both are equal"

def grades(marks):
    if marks >=90:
        return "A"
    elif marks >=70:
        return "B"
    elif marks >=50:
        return "C"
    else:
        return "F"

def year(year):
   if(year %4==0 and year %100!=0) or (year %400==0):
        return "Leap Year"
   else:
        return "Not a Leap Year"

def greatest_three(x , y , z):
    if x>=y and x>=z:
        return X
    elif y>=x and y>=z:
        return y
    else:
        return z

def vowel_consonant(vo):
    if vo in 'aeiouAEIOU':
        return "Vowel"
    else:
        return "Consonant"

username =input("Enter your username :" )
passwword =input("Enter your password :" )
def login(username , password):
    if username=="admin" and password=="1234":
        return "Login Successful"
    else:
        return "Login Failed"


print(hello())
print(name("Madhu"))
print(add(4,8))
print(mul(5,8))
print(even_odd(8))
print(stri("madhulika"))
print(st_add())
print(num(-5))
print(greatest_two(10,20))
print(grades(63))
print(year(2026))
print(greatest_three(10,25,15))
print(vowel_consonant('g'))
print(login(username , passwword ))



