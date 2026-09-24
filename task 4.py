def func():
    local_var="i am local variable"
    print(local_var)
 # This will print the local variable defined inside the function

a=5
def func1():
    a=10
    print(a)
 # This will print the global variable defined outside the function

#  short explanation of the output:
# In the first function, we defined a local variable 'local_var' inside the function 'func()'. When we call the function, it prints the value of the local variable.
#  In the second function, we defined a global variable 'a' outside the function 'func1()'. When we call the function, it prints the value of the global variable. 
# This demonstrates how a variable defined inside a function (local variable) is different from a variable defined outside the function (global variable).       
