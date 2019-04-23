age = 13
print ("I am " + str(age) + " years old!")
# I am 13 years old!

number1 = "100"
number2 = "10"

string_addition = number1 + number2
print(string_addition)
# 10010
ini_addition = int(number1) + int(number2)
print(ini_addition)
# 110

string_num = "7.5"
# print (int(string_num))
#7 according to codeacdemey but error here on atom????
print(float(string_num))
#7.5

float_1 = 0.25
float_2 = 40.0

product = float_1 * float_2
big_string = "The product was " + str(product)

skill_completed = "Python Syntax"

exercises_completed = 13
points_per_exercise = 5
point_total = 100

point_total += exercises_completed * points_per_exercise

#The amount of points for each exercise may change, because points don't exist yet
print("I got "+str(point_total)+" points!")
