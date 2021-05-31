import datetime


#year = input('Please enter the year: ')
class Person(object):
    def __init__(self, name, date_of_birth):
        super().__init__()
        self.name = name
        dob = date_of_birth.split("/")
        self.date_of_birth = dob[2]
        
    def speak(self): 
        print("hello")     

    def walk(self):
        print("walking away")

    def get_name(self): 
        return self.name
    
    def get_age(self): 
        #return (int(year) - int(self.date_of_birth))
        return datetime.date.today().year - int(self.date_of_birth)

class Student(Person):
    def __init__(self, name, date_of_birth, courselist):
        super().__init__(name, date_of_birth)
        self.courselist = courselist

    def get_courses(self):
        return self.courselist
    
    def speak(self): 
        print("I am so tired!")


User = Person("Eyram", "13/05/2000")
User.speak()
User.walk()
print(User.get_name())
print(User.get_age())
course = Student("Eyram", "13/05/2000", ["Biology", "Mathematics", "Physics"])
print(course.get_courses())
course.speak()





