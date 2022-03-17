#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Task1


# In[3]:


#Say "Hello, World!" With Python
print("Hello, World!")


# In[4]:


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if (n%2!=0):
        print ("Weird")
        
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        elif n>20:
            print("Not Weird")            


# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)


# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(int(a/b))
    print(float(a/b))


# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(int(a/b))
    print(float(a/b))


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    
for i in range(n):
    i=i**2
    print (i)


# In[ ]:


def is_leap(year):
    leap = False
    
    if (year %400==0):
        leap =True 
    elif(year%100==0):
        leap = False 
    elif (year%4==0):
        leap= True
            
    
    return leap

year = int(input())
print(is_leap(year))


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    
    i=1
    while i<=n:
        print(i,end="")
        i=i+1

