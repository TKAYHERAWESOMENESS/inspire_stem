
# for loop in list

friends = ["Rose" , "Sheila" , "Claudia" , "Blessing" ,"Marvin"]
for friend in friends:
    print(friend)


enemies = friends[:]    # This is how to copy one list into another
print(enemies)

# slicing the list to get part of it
fruits = ["kiwi" , "mango" , "guava" ,"grapes" "strawberry" "blueberry"]
print(fruits[0:3])
del fruits[0] # deletes fruit
print (fruits)


squares = [] #initialises an empty list
for x in range (0,11):
    squares.append(x**2)

print(squares)