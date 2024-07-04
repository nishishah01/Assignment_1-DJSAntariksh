#duplicate items are not allowed in sets. but in tuples and listd , duplicate items are allowed
#they are unordered, its not guranteed that you will get same sequence as the input
#indexing is not present

#1.
set1 = {True, 10, 40, 45, "Nishi", 40}
set1.add("Jigisha")
#set1.clear() #empties the set
set1.add((13, 34, 45))
print(set1)
set2 = {}
print(type(set2))  #dictionary
set3 = set()  #to create an empty set
