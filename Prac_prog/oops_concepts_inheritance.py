#1. Inheritance
class A:
    def method_A(self):
        print("Inside Class A and Method A")
class B:
    def method_B(self):
        print("Inside Class B and Method B")
class C:
    def method_C(self):
        print("Inside Class C and Method C")
#Multiple Inheritance of Class A, Class B and Class C
class D(A,B,C):
    def method_D(self):
        print("Inside Class D and Method D")

d= D()
d.method_A()
d.method_B()
d.method_C()
d.method_D()
