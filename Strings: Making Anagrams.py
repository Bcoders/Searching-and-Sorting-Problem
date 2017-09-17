"""
Given two strings,a and b , that may or may not be of the
same length, determine the minimum number of character
deletions required to make a and b anagrams. Any characters can be
deleted from either of the strings.
"""

def number_needed(a, b):
    dict_1 = {}
    num = 0
    #put all the characters from first input in a dict
    for item in a:
        if item not in dict_1.keys():
            dict_1[item] = 1
        else:
            dict_1[item] += 1

    #iterate through the next string and del the char from
    # dict if it is in dict1. If not add it to num
            
    for item in b:
        if item in dict_1.keys():
            dict_1[item] -= 1
            if dict_1[item] == 0:
                del dict_1[item]
        else:
            num += 1
            
    for item in dict_1:
        num += dict_1[item]
     
    return num
            
            
        

a = input().strip()
b = input().strip()

print(number_needed(a, b))
