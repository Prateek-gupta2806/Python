x= 4
print(x)

# def hello():
#     x= int(input("Enter the number: "))
#     print(x)
#     print("Hello, Harry")

# hello()

def hello():
    x= int(input("Enter the number: "))
    y= 52
    print(F"The local x is {x}")
    print("Hello, Harry")

print(f"The global x is {x}")
hello()
print(f"The global x is {x}")

x= 10 # Global variable

def my_function():
    global x
    x= int(input('Enter the number: '))
    y= 5 #Local Variable
    print(y)

my_function()
print(x)

# print(y) # Throws an error 


