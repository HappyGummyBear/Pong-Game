from turtle import Turtle #Import turtle class

class Paddle(Turtle): #Class to create and control the paddles

    def __init__(self, position): #Constructor with a position tupple to place the paddle
        super().__init__()
        self.penup() #Remove the line the turtle makes on the screen
        self.shape("square") #Change the shape and color of the paddle
        self.color("white")
        self.turtlesize(stretch_wid=5,stretch_len=1) #Stretch the size of the paddle
        self.goto(position) #Send the paddle to the position specified

    def move_up(self):
        '''Function to move the paddle up on the y axis'''
        new_y = self.ycor() + 20 #Add 20 pixels to the paddle current y position
        self.goto(x=self.xcor(), y=new_y) #Move paddle to new position

    def move_down(self):
        '''Function to move the paddle down on the y axis'''
        new_y = self.ycor() - 20 #Subtract 20 pixels to the paddle current y position to move it down
        self.goto(x=self.xcor(), y=new_y) #Move paddle to new position
