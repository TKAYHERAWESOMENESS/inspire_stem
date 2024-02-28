# helps to model physical items
#set of key-value pairs
#use curly brackets 
#they are mutable
# key is before : value is after colon before comma

My_laptop = {"make" : "HP", "weight" : "1.2", "colour": "silver", "year" : "2020"}

print (My_laptop["make"])
print (My_laptop["colour"])
print (My_laptop["weight"])
print (My_laptop["year"])

My_laptop["colour"]= "red"
My_laptop["year"]="2016"

My_laptop["size"] = "1200mm x 600mm"
print(My_laptop)


del My_laptop ["colour"]
print(My_laptop)
"""

for key,value in My_laptop .items():
    print(key)
    print("\n")
    print(value)
"""



# copying one dictionary into another

siz_laptop = My_laptop.copy()
print(siz_laptop)





my_car = {"make" : "ferrari" , "type" :  "urus" , "colour" : "purple" ,"year" : "2024"}
print(my_car["make"])
print(my_car["type"])
print(my_car["colour"])
print(my_car["year"])


bro_car= my_car.copy()
print(bro_car)



