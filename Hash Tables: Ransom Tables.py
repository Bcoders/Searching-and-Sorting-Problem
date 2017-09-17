"""
Given the words in the magazine and the words in the ransom note, print Yes
if he can replicate his ransom note exactly using whole words from
the magazine; otherwise, print No.
"""
def ransom_note(magazine, ransom):
    a = magazine
    b = ransom
    dict_1 = {}
    num = 0
    for item in a:
        if item not in dict_1.keys():
            dict_1[item] = 1
        else:
            dict_1[item] += 1
            
    for item in b:
        if item in dict_1.keys():
            dict_1[item] -= 1
            if dict_1[item] == 0:
                del dict_1[item]
        else:
            return False
            
    
     
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
