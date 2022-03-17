#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input())

countries = set()

for i in range(N):
    countries.add(input())

print(len(countries))


# In[ ]:


n = int(input())
s = set(map(int, input().split()))
num = int(input())
for i in range(num):
    ip = input().split()
    if ip[0]=="remove":
        s.remove(int(ip[1]))
    elif ip[0]=="discard":
        s.discard(int(ip[1]))
    else :
        s.pop()
print(sum(list(s)))


# In[ ]:


N1 = int(input())
storage1 = set(input().split());

N2 = int(input())
storage2 = set(input().split());

storage3 = storage1.union(storage2)

print(len(storage3))


# In[ ]:


N1 = int(input())
storage1 = set(input().split())

N2 = int(input())
storage2 = set(input().split())

storage3 = storage2.intersection(storage1)

print(len(storage3))


# In[ ]:


N= int(input())
SET_N = set(map(int, input().split()))

B = int(input())
SET_B = set(map(int, input().split()))

NEW_SET = SET_N.difference(SET_B)
print(len(NEW_SET))


# In[ ]:


n=int(input())
setn =set(map(int, input ().split ()))
l=int(input())
setl=set(map(int,input ().split ()))
print (len(setn.symmetric_difference (setl)))


# In[ ]:


len_set = int(input())

storage = set(map(int, input().split()))

op_len = int(input())

for i in range(op_len):
    operation = input().split()
    if operation[0] == 'intersection_update':
        temp_storage = set(map(int, input().split()))
        storage.intersection_update(temp_storage)
    elif operation[0] == 'update':
        temp_storage = set(map(int, input().split()))
        storage.update(temp_storage)
    elif operation[0] == 'symmetric_difference_update':
        temp_storage = set(map(int, input().split()))
        storage.symmetric_difference_update(temp_storage)
    elif operation[0] == 'difference_update':
        temp_storage = set(map(int, input().split()))
        storage.difference_update(temp_storage)
    else :
        assert False

print(sum(storage))


# In[ ]:


k= int (input ())
roomnolist=list(map(int, input ().split()))
captain_room=(sum(set(roomnolist))*k-sum(roomnolist))//(k-1)
print(captain_room) 


# In[ ]:


for i in range(int (input())):
    a=int(input())
    seta=set(map(int,input().split()))
    b=int(input())
    setb=set(map(int,input().split()))

    if len (seta-setb)==0:
        print("True")
    else:
      print("False")    


# In[ ]:


seta=set(input().split())
N=int(input())
output=True
for i in range(N):
    setb=set(input().split())
    if not setb.issubset(seta):
        output=False
    if len(setb)>=len(seta):
        output= False 
        
print(output)        
    

