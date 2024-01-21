a=[1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,]
same_element=False
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        same_element=True
        b=i
        l_half=a[0:b]
        r_half=a[b:]
        count_l_half=len(l_half)
        count_r_half=len(r_half)
   
        print("left half:",l_half)
        print("left half:",r_half)
        print("count of left half:",count_l_half)
        print("Count of right half:",count_r_half)
        break

else:
        print("There is no same elements in the list")

