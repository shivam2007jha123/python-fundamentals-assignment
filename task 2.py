# This is valid for for loop
n=int(input("enter your number:"))
for i in range(1,n+1):
    print(i)  #this will print the number from 1 to n

# This is valid for while loop
i=n
while i>=1:
    print(i)
    i-=1 #this reverse the number from n to 1

# This is valid for multiplication table

for i in range(1,11):
    print(f"The table of the given number {n} is :{n} x {i} = {n*i}")  #this will print the multiplication table of the given number n from 1 to 10 
