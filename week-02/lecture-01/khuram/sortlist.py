l1=[71,63,47,53,45]
print("l1 : " , l1)
for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]>=l1[j]:
           l1[i],l1[j]=l1[j],l1[i]

print("sort list : ",l1)           



