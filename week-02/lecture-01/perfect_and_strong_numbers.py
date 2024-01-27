# ***************************Program no # 01 ****************************
# ***************************Perfect number ****************************
def perfect(number):   #function body
    b=0
    for i in range(1,number):
        if number%i == 0:
            b = b+i
    if number==b:
        print(number," is a Perfect number")
    else:
        print(number,"is not a perfect number")

perfect(28) #function call


# ***************************Program no # 02 ****************************
# ***************************Strong number ****************************
def strong_number(number): #function 
    a=number
    factorial=1
    add_factorial=0
    while a!=0:
        b=a%10
        for i in range(1,int(b)+1):
            factorial=factorial*i
        add_factorial=add_factorial+factorial
        factorial=1
        a=int(a/10)
    return add_factorial

number=145
add_factorial=strong_number(number) #function call
if number==add_factorial:           #compare to check number is srong or not
    print(number," is a strong number")
else:
    print(number,"is not a strong number")


