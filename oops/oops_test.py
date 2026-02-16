# Aditya Ravichander
# Practice oops coding in python for beginners
# Goal: Revise and touch up basics after a gap

# Resource: Tech with tim

                    # Why OOPS
                    # Example: What is an Object?

# x = 1
# print(type(x))

# def hello():
#     print("hello")
# print(type(hello))

# x = 1
# y = "hello"
# z = 2
# print(x+y)
# print(x+z)

                # Methods - perform on objects

# string = "hello"
# print(string.upper())
# x = 1
# # method acting on object string that is storing a string variable and we are able to use is because object is string
# print(x.upper())

                # Creating a class

class Dog:  #CamelCase

    def __init__(self, name, age):
        self.name = name  # attribute of the object
        self.age = age
        print(name)
        print(age)
    
                # special method - allows us to instant the object right when created... this will be called right when we do d = Dog()

    def add_one(self, x):
        return x+1

                # invisibly pass the dog object when we get name of dog
    def get_name(self): 
        return self.name
    
    def get_age(self):
        return self.age
    
    def bark(self):
        print("bark")
    
    def set_age(self,age):
        self.age = age

                # creating a variable and assign it to instance of Dog class

# d = Dog("Tim") 
# d.bark()
# print(d.add_one(5))
# print(type(d))

                # init function and attributes, objects

# d2 = Dog("Bill")
# print(d.name)
# print(d2.name)
# print(d.get_name())

# d3 = Dog("Tim", "24")
# print(d3.get_age())
# d4 = Dog("Bill", 25)

                # modifying attributes

# d = Dog("Tim", 34)
# d.set_age(23)
# print(d.get_age())

                    # Once we create class, we can create as many instances of the class
# dog1_name = "Tim"
# dog1_age = 24
# what if 25000 dogs, every time run code, make different no. of dogs
# dogs_name = ["Tim", "Bill"]
# dogs_age = [32,13]
# pain when we need to access ... what if 25 attributes, methods... find index in a list, time, reference other index, attributes
# what if delete an instance, find index, delete everything at same time, no offset, etc,, it's pain
# this is why OOPS

                # complex object, multiple classes interact
                # Example: Students, grades, Course, maxgrade, avg grade, lowest grade, model a school. 

# class Student:
    
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade # 0 - 100
    
#     def get_grade(self):
#         return self.grade

# class Course:
    
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
        
#         # attribute and did not assign to parameters/arguments. We decide to define. 
#         self.students = []
#         self.is_active = False

#     # method to allow add students to the course

#     def add_student(self,student):
#         #instance of student object
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
    
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()  # using get_grade method and not attribute so that code doesn't break when attribute changes.
#             return value / len(self.students)
#         pass

# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 19, 75)
# s3 = Student("Jill", 19, 65)

# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.add_student(s3))
# print(course.get_average_grade())
# print(course.students[0].name)

                # Inheritance

# class Cat:
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    # def speak(self):
    #     print("Meow")

# class Dog: 
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age    
    # def speak(self):
    #     print("bark")

                # Inheritance + Create another class

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f" I am {self.name} and I am {self.age} years old ")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)     # super - ref the super/parent class, init - method want to call, name,age - arguments we need
        self.color = color

    def speak(self):
        print("Meow")
    
    def show(self):
        print(f" I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet): 
    def speak(self):
        print("bark")

class Fish(Pet):
    pass

# p = Pet("Tim", 19)
# p.show()
# c = Cat("Bill", 34, "white")
# c.show()
# d = Dog("Jill", 25)
# f = Fish("Bubble", 10)
# d.show()
# p.speak()
# c.speak()
# d.speak()
# f.speak()


                # Class attributes
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Tim")
p2 = Person("Jill")
# print(p1.number_of_people)
# print(Person.number_of_people)
# Person.number_of_people = 8 
# print(p1.number_of_people)
# Person.number_of_people = 9 
# print(p1.number_of_people)

print(Person.number_of_people_())

                # Static methods

def add1():
    pass

def add2():
    pass

class Math:
    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def pr():
        print("run")

print(Math.add5(5))
Math.pr()
