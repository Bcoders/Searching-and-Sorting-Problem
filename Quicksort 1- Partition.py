"""
Given ar and p = ar[0], partition ar into left, right, and equal using the
Divide instructions above. Then print each element left in followed by each
element in equal, followed by each element in on a single line.
Your output should be space-separated.
"""

n = int(input().strip())
arr = list(map(int, input().strip().split()))

pivot = arr[0]
j = 1
for i in range(1,n):
    if arr[i] < pivot:
        arr[i],arr[j] = arr[j],arr[i]
        j += 1
arr[j-1],arr[0] = arr[0],arr[j-1]  

for item in arr:
    print(item, end = ' ')
