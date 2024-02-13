string = "12321"
def reverse(str):
    list=""
    for i in range(len(str)-1, -1, -1):
        list+=str[i]
    return list 

lab = reverse(string)
print(lab)
    

def palindrone(str):
    reverse1= reverse(str)
    return reverse1 == str


result = palindrone(string)
print(result)