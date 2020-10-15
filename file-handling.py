#!/usr/bin/env python
# coding: utf-8
# Method 1
# In[2]:


f7  = open("C:\\Users\\singh\\Desktop\\movies.dat")
data = f7.read()
data = data.split("\n")
year = input("enter movie year")
genre = input("enter genre")
for i in data:
    i = i.split("::")
    if genre == "" :
        if year in i[1]:
            i = "\t".join(i)
            print(i)
    else :
        if year in i[1] and genre in i[2]:
            i = "\t".join(i)
            print(i)


# In[3]:
# Method 2

f7  = open("C:\\Users\\singh\\Desktop\\movies.dat")
data = f7.read()
data = data.split("\n")
result  = []
for i in data:
    c = i.split("::")
    d = c[2].split("|")
    e = c[1].split(" (")
    f = e[1].split(")")
    e = e[0:1]
    c = c[0:1]
    c.append(d)
    c.append(e)
    c.append(f[0])
    result.append(c)
print("0 for genre and 1 for year")
n = int(input())
movies = []
if n:
    year = input()
    for i in result:
        if year == i[3]:
            movies.append(i[2])
else:
    genre = input()
    for i in result:
        if genre in i[1]:
            movies.append(i[2])
print(movies)


# In[ ]:




