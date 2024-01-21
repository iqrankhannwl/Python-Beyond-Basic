# ***************************Check number is  Palindrome or not ****************************
value=96690
reverse = 0
temp = value
while temp/10!=0:
    b=temp%10
    reverse = (reverse*10)+b
    temp=int(temp/10)
if value==reverse:
    print("The number is palindrome")
else:
    print("The number is not palindrome")

# ***************************Check String is  Palindrome or not ****************************
string = "hellowwolleh"
a=len(string)-1
reverse = str()
while a>=0:
    reverse = reverse + string[a]
    a=a-1
print(reverse)
if string==reverse:
    print("The string is palindrome")
else:
    print("The string is not palindrome")

# ***************************Check number is Prime or not ****************************
value=13
for i in range(2,value):
    if (value % i)==0:
        print("The number is not Prime")
        break
if value==i+1:
    print("The number is Prime")


        

