
# ==========================
class human: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_all(self):
        print("Your name is: ", self.name)
        print("Your age is: ", self.age)

 

p1 = human("John", 36)

p1.display_all()
#print(p1.name)
#print(p1.age) 

# =======================  method2

class human:
    name= None
    age= None

    def get_name(self):
        self.name= input("Enter your name: ")

    def get_age(self):
        self.age= input("Enter your age: ")

    def display_name(self):
        print("YOur name is: ", self.name)

    def display_age(self):
        print("Your age is: ", self.age)


human1= human()
human1.get_name()
human1.get_age()
human1.display_name()
human1.display_age()
