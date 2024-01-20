def sort_a_list(given_list):
    temp = None
    for i in range(len(given_list)):
        for j in range(len(given_list)-1):
            if given_list[i] < given_list[j]:
                temp = given_list[i]
                given_list[i] = given_list[j]
                given_list[j] = temp
    return given_list

given_list = [3,2,6,1,9,0]
print(sort_a_list(given_list))