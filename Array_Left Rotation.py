"""
Given an array ofn  integers and a number,d, perform d
left rotations on the array.
Then print the updated array as a single line of space-separated integers.
"""
def array_left_rotation(a,n,k):
    # a = list, n = number of int, k = no of rotation
    # temp list will have first k-1 elem from the array a
    temp_list = a[:k]
    #from k to n, shift all the elements k steps behind
    for i in range(k,n):
        a[i-k] = a[i]
    j = 0
    #replace the last k-1 elements in the new array a
    # with the temp list.
    for i in range(-k,0,1):
        
        a[i] = temp_list[j]
        j += 1
    
    return a    
    

    
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
