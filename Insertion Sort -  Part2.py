"""
In this challenge, don't print every time you move an element.
Instead, print the array after each iteration of the
insertion-sort, i.e., whenever the next element is placed at its
correct position.
"""

n = int(input().strip())
a = list(map(int, input().strip().split()))
i = 0

for j in range(1,n):
    num = a[j]
    i = j-1
    while(num < a[i] and i >-1):
        a[i],a[i+1]= a[i+1],a[i]
        i -= 1
    for item in a:
        print (item, end = ' ')
    print()


