#
apple=4
if(apple>4):
  print("correct")
else:
  print("incorrect")

#nested if

a=int(input("enter a number: "))
if(a<0):
  print("number is negative")
elif(a>0):
  if(a<=10):
    print("number is between 1-10")
  elif(a>10 and a<=20):
    print("number is between 11-20")
  else:
    print("number is greater than 20")
else:
  print("number is zero")



#time module
import time
currentTime=time.strftime('%H:%M:%S')
print(currentTime)
currentTime=time.strftime( '%H')
print(currentTime)
currentTime=time.strftime('%M')
print(currentTime)
currentTime=time.strftime('%S')
print(currentTime)

#MATCH_CASE STATEMENTs
# a=int(input("enter the value of a:"))
# match a:
#   case 0:
#   print("a is zero")
#   case 4:
#   print("a is 4")
#   case _:
#   print(a)
