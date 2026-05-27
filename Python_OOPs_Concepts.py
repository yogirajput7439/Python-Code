# from module import myFunc

# Class Is like a blueprint of car and 
# Objects is Like Real Car

class Students:
  name = "Yogesh Rajput"
  Age = 21
  def __init__(self):
    print("Hello Yogesh")  # Constructor was Callled

  
  s1 = Students()

print(s1.name) #Output --> Yogesh Rajput

# __init__ Constructor in 

class Student:
  def __init__(self):
    print("Init Constructor callinng")

# What is Self 

class Student:
  def __init__(self, name):
    self.name = name

s1 = Student("Yogesh")

print(s1.name) 
# Output --> Yogesh

