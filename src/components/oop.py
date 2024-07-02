"""class car:# kei kura chutyaunu baneko class 
    color="blue"
    module="tata"
car1=car()# ani class ntra ko attribute lai chutyaunu baneko object ho 
print(car1.color,car1.module)

car2=car()
print(car2.color)"""


class student:
    college="GLOBAL COLLAGE"
    def __init__(self,fullname,marks,address):
        self.name=fullname
        self.marks=marks
        self.address=address
        print("adding new student in class....")

    def welcome(self):
        print("welcome students on GLOBAL COLLAGE")
    
s1=student("kuldip",98,"ktm")
s1.welcome()
print(s1.name,s1.marks,s1.address)
s2=student("sumitra",99,"ktm")
s2.welcome()
print(s2.name,s2.marks,s2.address)
print()
