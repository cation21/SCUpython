import math
x = 9.61
print(math.pi)
print(math.e)
result = math.sqrt(x)
result1 = math.ceil(x)
result2 = math.floor(x)

#round() function to round off the result
result3 = round(math.pi,2)
print(result3)

#Hypotenuse of a right angled triangle

a = float(input("a:"))
b = float(input("b:"))
#c = pow(a,2) + pow(b,2)
#Hypotenuuse = math.sqrt(c)
#print(Hypotenuuse)
c = math.sqrt(pow(a,2) + pow(b,2))
print(c)

#if-else statements
#Example of Python weight converter

weight = float(input("Enter your weight"))
unit = input("Kilo(K) or Pound(P)")

if unit == "K":
     weight *= 2.205
     unit = "Lbs"
elif unit == "L":
     weight /= 2.205
     unit = "Kgs"
else:
    print(f"Input valid unit K or L")

print(f"Converted weight is: {weight} {unit}")

