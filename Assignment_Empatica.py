import os
import random
import turtle
import time
import CreateObjects

turtle.fd(0) # it creates the screen
turtle.speed(10) # manage the speed of the animation
turtle.bgcolor("black")
turtle.ht() # hide the turtle
turtle.setundobuffer(1)
turtle.tracer(1)

# GAME #
class Game():
    def __init__(self,num):
        self.pen = turtle.Turtle()
        self.numRobots = num
        self.GameState = "GameRunning"

    def draw_border(self):
         # Draw border
         self.pen.speed(0)
         self.pen.color("white")
         self.pen.pensize(3)
         self.pen.penup()
         self.pen.goto(-300, 300)
         self.pen.pendown()
         for side in range(4):
             self.pen.fd(600)
             self.pen.rt(90)
         self.pen.penup()
         self.pen.ht()
         self.pen.pendown()

    # Show Score msg

    def show_msg(self):
        self.pen.undo()
        msg = "        Robots Status:\n\nRobot:      Score:      Lives:"
        self.pen.penup()
        self.pen.goto(320,250)
        self.pen.write(msg, font = ("Arial",20,"normal"))


# SCORE #
class RobotStatus():
    def __init__(self):
        self.pen = turtle.Turtle()
        self.score = 0
        self.lives = 3
        self.RobotState = "Alive"

    def show_RobotStatus(self, name, xpos, ypos, color, game):
        self.pen.undo()
        self.pen.penup()
        msg = name + "              " + str(self.score) + "                   " + str(self.lives)
        if self.RobotState == "Dead":
            msg = "GAME OVER"
        if game.GameState == "Finish" and self.RobotState == "Alive":
            msg = "WINNER"
        self.pen.goto(xpos,ypos)
        self.pen.color(color)
        self.pen.clear()
        self.pen.write(msg, font = ("Arial",16,"normal"))
        self.pen.ht()
        self.pen.pendown()

# GAMEOBJECT #
class Robot(turtle.Turtle): # define the object in the game, we make it inherite from the turtle class
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0) #speed of animation
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1
        self.shapesize(stretch_wid = 1, stretch_len = 1, outline = None) # size of the sprite in terms of width and length (1,1 is the basic one)
        self.speed = 20
        self.counter_collision = 0
        self.state = "Playing"


    # Method to define the motion of the GameObject
    def move(self,deg,game):
        if self.state == "Playing" and game.GameState == "GameRunning":
            self.fd(self.speed) # creates a default forward movement function

            #Boundary detection: if the Robot hits the border it bounces
            if self.xcor() > 290:
                self.setx(290) # set the x position
                self.rt(deg) # set the right rotation angle
            if self.xcor() < - 290:
                self.setx(-290)
                self.rt(deg)
            if self.ycor() > 290:
                self.sety(290) # set the y position
                self.rt(deg) # set the right rotation angle
            if self.ycor() < -290:
                self.sety(-290)
                self.rt(deg)
        if self.state == "Game Over":
            self.goto(-1000,1000)
            self.speed = 0
        if self.state == "Playing" and game.GameState == "Finish":
            self.goto(self.xcor(),self.ycor())
            self.speed = 0

    def rotate(self,deg,game):
        if self.state == "Playing" and game.GameState == "GameRunning":
            self.rt(deg) # creates a default forward movement function
        if self.state == "Game Over":
            self.goto(-1000,1000)
            self.speed = 0
        if self.state == "Playing" and game.GameState == "Finish":
            self.goto(self.xcor(),self.ycor())
            self.speed = 0

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20))and \
        (self.xcor() <= (other.xcor() + 20)) and\
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
           return False

    # COLLISION BETWEEN ROBOTS #
    def collision_RR(self, scoreA, nameA, xposA, yposA, colorA, other_R, scoreB, nameB, xposB, yposB, colorB, game):     
        if self.state == "Playing" and other_R.state == "Playing":
            if self.is_collision(other_R):
                x1 = random.randint(-250,250)
                y1 = random.randint(-250,250)
                x2 = random.randint(-250,250)
                y2 = random.randint(-250,250)
                self.goto(x1,y1)
                scoreA.score -= 50
                self.counter_collision += 1
                if self.counter_collision == 2:
                    scoreA.lives -= 1
                    self.counter_collision = 0
                    if scoreA.lives == 0:
                        self.state = "Game Over"
                        scoreA.RobotState = "Dead"
                        game.numRobots -= 1                       
                        if game.numRobots == 1:
                            game.GameState = "Finish"
                scoreA.show_RobotStatus(nameA, xposA, yposA, colorA, game)
                other_R.goto(x2,y2)
                scoreB.score -= 50
                other_R.counter_collision += 1
                if other_R.counter_collision == 2:
                    scoreB.lives -= 1
                    other_R.counter_collision = 0
                    if scoreB.lives == 0:
                        other_R.state = "Game Over"
                        scoreB.RobotState = "Dead"
                        game.numRobots -= 1
                        if game.numRobots == 1:
                            game.GameState = "Finish"
                scoreB.show_RobotStatus(nameB, xposB, yposB, colorB, game)

    # COLLISION BETWEEN ROBOT AND MISSILE #
    def collision_RM(self, scoreA, nameA, xposA, yposA, colorA, other_M, other_R, scoreB, nameB, xposB, yposB, colorB , game):
        if self.state == "Playing" and other_R.state == "Playing":
            if self.is_collision(other_M):
                x = random.randint(-250,250)
                y = random.randint(-250,250)
                self.goto(x,y)
                # decrease the score of robot2
                other_M.status = "Ready"
                scoreA.score -= 100
                scoreA.lives -= 1
                scoreB.score += 100
                scoreB.lives += 1
                if scoreA.lives == 0:
                    self.state = "Game Over"
                    scoreA.RobotState = "Dead"                    
                    game.numRobots -= 1
                    if game.numRobots == 1:
                        game.GameState = "Finish"
                scoreA.show_RobotStatus(nameA, xposA, yposA, colorA, game)
                scoreB.show_RobotStatus(nameB, xposB, yposB, colorB, game)


# MISSILE #
class Missile(Robot):
    def __init__(self, spriteshape, color, startx, starty):
        Robot.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid = 0.3, stretch_len = 0.4, outline = None)
        self.speed = 50
        self.status = "Ready"
        self.goto(-1000, 1000) # to not visualise it on the screen

    def fire(self,other,game):
        if self.status == "Ready":
            self.goto(other.xcor(),other.ycor())
            self.setheading(other.heading())
            self.status = "Firing"
        if other.state == "Game Over":
            self.goto(-1000, 1000)
            other.goto(-1000,1000)
        if game.GameState == "Finish":
            self.goto(-1000,1000)
            other.speed = 0
  
    def move(self):
        if self.status == "Ready":
            self.goto(-1000, 1000)
        if self.status == "Firing":
            self.fd(self.speed)
        # Border check
        if self.xcor() < -290 or self.xcor() > 290 or \
           self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000,1000)
            self.status = "Ready"


execfile("CreateObjects.py")

time = 0

while True:
    turtle.update()
    time += 1 # the clock is ticking

    execfile("Robot1_AI.py") # this allows to exec the code in the Robot# AI
    execfile("Robot2_AI.py") 
    execfile("Robot3_AI.py")

    execfile("HandleCollisions.py")


delay = input("Press enter to finish")





