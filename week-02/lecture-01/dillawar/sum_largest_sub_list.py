def sum_of_largest_sub_list(given_list):
    sub_list = []
    count = 0
    for i in range(len(given_list)-1):
        j = i+1
        if given_list[i] != given_list[j]:
            count += given_list[i]
        else:
            sub_list.append(count)
            count = 0
    return max(sub_list)


given_list = [1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0] 
print("Sum of largest sub-list is: ",sum_of_largest_sub_list(given_list))