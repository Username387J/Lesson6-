list =[1,1,3,3,2,7,7,7,]
myset = set(list)
print(myset)

#CHeck if a number is in the set
if 9 in myset:
    print("Number exists in set")
else:
    print("Number does not exist in set")

#add values
set1= set([])
set1.add(100)
set1.add(386)
set1.add(718)
set1.add(198)
set1.add(683)

print(set1)

set1.remove(100)
print(set1)

#set1.remove(500)
set1.discard(500)
print(set1)