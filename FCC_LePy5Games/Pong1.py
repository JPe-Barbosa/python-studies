#Turtle module is realy good for simple games, a lot of py games use it.
#The module aim is to make turtle graphics, vectorial drawings using a 
#cursor relative to a cartesian plane.

import turtle

#constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 5
PADDLE_HEIGTH = 1
PADDLE_INCREMENT = 20
BALL_SPEED = 0.5

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)#speed in which the animation paddle moves in the game, in this case the maximum possible
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = PADDLE_WIDTH, stretch_len = PADDLE_HEIGTH)
paddle_a.penup() # with this the movement of the object dosen't leave a trace
paddle_a.goto(-(SCREEN_WIDTH/2-50), 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)#speed in which the paddle moves in the game, in this case the maximum possible
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = PADDLE_WIDTH, stretch_len = PADDLE_HEIGTH)
paddle_b.penup()
paddle_b.goto((SCREEN_WIDTH/2-50), 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)#speed in which the paddle moves in the game, in this case the maximum possible
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = BALL_SPEED #dx is for delta. It dictates the speed of the game 
ball.dy = BALL_SPEED

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: "+ str(score_a) +" Player B: "+ str(score_b), align="center", font=("Courier", 24, "normal"))



# Function 
def paddle_a_up():
    y = paddle_a.ycor()
    if y + PADDLE_INCREMENT + 50 > SCREEN_HEIGHT/2:
        paddle_a.goto(-(SCREEN_WIDTH/2-50),SCREEN_HEIGHT/2-50)
        return
    y += PADDLE_INCREMENT
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y - PADDLE_INCREMENT - 50 < -SCREEN_HEIGHT/2:
        paddle_a.goto(-(SCREEN_WIDTH/2-50),-SCREEN_HEIGHT/2+50)
        return
    y -= PADDLE_INCREMENT
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y + PADDLE_INCREMENT + 50 > SCREEN_HEIGHT/2:
        paddle_b.goto((SCREEN_WIDTH/2-50),SCREEN_HEIGHT/2-50)
        return
    y += PADDLE_INCREMENT
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y - PADDLE_INCREMENT - 50 < -SCREEN_HEIGHT/2:
        paddle_b.goto((SCREEN_WIDTH/2-50),-SCREEN_HEIGHT/2+50)
        return
    y -= PADDLE_INCREMENT
    paddle_b.sety(y)

# Keyboard bindig
wn.listen() #it is open to keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

# Keyboard bindig
wn.listen() #it is open to keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


        

#main loop of the game
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > SCREEN_HEIGHT/2 -10:
        ball.sety(SCREEN_HEIGHT/2 -10)
        ball.dy *= -1 #inverts the directions of the ball

    if ball.ycor() < -(SCREEN_HEIGHT/2 -10):
        ball.sety(-(SCREEN_HEIGHT/2 -10))
        ball.dy *= -1

    if ball.xcor() > SCREEN_WIDTH/2 -10:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -(SCREEN_WIDTH/2 -10):
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: "+ str(score_a) +" Player B: "+ str(score_b), align="center", font=("Courier", 24, "normal"))


    #Paddle and ball collision
    if (ball.xcor() > (SCREEN_WIDTH/2 -50- 2*PADDLE_WIDTH) and ball.xcor() < (SCREEN_WIDTH/2 -50)) and (ball.ycor() < paddle_b.ycor() +  50 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx((SCREEN_WIDTH/2 -50- 2*PADDLE_WIDTH))
        ball.dx *= -1

    if (ball.xcor() < -(SCREEN_WIDTH/2 -50- 2*PADDLE_WIDTH) and ball.xcor() > -(SCREEN_WIDTH/2 -50)) and (ball.ycor() < paddle_a.ycor() +  50 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-(SCREEN_WIDTH/2 -50- 2*PADDLE_WIDTH))
        ball.dx *= -1

