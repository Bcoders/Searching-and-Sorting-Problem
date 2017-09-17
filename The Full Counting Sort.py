"""
In the previous challenge, you created a "helper array" that contains
information about the starting position of each element in a sorted array.
Can you use this array to help you create a sorted array of the original list?

Hint: You can go through the original array to access the strings. You can then use your helper array to help determine where to place those strings in the sorted array. Be careful about being one off.
"""

n = int(input().strip())
array1 = [] #with number
array2 = [] #with string

#fill array1 and array2 with given input
for i in range(n):
    num,string = input().strip().split()
    array1.append(num)
    if i <(n//2):
        array2.append('-')
    else:
        array2.append(string)
array1 = list(map(int, array1) )  #results = list(map(int, results))     
# find the length of bucket
max_value = max(array1)
len_bucket = max_value + 1

#create an array(bucket) that can include number from 0 to max_value.
#make another bucket, bucket1, which is a list containing list to store strings that come along with the numbers
bucket = [0]*(len_bucket)  
bucket1 = [[] for x in range(len_bucket)]

#iterate through the array1 to fill up bucket
#iterate to fill the list of bucket1 with strings associated with that index
for i in range(n): 
    bucket[array1[i]] += 1
    bucket1[array1[i]].append(array2[i])
        
sort_index = 0

#re arrange the array1 and array2
for i in range(len_bucket):
    string_index = 0
    while(bucket[i] > 0):
        array1[sort_index] = i
        #array2 can have list with two strings for one index. iterate through that index using string_index
        #string index starts with 0 and ends with number of same integers we have in array1 asssociated with that index
        array2[sort_index] = bucket1[i][string_index]
        bucket[i] -= 1
        sort_index += 1
        string_index += 1

for i in range (len(array1)):
    print(array2[i], end =' ')
    
    
        

