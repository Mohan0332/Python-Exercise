class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def talk(self):
        return self.x

point1 = Point(10,20)
x1 = point1.talk()
print(f'The x-cordinate is of point1 is {x1}')