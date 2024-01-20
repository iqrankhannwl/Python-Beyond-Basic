def find_largest_sub_list(given_list):
    sub_list = []
    sub_lists = []
    for i in range(len(given_list)-1):
        j = i+1
        if given_list[i] != given_list[j]:
            sub_list.append(given_list[i])
        else:
            sub_lists.append(sub_list)
            sub_list=[]
    return sub_lists


given_list = [1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0] 
print(find_largest_sub_list(given_list))