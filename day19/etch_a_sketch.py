from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counterclockwise():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)

def move_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clearscreen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_counterclockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clearscreen, "c")

screen.exitonclick()
#
# from turtle import Turtle, Screen
#
# screen = Screen()
# tim = Turtle()
#
# def move_forwards():
#     tim.forward(20)
#
# def move_backwards():
#     tim.backward(20)
#
# def move_counterclockwise():
#     tim.circle(100, 10)
#
# def move_clockwise():
#     tim.circle(-100, 10)
#
# def clearscreen():
#     tim.clear()
#
#
# screen.listen()
# screen.onkey(key="w",  fun=move_forwards)
# screen.onkey(key="s",  fun=move_backwards)
# screen.onkey(key="a",  fun=move_counterclockwise)
# screen.onkey(key="d",  fun=move_clockwise)
# screen.onkey(key="c",  fun=clearscreen)
#
# screen.exitonclick()
#
# from turtle import Turtle, Screen
#
# tim = Turtle()
# sc = Screen()
#
# def move_forward():
#     tim.forward(10)
#
# def move_back():
#     tim.backward(10)
#
# def moveLeft():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def moveRight():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# sc.listen()
# sc.onkey(move_forward(), "w")
# sc.onkey(move_back(), "s")
# sc.onkey(moveLeft(), "a")
# sc.onkey(moveRight(), "d")
# sc.onkey(clear(), "c")
#
#
# sc.exitonclick()

