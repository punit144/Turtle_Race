import turtle
from random import randint


class TurtleCreate:

    def __init__(self, name, location, color="red"):
        self.name = name
        self.location = location
        self.color = color

    def create_turtle(self):
        self.name = turtle.Turtle()
        self.name.speed(5)
        self.name.color(self.color)
        self.name.shape("turtle")
        self.name.penup()
        self.name.goto(-250, self.location)
        self.name.pendown()
        for a in range(10):
            self.name.right(36)
        return True


wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle Race")
track_turtle = turtle.Turtle()

track_turtle.speed(500)
track_turtle.penup()
track_turtle.goto(-220, 220)
for step in range(23):
    track_turtle.write(step, align="center")
    track_turtle.right(90)
    track_turtle.forward(10)
    track_turtle.pendown()
    for i in range(21):
        track_turtle.forward(10)
        track_turtle.penup()
        track_turtle.forward(10)
        track_turtle.pendown()
    track_turtle.penup()
    track_turtle.backward(430)
    track_turtle.left(90)
    track_turtle.forward(20)

user_1 = TurtleCreate(name="p", location=200, color="red")
user_1.create_turtle()
user_2 = TurtleCreate(name="s", location=150, color="black")
user_2.create_turtle()
user_4 = TurtleCreate(name="su", location=100, color="pink")
user_4.create_turtle()
user_3 = TurtleCreate(name="v", location=50, color="yellow")
user_3.create_turtle()
user_5 = TurtleCreate(name="g", location=0, color="blue")
user_5.create_turtle()
user_6 = TurtleCreate(name="a", location=-50, color="orange")
user_6.create_turtle()
user_7 = TurtleCreate(name="k", location=-100, color="sky blue")
user_7.create_turtle()
user_8 = TurtleCreate(name="ga", location=-150, color="purple")
user_8.create_turtle()

for turn in range(158):
    user_1.name.forward(randint(1, 5))
    user_2.name.forward(randint(1, 5))
    user_3.name.forward(randint(1, 5))
    user_4.name.forward(randint(1, 5))
    user_5.name.forward(randint(1, 5))
    user_6.name.forward(randint(1, 5))
    user_7.name.forward(randint(1, 5))
    user_8.name.forward(randint(1, 5))

del user_1
del user_2
del user_3
del user_4
del user_5
del user_6
del user_7
del user_8
turtle.done()
