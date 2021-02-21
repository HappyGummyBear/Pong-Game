from turtle import Turtle #Import turtle class


class Ball(Turtle): #Class to create and control the ball

    def __init__(self):
        super().__init__()
        self.penup() #Remove the tracing line from the turtle
        self.shape("circle") #Give the ball a shape and color
        self.color("white")
        self.x_move = 10 #Pixels the ball will move in the x and y coordinates
        self.y_move = 10

    def start_moving(self):
        '''Function that will get the ball moving at the start of the game'''
        new_x = self.xcor() + self.x_move #Ball coordinates will be added from the x_move and y_move variable
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y) #Moves the ball to the new coordinate

    def y_bounce(self):
        '''Function to move flip the direction the ball bounces when it hits the top or bottom of the screen'''
        self.y_move *= -1

    def x_bounce(self):
        '''Function to flip the direction of the ball if it hits a paddle'''
        self.x_move *= -1

    def reset_ball(self):
        '''Function to reset the ball to its starting position'''
        self.goto((0, 0)) #Resets all variable associated with the ball
        self.x_move = 10
        self.y_move = 10
        self.x_bounce() #Flips the direction the ball originally bounced to

    def increase_speed(self):
        '''Function to increase the speed of the ball'''
        self.x_move *= 1.1 #Adds 10% more speed to the ball x and y direction
        self.y_move += 1.1