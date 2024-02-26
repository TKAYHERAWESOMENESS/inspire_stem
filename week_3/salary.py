# This is a program that calculates condtional salary increments
# Date: 26/02/2024
# Name:Tracy Kanyora


salary = int(input("Enter salary"))
if salary is < 100000 :
    new_salary = (1.3 * salary)
    print("The new salary:" , new_salary)

elif salary is > 100000 and < 150000 :
    new_salary = (1.15 * salary)
    print("The new salary:" , new_salary)

elif salary is > 150000 :
    new_salary = (1.05 * salary)
    print("The new salary" , new_salary)






