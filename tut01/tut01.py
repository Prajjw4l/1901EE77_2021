def meraki_helper(n):
    n = str(n)
    l = len(n)
    for i in range(l-1):
        if abs(int(n[i])-int(n[i+1]))!=1:
            print("No - " + n + " is not a meraki number")
            return False
    print("Yes - " + n + " is a meraki number")
    return True

input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]

num_meraki = 0
for val in input:
    if meraki_helper(val):
        num_meraki += 1

print("The input list contains " + str(num_meraki) + " meraki numbers and " + str(len(input) - num_meraki) + " non-meraki numbers")
