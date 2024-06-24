#1.
tup = (1, 5, 6, "green")
print(type(tup), tup)
print(tup[0])
print(tup[1])
if "green" in tup:
  print("present")
tup2 = tup[1:4]
print(tup2)
for i in tup:
  print(i)

#2.
countries1 = ("spain", "italy", "india", "england", "germany")
countries2 = ("india", "pakistan", "austrailia", "japan")
total = countries1 + countries2
print(total)

#3. Methods

l = (1, 3, 4, 5, 7, 4, 4, 4, 3, 2)
res = l.count(4)
ind = l.index(5)
print(ind)
print("count of 4 in l is:", res)
