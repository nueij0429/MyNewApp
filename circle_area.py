PI = 3.14

def calculate(radius):
    return PI * radius ** 2 #원의 넓이 공식: PI * r^2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return calculate(self.radius)

if __name__ == "__main__":
    circle = Circle(5)
    print(f"원의 넓이: {circle.area()}")