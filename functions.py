# Parts of a function 
# Name -> What is the name of the function
# Input -> What is the input of a function 
# Output -> Function 


output_of_print = print("hello world")
print(output_of_print)
# Name = Print 
# Input = Python object 
# Output = None


# User Defined Function 

# Add two number 

def Add(number_1, number_2):
    # body 
    # We want to add the two number
    res = number_1 + number_2
    # print(res)
    return res 


result = Add(12, 8)
print(result)

def Subtract(number_1, number_2):

    res = number_1 - number_2

    return res 

print(Subtract(12, 8)) # We should get 4



# We want a function that will give a sum from x, y 
# Loop inside a function

def RangeSumFunction(x, y):
    # We will use loops 
    # Function Body
    res = 0 
    for i in range(x,y+1):
        # loop body
        # Function inside a function
        res = Add(res, i)

    return res 

# 12 + 13 + 14 + 15 = 25 + 29 = 54
print(RangeSumFunction(12, 15))


# Recursion
# When you call a function inside its function definition 
# 
# Fibonacci Formula 
# 
# Xi = Xi-1 + Xi-2
# X0 = 0
# X1 = 1
# X2 = X1 + X0 = 1
# X3 = X2 + X1 = 2
# X4 = X3 + X2 = 3
# X5 = X4 + X3 = 5
# X6 = X5 + X4 = 8
# X12 = 144

def FibonacciIterative(n):
    x_n_2 = 0
    x_n_1 = 1

    if n == 0:
        return x_n_2 

    elif n == 1:
        return x_n_1 
    else:
        
        for i in range(n-1):
            # Calculate the new n 
            x_n = x_n_1 + x_n_2 
            # Shift the pervious n 
            x_n_2 = x_n_1
            x_n_1 = x_n 

        return x_n 

print(FibonacciIterative(0))
print(FibonacciIterative(1))
print(FibonacciIterative(12))

def FibonacciRecussive(n):

    if n == 0:
        return n
    elif n == 1:
        return n 
    else:
        res = FibonacciRecussive(n-1) + FibonacciRecussive(n-2)
        return res

print(FibonacciRecussive(0))
print(FibonacciRecussive(1))
print(FibonacciRecussive(12))
