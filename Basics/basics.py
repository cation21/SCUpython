print("Hello Python")

#variables are containers for values whether real or abstract
#(String, integer, boolean, float)

my_name = "Ananya"
#classic declaration 

dob = 21 #int declaration
price_of_onions = 69.999 #float declaration

#printing using an f-string
print(f"My name is {my_name} and my date of birth is {dob}")

#other ways of printing the same thing without an f-string
print("My name is {}, my dob is {}".format(my_name,dob))
print("My name is %s, my dob is %d"%(my_name, dob))


#Typecasting = process of converting one datatype to another
#Use case = Specially used in managing user input
#str(),int(),bool(),float()

#check = bool(name)

#input() function prompts user to enter, returns entered data in string
name = input("What is your name:")
#age = input("What is your age:")

#Now to use age as integer
#age = int(age)

#You can directly typecast
age = int(input("What is your age:"))
age = age + 1
print(age)

#Handling Arithematic and Math
friends = 10
#friends = friends + 1
#friends += 1
#friends = friends * 2
#friends *= 2
#friends = friends/2
#friends /= 2
remainder = friends%2
print(remainder)