"""
Given n strings of brackets, determine whether each sequence of
brackets is balanced. If a string is balanced, print YES on a new
line; otherwise, print NO on a new line."""

def is_matched(expression):
    stack_list = []
    add = {'(':')','[':']','{':'}'}
    
    
    for i in range(len(expression)):
        if expression[i] in add.keys():
            
            stack_list.append(add[expression[i]])
        else:
            if (len(stack_list) == 0):
                return False
            brac = stack_list.pop()
            if expression[i] != brac:
                return False    
    if len(stack_list) != 0:
        return False
    return True
            
            

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

