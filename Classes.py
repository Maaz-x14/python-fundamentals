class Point:
    def __init__(self, num1, num2):
        self.x = num1
        self.y = num2

    def move(self):
        print("Point moved")

    def draw(self):
        print("Point drawn")

    def addition(self, num1, num2):
        return num1 + num2


point1 = Point(6, 11)
point1.draw()
point1.move()
print(point1.addition(point1.x, point1.y))
