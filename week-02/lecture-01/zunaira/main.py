a=[1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,]

if a[0]==a[1]:
    b=len(a) // 2
    l_half=a[0:b]
    r_half=a[b:]
    count_l_half=len(l_half)
    count_r_half=len(r_half)
   
    print("left half:",l_half)
    print("left half:",r_half)
    print("count of left half:",count_l_half)
    print("Count of rifht half:",count_r_half)

else:
    print("There is no same elements in the list")

