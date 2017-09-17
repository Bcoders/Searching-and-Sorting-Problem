"""
Given a sorted list with an unsorted number e in the rightmost cell,
can you write some simple code to insert into the array so that it
remains sorted?

Print the array every time a value is shifted in the array until
the array is fully sorted. The goal of this challenge is to follow
the correct order of insertion sort.
"""
n = int(input().strip())
a = list(map(int,input().strip().split()))

num = a[n-1]
found = False
i = n-1

for j in range(n-2,-1,-1):
    if a[j] > num:
        a[i]= a[j]
        i -= 1
        
        for item in a:
            print (item, end =' ')
            
        print()
 
    else:
        a[i] = num
        found = True
        for item in a:
            print (item, end =' ')
            
        break
        
if (not found):
    a[0]= num
    for item in a:
            print (item, end =' ')
