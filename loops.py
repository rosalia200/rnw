"""
for loop repeats a task until max is reached
while loop repeats a task until a conditon is false



"""
vallist =[]
for val in range (0,10):
    vallist.append(val)
print(vallist)

print(myval)

vallist2 =[]
for val in range (0,10):
    if val%2==0 and not val%3==0:
     vallist2.append(val)
newlist =["john","ann","lizzo"]
for myval in newlist :
    print(myval)
print(vallist2)


i=0
while i <=10:
    print(i)
    i =i +1
count =object
while count<len(newlist):
    print(newlist[count])
    count+=1