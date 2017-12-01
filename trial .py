import math


class QuaError(Exception): pass


def quad(a, b, c):
    if a == 0:
        ex = QuaError("Not Quadratic")
        ex.cf = (a, b, c)
        raise ex
    if b * b - 4 * a * c < 0:
        mm = QuaError("No Real Roots")
        mm.cf = (a, b, c)
        raise mm
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return (x1, x2)


def qu(a, b, c):
    try:
        x1, x2 = quad(a, b, c)
        print("Roots are", x1, x2)
    except QuaError as e:
        print(e, e.cf)


qu(2, 3, 4)


class Stud:
    name='Ram'
    def change_name(self,new_name):
        self.name=new_name
        print(self.name)

    def __init__(self,name,sub):
        self.name=name
        self.sub=sub
print(Stud.name)
# s=Stud('kk')
# print(s.name)
s1=Stud('cc','qqqqqq')
# s2=Stud('bb')
print(s1.sub)
# print(s2.name)
# s.change_name('gg')


class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)


def iss(i):
    print('inside')
    return i%2==0
print(iss(3))


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __add__(self,a):
        x=self.x+ a.x
        y=self.y+ a.y
        return Point(x,y)
p1=Point(2,3)
print(p1)
p2=Point(-1,2)
p3=Point(2,2)
print(p1+p2+p3)



#student-subjects-marks
class Vector:
    def __init__(self, a, b):
      self.a = a
      self.b = b
    def sum(self,a,b):
        print(a+b)
    # def mult(self,m,n):
    #     print(m*n)
class Vv(Vector):
    def __init__(self,a,b,c):
        Vector.__init__(self,a,b)
        self.c=c
    def sum(self,a,b):
        print('overridden..')
    def sum(self,m,n,l):
        print('overloaded..')


s=Vv(2,3,4)
s.sum(2,3)



