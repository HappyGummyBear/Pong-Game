from turtle import Turtle #Import turtle class


class Scoreboard(Turtle): #Class to control the score of the game

    def __init__(self):
        super().__init__()
        self.color("white") #Change the color of the scoreboard
        self.penup() #Remove the ability to draw a line on the screen
        self.hideturtle() #Hide the turtle on the screen
        self.l_score = 0 #0 on both players score to start the game
        self.r_score = 0

    def update_scoreboard(self):
        '''Function to update the scoreboard with new information'''
        self.clear() #Clear the scoreboard current information from the screen
        self.goto(-100, 200) #Move Scoreboard away from the screen to hide it
        self.write(self.l_score, align="center", font=("Courier", 80, "normal")) #Set up a new scoreboard to write on
        self.goto(100, 200) #Move to old scoreboard position
        self.write(self.r_score, align="center", font=("Courier", 80, "normal")) #Write the new score on the screen

    def l_point(self):
        '''Function to add a point to the left player'''
        self.l_score += 1 #Add 1 to left player score
        self.update_scoreboard() #Call update function to update the scoreboard with new score

    def r_point(self):
        '''Function to add a point to the right player'''
        self.r_score += 1 #Add 1 to right player score
        self.update_scoreboard() #Call update function to update the scoreboard with new score