# lambda fnction
# addition 
(lambda x,y: x+y)(23,32) #input

#Product
(lambda a, b: a*b)(10,10)

#list 
ls=[1,2,3,4,9,8,7,6,5]
sqr=(lambda ls: [i**2 for i in ls])(ls)
print(sqr)

# even odd
even=(lambda x: [i%2==0 for i in ls])(ls)
print(even) # true for even


