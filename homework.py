set1 = set([])
numberoftimes = int(input("How many values do you intend to add?"))

for i in range (numberoftimes) :
    num = int(input("Insert the variable: "))
    set1.add(num)

print(set1)

set2 = set([])
number = int(input("How many values?"))

for i in range(number):
    nom = int(input("Inset the variable: "))
    set2.add(nom)

print(set2)
print("if set 1 is",set1,", and set 2 is",set2,"then the symmetric difference would be",set1.symmetric_difference(set2),",")
print("the union of both sets would result in",set1.union(set2),",")
print("the difference between the 1st and second set would be",set1.difference(set2),"thus vice versa would be equal to",set2.difference(set1))
print("and the intersection would result in", set1.intersection(set2))
