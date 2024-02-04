#Partial Functions:
# Parial function allow us o fix certain number of argumets of a function and genrate a new function

from functools import partial

def multiplication(a,b):
    return a*b


# multi=partial(multiplication, a=10)   
# print(multiplication(b=5))
# multiplication(5)

multiplication=partial(multiplication, a=10)    # here we fixed a, a=10
print(multiplication(b=5))
print(multiplication)


