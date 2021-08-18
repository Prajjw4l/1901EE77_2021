def meraki_helper(num): #this is parent function used to check the miraki number
    num = str(num) #converting the given number into string version of object
    length = len(num)  #calculating the length of string array
    for i in range(length-1):
        if abs(int(num[i+1])-int(num[i]))!=1: 
           #if the absolute diff between two adjacent number is!=1 then it is not miraki number else it is 
            print("NO - : " + num + " is not a Meraki Number")
            return False
    
    print("YES - : " + num + " is a Meraki Number")
    return True

#input list 
input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]

meraki = 0
for val in input:
    if meraki_helper(val): #if the above functions return true count it as miraki number 
        meraki+=1

print("The input list contains " + str(meraki) + " meraki numbers and " + str(len(input) - meraki) + " non-meraki numbers")
