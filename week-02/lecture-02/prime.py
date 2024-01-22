num = int(input("Please Enter the number"))

def prime(num):
    if num%2==0 or num%3==0 or num%5==0:
        print("The Number is not Prime Number")
    else:
        print("The Number is Prime Nmber")


result = prime(num)

        