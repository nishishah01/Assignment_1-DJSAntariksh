#1. write a function to calculate and return square of a number
def calculateSquare(num):
  return num * num


calculateSquare(4)
print(calculateSquare(4))


#2. Create a function that takes two numbers as parameters and returns their sum
def calculateSum(num1, num2):
  return num1 + num2


ans = calculateSum(3, 5)
print(ans)


#3. Write a functions multiply that multiplies two numbers,but can also accept and mulltiply strings
def calculateProduct(num1, num2):
  return num1 * num2


a1 = calculateProduct(3, 5)
a2 = calculateProduct('n', 4)
a3 = calculateProduct(4, 'n')
print(a1)
print(a2)
print(a3)


#4. Create a function that returns both the area and circumference of a circle given its radius
def Circle(rad):
  pi = float(3.14)  #we can also use Math.pi and import Math
  area = float(pi * rad * rad)
  circumference = float(2 * pi * rad)
  print(float("%0.2f" % area))  #to get ans to 2 decimal places
  print(circumference)


Circle(3)


#5. Write a function that greets a user. If no name is provided, it should greet with a default name.
def Greeting(name="Nishi"):  #default name
  return "Hello," + name + "!"


print(Greeting("Jigi"))
print(Greeting())  #if no name is provided, it will print default name

#6. Create a lambda function to find the cube of a number
cube = lambda x: x**3
print(cube(3))


#7. Write a function that takes variable number of arguments and returns the sum of all arguments
def calculateSum(
    *args):  #asterisk signifies that it can take multiple of arguments
  sum = 0
  for i in args:
    sum = sum + i
  return sum


ans = calculateSum(1, 2, 3, 4, 5, 6)
print(ans)


#8. Create a function that accepts any number of arguments and prints them in the format "key:value"
def printing(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}:{value}")


printing(name="Nishi", age=20)
printing(name="Nishi", age=20, Field="computer engineering")
printing(name="nishi")

#it allows to print any number of key value pairs.


#9. Write a generator function that yields even numbers upto a specified limit.
def even(limit):
  for i in range(2, limit + 1, 2):
    yield i  #it returns a value but also keeps the original value and also keeps a track of its state , ki ab tak kitne iterations hue hai.


for num in even(20):
  print(num)


#10. Create a recursive function to calculate the factorial of a number
def factorial(n):
  if n == 0:
    return 1
  else:
    return (n) * factorial(n - 1)


res = factorial(5)
print(res)


#11. Write a function that takes a list of numbers and returns the maximum number
def calculateMaximum(list):
  for i in list:
    max = list[0]
    if i > max:
      max = i
  return max


lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(calculateMaximum(lis))

#lecquestion1
even_odd = lambda x: ("Even" if x % 2 == 0 else "Odd")
print(even_odd(int(input("Enter a number:"))))
