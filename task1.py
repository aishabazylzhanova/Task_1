import itertools
mylist=[]
x=input()
for i in range(len(x)):
    if x[i]!="," and x[i]!=" ":
        mylist.extend(x[i])
print( list(itertools.permutations(mylist)))
