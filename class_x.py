class student:
    def __init__(self, name, age, GPA):
        self.name = name 
        self.age = age 
        self.GPA = GPA 
    def introduce_func(self):
        print("Hello my name is ", self.name, ". I am ", self.age, "years old. My GPA is " , self.GPA)

p1 = student("elena", 17, 4.0)
p1.introduce_func()


   
class course:
    def __init__(self, duration, difficulty):
        self.duration = duration 
        self.difficulty = difficulty 
    def myfunc(self):
        print("This course has a duration of", self.duration, "days and a difficulty level of", self.difficulty)

c1= course(60, 5)
c1.myfunc()

 