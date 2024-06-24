#Basic
marks = [10, 30, "Nishi", True]
print(marks)
print(marks[-2])
print(marks[0])
if "Nishi" in marks:
  print("Yes")
else:
  print("No")

#List Comprehension
list = [i for i in range(20)]
print(list)

names = ["Nishi", "Nisha", "Nishant", "Nishali"]
nameswith_t = [item for item in names if "t" in item]
print(nameswith_t)

#Methods in List
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 2]
n.sort()
print(n)
print(n.reverse())
print(n.index(3))
print(n.append(11))
m = n.copy()  #copies the n list and stores in m
m[0] = 7
print(m)
