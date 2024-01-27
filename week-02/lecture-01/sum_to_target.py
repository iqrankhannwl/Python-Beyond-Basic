
def sum_to_target(list,target):
    new_list = []
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[i]+list[j]==target:
                new_list.append(i) 
                new_list.append(j)
                print(new_list)
                break

sum_to_target([2,6,13, 3], 9)  #function call


print("jkgb b")








