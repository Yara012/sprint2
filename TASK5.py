#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cmath;

num = complex(input())
z = complex(num)

print(cmath.polar(z)[0])
print(cmath.polar(z)[1])


# In[ ]:


import math

AB = int(input())
BC = int(input())

H = math.sqrt(AB**2 + BC**2)
H = H/2.0
adj = BC/2.0

Output = int(round(math.degrees(math.acos(adj/H))))

Output = str(Output)

print(Output+"°")


# In[ ]:


for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i - 1)//9)**2)


# In[ ]:


a = int(input());
b = int(input());
print(a//b);
print(a%b);
print(divmod(a,b));


# In[ ]:


A = int(input())
B = int(input())
C = int(input())
D = int(input())

print((A**B)+(C**D))


# In[ ]:


a = int(input())
b = int(input())
m = int(input())

print(pow(a,b))

print(pow(a,b,m))

