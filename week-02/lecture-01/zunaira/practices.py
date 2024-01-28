a=[1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1]
same_element=False

for i in range(len(a)-1):
    if a[i]==a[i+1]:
        same_element=True
        b=i+1
        l_half=a[0:b]
        r_half=a[b:]
        sum_l_half=sum(l_half)
        sum_r_half=sum(r_half)

        print("left half:",l_half)
        print("right half:",r_half)
        print("Sum of left half:",sum_l_half)
        print("Sum of right half:",sum_r_half)
        break
if same_element:
    if sum_l_half>sum_r_half:
            squ=sum_l_half**2
            print("square of largest value=",squ)
    else:
            squa=sum_r_half**2
            print("square of largest value=",squa)

else:
    print("There is no same elements in the list")
