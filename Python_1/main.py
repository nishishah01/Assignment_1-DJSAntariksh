#implicit type casting
x=input("enter the value of x:")
y=input("enter the value of y:")
print(int (x)+int(y))

#without type casting
x=input("enter the value of x:")
y=input("enter the value of y:")
print( (x)+(y))

#strings
name="Nishi"
sentence='''She said,
"how are you?" I said,
"I am fine"'''
# print(sentence)
for character in sentence:
  print (character) #prints according to index

#slicing
name="Nishi"
length=len(name)
print({name},"is a", {length}, "letter word")
print(name[0::])
names=("nishi,jigisha,kriya")
print(len(names))
#len() finds the length of the string
print(name[0:-3]) #-3 means length of name-3
print(name[-4:-2])

#STRUNG_METHODS
vegetable = "Carrot $$$"
print(vegetable.upper())
print(vegetable.lower())
print(vegetable.rstrip("$"))  #removes trailing characters
print(vegetable.replace("Carrot", "Potato"))
print(vegetable.split(" ")) #converts string into a list
print(vegetable.center(50))
print(vegetable.count("$"))#counts the number of times $ occurs
print(vegetable.endswith("t")) #boolean method i.e.returns true or false
sentence="myluckynumberis 9"
print(sentence.isalnum()) #returns true only if the entire string only consists of A-Z,a-z,0-9. If any special characters or punctuations are present, then it returns false.
print(vegetable.swapcase())
str1="World Health Organisation"
print(str1.istitle())
str2="World health organisation"
print(str2.istitle())
