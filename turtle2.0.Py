import turtle
def draw_octagon():
    for _ in range(8):
        turtle.forward(100)
        turtle.left(45)
window = turtle.Screen()
window.bgcolor("white")
stop_sign = turtle.Turtle()
stop_sign.shape("turtle")
stop_sign.color("red")
stop_sign.speed(1)
stop_sign.penup()
stop_sign.goto(0, -100)
stop_sign.pendown()
stop_sign.begin_fill()
draw_octagon()
stop_sign.end_fill()
stop_sign.penup()
stop_sign.goto(0, -50)
stop_sign.pendown()
stop_sign.color("white")
stop_sign.write("STOP", align="center", font=("Arial", 20, "bold"))
window.exitonclick()
