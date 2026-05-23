#SECTION 2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("addition:",num1 + num2)
print("subtraction:",num1 - num2)
print("multiplication:",num1 * num2)
print("division:",num1/num2)

#Circle
radius = float(input("enter radius: "))
circle_area = 3.142 * radius * radius
print("area of circle:", circle_area)

#Rectangle
length = float(input("enter length: "))
width = float(input("enter width: "))
rectangle_area = length * width
print("area of rectangle:", rectangle_area)

#Triangle
base = float(input("enter base: "))
height = float(input("enter height: "))
triangle_area = 0.5 * base * width
print("area of triangle:", triangle_area)


number = int(input("enter a number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")

score = float(input("enter score: "))
total = float(input("enter total marks: "))
percentage = (score/total) * 100
print("percentage:", percentage, "%")


#BMI
weight = float(input("enter weight in kg: "))
height = float(input("enter height in meters: "))
bmi = weight/(height**2)
print("BMI = ",bmi)

#POWER
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
print("power:", num1 ** num2)
print("modulus:", num1 % num2)


