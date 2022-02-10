# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 16:01:54 2021

@author: User
"""


stack = []
aCount = 0
bCount = 0
cCount = 0
dCount = 0

str = input("enter a string to be the input \n")
stack.append("$")
for i in range(len(str)):
    if (str[i] == "a"):
        stack.append("a")
        aCount = aCount+1
    elif (str[i] == "b"):
        bCount = bCount+1
        if (len(stack)!=0 and len(stack)!=1):
            stack.pop()
    elif (str[i] == "c"):
        cCount = cCount+1
        continue
    
        
stack.pop()        
if  ((len(stack)==0 or stack.pop() == "$")and (aCount == bCount) and (cCount  == 1)):
    print("acceptable")

else:
    stack.append("$")
    for j in range(len(str)):
        if (str[j] == "a"):
            aCount = aCount+1
            stack.append("a")
            stack.append("a")
        elif (str[j]== "b"):
            bCount = bCount+1
            if (len(stack)!=0 and len(stack)!=1):
                
                stack.pop()
        elif (str[j]== "d"):
            dCount = dCount+1
            continue
        
    stack.pop()  
    if ((len(stack)==0 or stack.pop() == "$") and (bCount == (2*aCount) and (dCount ==1))):
        
        print("acceptable")
    else:
        print("not acceptable")
        
            
            
            
            
            
        
        
    
    
    
    
   
    
    
    
    