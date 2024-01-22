#welcome to python coding

#PROBLEM:
#Find the given number is prime or not?..

num=int(input("Enter a number:")) #taking user input
print("You entered:",num)
for i in range(2,num):
    if num%i==0:
        print("The given number is not prime")
        break
else:
    print("The given number is prime")


#PROBLEM:
#Find the palindrome 
    
a =input("Enter a string:")
print("You entered:",a)
c = ""

for i in range(len(a) - 1, -1, -1):
    c += a[i]

if a == c:
    print("The string is a palindrome")
    print("Output:",c)
else:
    print("The string is not a palindrome")
    
