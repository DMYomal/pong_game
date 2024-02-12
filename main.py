from turtle import Turtle, Screen

screen = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor("Black")
screen.title("Pong Game")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5,stretch_len=1)
paddle.penup()
paddle.goto(350,0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

game_is_on = True
while game_is_on:
    screen.update()

screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")

screen.exitonclick()

