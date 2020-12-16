# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def FindPairs(arr, k):
    count = 0
    for i in range(0,len(arr)):
        if  k - arr[i] in arr:
            count += 1
    if count > 0: 
        return True
    else:
        return False

A =[10,15,3,7]
n = 17
print(FindPairs(A,n))