# #1.STRINGS
name = "Nishi"
for i in name:
  print(i)

# #2. LIST
fruits = ["Mango", "Litchi", "Apple", "Watermelon"]
for fruit in fruits:
  print(fruit)
  for i in fruit:
    print(i)

# #3. RANGE
for k in range(5, 50, 2):  #(start,stop,increment)
  print(k)

#4. MOVIE RATING
movie_rating = {
    "Movie A": [1, 2, 3, 4, 5],
    "Movie B": [1, 2, 3, 4, 5],
    "Movie C": [1, 2, 3, 4, 5],
    "Movie D": [1, 2, 3, 4, 5],
}

for movie, ratings in movie_rating.items():
  average = sum(ratings) / len(ratings)
  print(f"{movie}: AVERAGE RATING IS {average}")

#5. count occurance of a character in a string
name = "Banana"
count = 0
for i in name:
  if (i == "a"):
    count = count + 1
print(count)

#6.Prime numbers from 1-20
for num in range(1, 21):
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        break
    else:
      print(num)

#7. Factorial of a number
a = int(input("enter a number:"))
fac = 1
for i in range(1, a + 1):
  fac = fac * i
print("the factorial of", a, "is", fac)

#8. Enumurate function

fruits=["mango","litchi","banana","apple","watermelon"]
for index,element in enumerate(fruits): #enumerate function returns index and element
  print(index,element)

#9. Nested for loop
for i in range(2):
  print(i)
  for j in range(5,10):
    print(j)

#10. break statement brings control out of loop and continue statement skips that particular iteration

#11. Fibonacci series
a=0
b=1
print(a)
print(b)
for i in range(1,10):
  c=a+b
  print(c)
  a=b
  b=c
