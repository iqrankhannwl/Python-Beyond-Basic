i  = [1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1]
def substring(lst):
    list=""
    list1=""
    for x in range(len(i)-1):
        if  lst[x] == lst[x+1]:
            list+=str(lst[x])
            for y in range(x+1,len(lst)-1):
                if i[y] == i[y+1] and y +1 <len(lst):
                    list1+=str(lst[y])
                else:
                    list1+=str(lst[y])
            break
        else:
            list+=str(lst[x])
    return list , list1
        
        
result,result1 = substring(i)
print("The result of first substring",result)
print("The result of second substring ",result1)
print("The length  of first substring",len(result))
print("The length of second substring ",len(result1))

