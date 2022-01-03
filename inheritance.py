class Parent():
    def fun1(self):
        print('this is parent class')
class Child(Parent):
    def fun2(self):
        print('this is children class')
ob=Child()
ob.fun1()
ob.fun2()
