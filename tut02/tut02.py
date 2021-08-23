def get_memory_score(input_nums):
    arr=[]
    count=0
    for i in range(len(input_nums)):
        if input_nums[i] in arr:
           count = count+1
        elif(len(arr)>4):
            arr.pop(0)
            arr.append(input_nums[i])
        else:
            arr.append(input_nums[i])    
    return count
        

input_nums = [3, 4, 3, 0, 7, 4, 5, 2, 1, 3]
list=[]
flag = False
for i in range(len(input_nums)):
        if(str(input_nums[i]).isdigit()):
            continue
        else:
            flag = True
            list.append(input_nums[i])
if(flag):    
    print("Please enter a valid input list.")
    print("Invalid inputs detected : ",list)
else:
    print("Score :", get_memory_score(input_nums))
