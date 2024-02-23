# strings in python
#Date:22/02/2024
#Name: TKAY

city ="nairobi"
#assign each letter a number starting from 0

print(city[0]) #n
print(city[1]) #a
print(city[2]) #i
print(city[3]) #r
print(city[4]) #o
print(city[-1]) #b #-numbers reverse the string
print(city[-2]) #i



#convert to upper case

print(city)
print("\n")# prints a new line
print(city.upper())

name="TRACY KANYORA"
print(name)
print(name.lower()) # converts strings to lower case

town = "    Naivasha"
print("town")
print("\t") # prints new tab
print(town.strip())

# add two strings

f_name = "Rose"
s_name ="Nyambura"
full_name = f_name + s_name
print(full_name)


#replacing a character

fruit = "OrangeOOOOO"

print(fruit.replace("O"  , "Y"))



subject = "Physical,Sciences"

print(subject.split (",")) # what is in the bracket is what is used to split in ths case (,) you can use (.)etc


age = 18
height =1.2
print("I am{0} years old and {1} meters tall" . format(age ,height))  # if more than one use numbers btwn curly brackets starting from 0 and separate with


