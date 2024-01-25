#welcome to python coding

#PROBLEM:
#Given an array of integers nums and an integer target, return indices 
#of the two numbers such that they add up to target.

nums=[1,4,11,8,18,6]
print("Given list:",nums)
target=int(input("Enter the target:"))
def two_sum(num,tar):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return[i,j]
                
print("The required indices for target:",two_sum(nums,target))

