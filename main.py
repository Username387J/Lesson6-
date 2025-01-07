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

#Set operations
# 01) Union
# 02) Intersection
# 03) Difference
# 04) Symmetric difference

print("\n")

a = {1, 2, 3, 4, 5,}
b = { 4, 5, 6, 7, 8}

#Union means addition of sets
print("Set a : ",a)
print("Set b: ",b)
print(a.union(b))#the same as print(a | b)

#Intersection means the common elements between two sets
print("\n")
print("Intersection of two sets")
print(a.intersection(b))
print(a & b)

#Gives only the unique values in the first value; Difference of A and B is the elements that exist in a but not b
print("\n")
print("difference of A and B")
print(a.difference(b))
print(a - b)

#Difference of B and a is the elements that exist in b but not a
print("\n")
print("difference between b and a")
print(b.difference(a))
print(b - a)

#Symmetric difference is the union of sets - intersection of sets
#removes common terms
print("\n")
print("Symmetrical difference between a and b")
print(a.symmetric_difference(b))
print(a ^ b)