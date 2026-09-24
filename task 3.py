a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
def add(a,b):
    return a+b  
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def modulus(a,b):
    return a%b

#return function called to display the result of the operation

print("Addition of two numbers is:",add(a,b))   
print("Subtraction of two numbers is:",substract(a,b))
print("Multiplication of two numbers is:",multiply(a,b))            
print("Division of two numbers is:",division(a,b)) # This gives the quotient of the division of two numbers
print("Modulus of two numbers is:",modulus(a,b)) #This gives the remainder of the division of two numbers   
