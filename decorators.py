#a decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is known as decorated function.
#1.
def decor(fx):

  def mfx():
    print("Good Morning, I am Nishi")
    fx()
    print("Good Afternoon, I am Jigisha")

  return mfx


@decor
def important():
  print("I am in between")


important()


# #2.
def greet(fx):

  def mfx(*args, **kwargs):
    print("Good Morning, I am Nishi")
    fx(*args, **kwargs)
    print("Good Afternoon, I am Jigisha")

  return mfx


def add(a, b):
  print(a + b)


greet(add)(1, 3)

#3.
import logging


def log_function_call(func):

  def decorated(*args, **kwargs):
    logging.info(f"Calling {func.__name__} with args={args},kwargs={kwargs}")
    result = func(*args, **kwargs)
    logging.info(f"{func.__name__}returned {result}")
    return result

  return decorated


@log_function_call
def my_function(a, b):
  return a + b


# Output:
# INFO:root:Calling my_function with args=(2, 3), kwargs={}
# INFO:root:my_function returned 5


#4.
#decorator chaining (referred gfg)
def decor1(func):

  def inner():
    x = func()
    return x * x

  return inner


def decor(func):

  def inner():
    x = func()
    return 2 * x

  return inner


@decor1
@decor
def num():
  return 10


@decor
@decor1
def num1():
  return 20


print(num())
print(num1())

#5.
