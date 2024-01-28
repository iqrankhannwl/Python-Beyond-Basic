#    ******************Program for Assending order*********************
value = [8,4,6,3,2,0,5,6,5]
# outer loop
for i in range(len(value)-1):
#  inner loop
    for j in range(i+1,len(value)):
        if value[i]>value[j]:
#  swaping 
            temp = value[i]
            value[i] = value[j]
            value[j] = temp

print("Values of list in Assending order" ,value)

# ***************************Program no # 02 ****************************
list = [1,0,1,0,1,0,1,1,5,1,0,1,0,1,8,0,1,0,1,8,1,0,0,8,7] 
start_range=0
count_lists_values=[]
print("\nLists \n")
for index in range(len(list)-1):
# where this condition will be true single list convert into multiple lists depend upon same values
    if list[index]==list[index+1]:
        j=index+1
        print(list[start_range:j])
        condition = j-start_range
        start_range = j
# append values to check in last which list is large
        count_lists_values.append(condition)
#    list that left after the same values in last
print(list[start_range:len(list)])
condition = len(list)-start_range
count_lists_values.append(condition)
# which list is large
large_list = 1
for i in range(len(count_lists_values)-1):
    if count_lists_values[i]<count_lists_values[i+1]:
        large_list = i+2
print("\nLargest list is list number ", large_list)




# ***************************Program no # 03 ****************************
list = [1,0,1,0,1,0,1,1,5,1,0,1,0,1,0,0,1,0,1,8,1,0] 

start_range=0
summation =[]
print("\nLists \n")
for index in range(len(list)-1):
# where this condition will be true single list convert into multiple lists depend upon same values
    if list[index]==list[index+1]:
        j=index+1
        print(list[start_range:j])
# take sum of list according to given range
        sum_of_list = sum(list[start_range:j])
# append sum in list to check  which list has greatest sum
        summation.append(sum_of_list)   
#  as one list complete other list will be start so it will be start where first list end 
        start_range = j
#    list that left after the same values in last
print(list[start_range:len(list)])
sum_of_list = sum(list[start_range:len(list)])
summation.append(sum_of_list) 

# which list is large
maximum = 1
greatest_sum = summation[0]
for i in range(len(summation)-1):
    if summation[i]<summation[i+1]:
        greatest_sum = summation[i+1]
        maximum = i+2
print("\nGreatest sum is ", greatest_sum,"of list number",maximum)
print("And squre is ", greatest_sum*greatest_sum)