"""
Challenge
Given a list of integers, can you count and output the number
of times each value appears?
"""

n = int(input().strip())
arr = list(map(int, input().strip().split()))

max_value = max(arr)

buckets = [0]*(max_value+1) #create an array that can include number from 0 to max_value. 

for i in range(n):
    buckets[arr[i]] += 1
    
for item in buckets:
    print(item, end = ' ')
    
