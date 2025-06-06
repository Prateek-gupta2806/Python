# # Day 61

# class Employee:
#     def __init__(self, name, id):
#         self.name= name
#         self.id= id

#     def showDetails(self):
#         print(f"The name of Employee:  {self.id} is {self.name}.")

# e= Employee("Rohan Das", 400)
# e.showDetails()
# e2= Employee("Harry",4100)
# e2.showDetails()
# print("Done with the previous program.")

# class Employee:
#     def __init__(self, name, id):
#         self.name= name
#         self.id= id

#     def showDetails(self):
#         print(f"The name of Employee:  {self.id} is {self.name}.")

# class Programmer(Employee):
#     def showlanguage(self):
#         print("The default Language is Python.")


# e= Employee("Rohan Das", 400)
# e.showDetails()
# e2= Employee("Harry",4100)
# e2.showDetails()

# e3= Programmer("Harry",4100)
# e3.showlanguage()

# Kaun Banega Crorepati

# try:
#     name= input("Enter Your name: ")
#     print("My name is,", name)
# except:
#     print("Enter the name only.")

# print("Welcome to Kaun Banega Crorepati", name)

# questions= [
#     ["Which is the capital of India?","Delhi","Banglore","Lucknow","Kolkata",1],
#     ["Which is the capital of Uttar Pradesh?","Lucknow","Kanpur","Varanasi","Agra",1],
#     ["What is the Currency of India?","Dollar","Euro","Rupee","Yen",3],
#     ["Which planet is known as Red Planet?","Earth","Mars","Venus","Jupiter",2],
#     ["Who wrote Ramayana?", "Valmiki","Tulsidas","Kalidas","Premchand",1],
# ]


# levels=  [1000,2000,3000,5000,10000]
# money= 0

# for i in range(0,len(questions)):
#     question= questions[i]
#     print(f"\nQuestion {i+1} {questions[i][0]}  (Rs.{levels[i]})")
#     print(f"A. {questions[i][1]}         B. {questions[i][2]}")
#     print(f"C. {questions[i][3]}         D. {questions[i][4]}")
#     try:
#         l=[0,1,2,3,4]
#         reply= int(input("Enter your answer in number in 1-4 only or 0 to quit: "))
#         reply= l[reply]
#     except:
#         print("Enter the number only")

#     if (reply==0):
#         print("Apne quit kar diya.")
#         break

#     if (reply== questions[i][5]):
#         print(f"Sahi Jawab, Ap Jit te haii Rs. {levels[i]}. ")
#         money= levels[i]

#         if i==4:
#             money= 10000

#     else:
#         print("Galat Jawab!!!")
#         correctanswer= questions[i][5]
#         print(f"Sahi jawab haii {correctanswer}.")
#         break

# print(f"Your take home money is  Rs.{money}.")
# print("Game over, Thank you for playing the game.")

x= int(input("enter the number only: "))
print(x)
if not (x==2):
    print("You have entered wrong number.", 7489546665)
else:
    print(745)


x= int(input("enter the number only: "))
print(x)
if x not in [7458,9658,1452,6325]:
    print("You have entered wrong number.", 7489546665)
else:
    print(745)



