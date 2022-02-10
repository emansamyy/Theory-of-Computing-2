# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 19:34:56 2021

@author: User
"""



  
 
tape = []  
x = int(input("enter x ; x is >=0 \n"))
counter = 0
final = 0
for i in range ((7*x)-1): #create fields of 1 depending on the value of x
    tape.append(1)
    
tape.append(0)
tape.append(1)
l = len(tape) -1
for j in range(len(tape)):
    if (tape[j]==1):
        
        continue
    else:
        tape[j]=1


  
   

for j in tape[::-1]:
    if (tape[j]==1):
        if (tape[j] == l):
            tape[j]=0
       
            

for n in tape[::-1]:
    if (tape[n]==1):
        counter+=1
    if (n==0):
        final=n


if (final == 0 and counter == ((x*1)+1)):      
    print("the function is computable")
else:
    print("the function is not computable")    
            
            

                
            
  
    

  

    