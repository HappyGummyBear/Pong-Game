from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Create window for the game. Setup size and color
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen() #Function to kisten for user inputs
screen.tracer(0) #Stop screen from updating on its own

#Create paddles from paddle class
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
#Create ball from ball class
ball = Ball()
#Create scoreboard from scoreboard class
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

game_is_on = True #Boolean to keep game running

#Functions to control the two paddles from the listen function
screen.onkey(fun=paddle_r.move_up, key="Up")
screen.onkey(fun=paddle_r.move_down, key="Down")
screen.onkey(fun=paddle_l.move_up, key="w")
screen.onkey(fun=paddle_l.move_down, key="s")

while game_is_on: #Loop to keep updating screen
    time.sleep(0.1) #Timer to slow down loop
    screen.update() #Manually update screen since tracer function disabled the updating
    ball.start_moving() #Function from ball class to move the ball

    # Detect wall collision
    if ball.ycor() > 290 or ball.ycor() < -290: #If ball hits the top and bottom of screen it will bounce off
        ball.y_bounce()

    # Detect collision with right paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.x_bounce() #If ball hits one of the paddles it will bounce off and pick up speed
        ball.increase_speed()

    # Detect back wall collision
    if ball.xcor() > 380:
        ball.reset_ball() #If ball hits right wall behind the paddle the ball resets and the left player gets a point
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_ball() #If ball hits left wall behind the paddle the ball resets and the right player gets a point
        scoreboard.r_point()

#Function to keep window open
screen.exitonclick()
