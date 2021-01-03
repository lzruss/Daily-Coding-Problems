# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

def largestSum(myList):
    sum = 0
    if len(myList) % 2 == 0:
        for i in myList[::-2]:
            #print(i)
            if not i < len(myList)/2:
                sum = sum + i
            
        for i in myList[::2]:
            #print(i)
            if not i >= len(myList)/2:
                sum = sum + i
            
    else:
        
        for i in myList[::2]:
            sum = sum + i
    return sum

sheesh = [5,1,1,5,6,5]
print (largestSum(sheesh))