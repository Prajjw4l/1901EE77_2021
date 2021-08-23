def get_memory_score(input_nums):
    arr=[]
    count=0
    list=[]
    flag = False

    for i in range(len(input_nums)):
        if(str(input_nums[i]).isdigit()): #if non- digit detected then it is invalid 
            continue
        else:
            flag = True
            list.append(input_nums[i])
    if(flag):    
        print("Please enter a valid input list.")
        print("Invalid inputs detected : ",list)
        exit()
    
    for i in range(len(input_nums)):
        if input_nums[i] in arr:
           count = count+1
        elif(len(arr)>4): #if the length of the arr is greater then 4 that is it can hold max 5 element
            arr.pop(0)
            arr.append(input_nums[i])
        else:
            arr.append(input_nums[i])    
    return count
        

input_nums = [3, 4, 3, 0, 7, 4, 5, 2, 1, 3]

print("Score :", get_memory_score(input_nums))
print("1. Score:", get_memory_score([3, 4, 1, 6, 3, 3, 9, 0, 0, 0]))
print("2. Score:", get_memory_score([1, 2, 2, 2, 2, 3, 1, 1, 8, 2]))
print("3. Score:", get_memory_score([2, 2, 2, 2, 2, 2, 2, 2, 2]))
print("4. Score:", get_memory_score([1, 2, 3, 4, 5, 6, 7, 8, 9]))
nums = [7, 5, 8, 6, 3, 5, 9, 7, 9, 7, 5, 6, 4, 1, 7, 4, 6, 5, 8, 9, 4, 8, 3, 0, 3]
print("5. Score:", get_memory_score(nums))
