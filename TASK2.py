#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
output = list(student_marks[query_name])    
per = sum(output)/len(output);
print("%.2f" % per);   


# In[ ]:


if __name__ == '__main__':
    N = int(input())
    # Lists in Python - Hacker Rank Solution START
    Output = [];
    for i in range(0,N):
        ip = input().split()
        if ip[0] == "print":
            print(Output)
        elif ip[0] == "insert":
            Output.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "remove":
            Output.remove(int(ip[1]))
        elif ip[0] == "pop":
            Output.pop()
        elif ip[0] == "append":
            Output.append(int(ip[1]))
        elif ip[0] == "sort":
            Output.sort()
        else:
            Output.reverse()


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    # Tuples in Python - Hacker Rank Solution START
    t = tuple(integer_list)
    print(hash(t));

