# ***************************Check number is  Palindrome or not ****************************
def palindrome(value):
    temp = value
    reverse = 0
    while temp/10!=0:
        b=temp%10
        reverse = (reverse*10)+b
        temp=int(temp/10)
# compare to check palindrome or not
    if value==reverse:
        print("The number is palindrome")
    else:
        print("The number is not palindrome")
palindrome(96690)


# ***************************Check String is  Palindrome or not ****************************
def string_palindrome(string):
    a=len(string)-1
    reverse = str()
#  loop to take reverse value
    while a>=0:
        reverse = reverse + string[a]
        a=a-1
# compare to check palindrome or not
    if string==reverse:
        print("The string is palindrome")
    else:
        print("The string is not palindrome")
string_palindrome("abba")

# ***************************Check number is Prime or not ****************************
    # function initilization
def prime(value):
    if value!=2: 
        for i in range(2,value):
            if (value % i)==0:
                print("The number is not Prime")
                break
        if value==i+1:
            print("The number is Prime")
    else:
        print("The number is Prime")
# function call
prime(8)

        
