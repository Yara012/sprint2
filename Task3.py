#!/usr/bin/env python
# coding: utf-8

# In[15]:


def swap_case(s):
    Output = ''
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower())
        elif(char.islower()==True):
            Output += (char.upper())
        else:
            Output += char
    return Output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print (result)


# In[17]:


def split_and_join(line):
    a= line.split(" ")
    a="-".join(a)
    return a
   
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print (result)


# In[ ]:


def print_full_name(first, last):
    print("Hello "+first+" "+last+"! You just delved into python.")
if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)


# In[ ]:


def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    string=''.join(l)
    
    return string

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new


# In[ ]:


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)] == sub_string):
            count += 1
    return count
    return

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count


# In[ ]:


if __name__ == '__main__':
    S = raw_input()
    print any(c.isalnum() for c in S)
    print any(c.isalpha() for c in S)
    print any(c.isdigit() for c in S)
    print any(c.islower() for c in S)
    print any(c.isupper() for c in S)
  


# In[ ]:



thickness = int(input()) # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# In[ ]:


import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# In[ ]:



from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    strlen = len(string)
    for i in range(0,strlen,k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))
# Merge the Tools in python - Hacker Rank Solution END
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# In[ ]:





# In[ ]:




