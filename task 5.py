import math
import random
import datetime 

# Calculate square root using math module
num = 16    
a = math.sqrt(num)
# sqrt function gives the square root of the given number
print("The square root of", num, "is:", a)

# Generate a random number using random module
random_number = random.randint(1, 10)
#rand int function genrete a random number between the given range
print("A random number between 1 and 10 is:", random_number)

# Display the current date/time using datetime module
current_datetime = datetime.datetime.now()
print("The current date and time is:", current_datetime)