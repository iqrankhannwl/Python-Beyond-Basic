list = "This is ehsas lab 1234 and its also benefits"
def check(str):
    num=""
    string=""
    for i in list:
        if i.isdigit():
            num+=i
        else:
            string+=i
    return num,string
    

result1,resuk2 =check(list) 
print(result1)
print(resuk2)