l=9
b=12
h=10
class triangle():
    def area1(self):
        print(1/2*b*h)
class rectangle(triangle):
    def area2(self):
        print(l*b)
object=rectangle()
object.area1()
object.area2()