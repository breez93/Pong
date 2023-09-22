import turtle

#Window Creation

wn = turtle.Screen()
wn.title("Pong by Paulo Rafael")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.bgcolor("black")

#Paddle A Creation

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("White")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)


#Paddle B Creation

paddle_b = turtle.Turtle()
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("White")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)


#Ball creation
ball = turtle.Turtle()
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("White")
ball.penup()
ball.goto(0,0)

#BallMovement Moves by 2 pixels
ball.dx = 0.1
ball.dy = 0.1
#Keyboard bind


#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main Game Loop
while True:
    wn.update()

    #Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(0)
        ball.dx *= -1

    
    if ball.xcor() < -390:
        ball.setx(0)
        ball.dx *= -1

 #Its getting stuck but ye games this pretty much done. getting this done tomorow.
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor > paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
     ball.setx(340)
     ball.dx*= -1
