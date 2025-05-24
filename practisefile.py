# # Day 53
# def cube(x):
#     return x*x*x

# print(cube(27))
# print(cube(89))

# l= [1,2,4,6,4,3]
# newl= []
# for item in l:
#     newl.append(cube(item))

# print(newl)

# print("Done with the previous program.")

# newl= list(map(cube, l))
# print(newl)

# print("Done with the program")

# # Filter

# def filter_function(a):
#     return a>4

# newnewl= list(filter(filter_function, l))
# print(newnewl)

# # Map

# l=[74,85,96,45,65,78,98,14,35,62,61,39,99,121,845]
# newl= list(map(lambda x: x*x*x,l))
# print(newl)
# print("Done with the previous program.")

# # Filter
# l=[74,85,96,45,65,78,98,14,35,62,61,39,99,121,845]
# def filter_function(a):
#    return a>80

# newnewl= list(filter(filter_function,l))
# print(newnewl)

# print("Done with the previous program.")

# Class 57

# class person:
#     name= "Harry"
#     occupation= "Software Developer"
#     networth= f"{100} Dollars!!!"
#     def info(self):
#         print(f"{self.name} is a {self.occupation}.")


# a= person()
# print(a)
# print(a.name)
# print(a.occupation)
# print(a.networth)

# print("Done with the program.")
# a= person()
# a.info()
# b= person()
# b.name= "Shubham"
# b.occupation= "Accountant"
# b.info()

# print("Done with the previous program.")

# c= person()
# c.name= "Yashii"
# c.occupation= "Software Developer"
# c.networth= f"{1000} Dollars!!!"
# c.info()

# print("Done with the previous program.")

# d= person()
# d.name= "Nikita"
# d.occupation= "Actress"
# d.networth= f"{850} Dollars!!!!"
# d.info()

# print("Done with the previous program.")

print("Hello World", 78)
print(5)
print("Bye")
print(854*965)

print("This is a print Statement.")

print("Hello World!!!!")

print("Python Program.")

p= 85
if (p>5):
    print("P is greater than 5.")
else:
    print("P is not greater than 5.")

print("Done with the previous program.")

print("Hello World \n Hello Mom")
print("This will \'execute\'")
print("You are a good girl/boy \n \"May you dreams come true.\"")

a= complex(74,85)
b= True
c= "Harry"
d= None
print(a)
print(b)
a1= 745
print(a+a1)
print(f"The type of a is {type(a)}.")
print(f"The type of b is {type(b)}.")
print(f"The type of c is {type(c)}.")
print(f"The type of d is {type(d)}.")
print(f"The type of (a and a1)is {type(a+a1)}.")

list1= [74,55,96,15,94,65,789,369,748,963]
print(list1)
print(f"The type of list1 is {type(list1)}.")
for i in list1:
    print(i)

tuple=("School","Dog","Parrot","Apple","Banana","Sparrow","Tiger","Black","Blue")
print(tuple)
print(f"The type of tuple is {type(tuple)}.")
for i in tuple:
    print(i)
    for x in i:
        print(x)

print("Done with the previous program.")

dict1= {"Name":"Sakshi","Age":74,"Canvote": True}
print(dict1)
print(f"THe type of dict1 is {type(dict1)}.")

for i in dict1:
    print(i)

print("Done with the previous program.")

x= 12
y=96
z="85"
d="35"
print(x+y)
print(int(z)+int(d))
print(f"The type of {x} and {y} is {x+y}.")

e= int("856")
f= int("8594")
print(e+f)
c= 74.85
d=96
print(f"Sum of {c} and {d} is {c+d}.")
print(f"The type of {c} and {d} is {type(c+d)}.")
print("Done with the previous program.")

print("Done with the previous program.")


x= input("Enter the first number: ")
y= input("Enter the second number: ")
print(int(x)+int(y))
print("Done with the previous program.")

a= input("Enter your name: ")
print("My name is," + a)

a= 745
b=965
print(a+b)

x= input("Enter First number: ")
y= input("Enter Second number: ")
print(int(x)+int(y))

x= int(input("Enter the first number: "))
y= int(input("Enter the Second number: "))
print(f"Sum of {x} and {y} is {x+y}.")
print(f"The type of Sum of  {x} and {y} is {type(x+y)}.")



