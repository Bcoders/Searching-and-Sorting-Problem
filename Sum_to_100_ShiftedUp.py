def operation(str1, str2, set1):
    
    str1 = str1+str2[0]
    str2 = str2[1:]
    
    sign = ['+','-','']
    for item in sign:
        str3 = str1+item
        str4 = str3+str2
        if str4[-1] == item:
            break
        
        add = eval(str4)
       
        if add == 100:
            if str4[0] == '+':
                set1.add(str4[1:])
            else:
                set1.add(str4)
        operation(str3,str2,set1)

def main(string):
    set1 = set()
    item = ['+','-',''] 
    str2 = string
    str1 =''
    for items in item:
        operation(items+str1, str2, set1)
    print(set1)
    print(len(set1))
main('123456789')
    
