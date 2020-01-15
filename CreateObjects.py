
import random
from  Assignment_Empatica import Robot # import the Robot class 
from Assignment_Empatica import Missile # import the Missile class 
from Assignment_Empatica import RobotStatus # import the RobotStatus class
from Assignment_Empatica import Game # import the Game class

# Number of Robots *
robotNum = 3

# Create the game object
game = Game(robotNum)
# Draw the game border
game.draw_border()
# Show the game status
game.show_msg()


# Missile Characteristics
shape = "triangle"
colorM = "white"

# Create Robot 1: 
nameR1 = "Robot 1" 
colorR1 = "red"
robot1 = Robot("triangle", "red", random.randint(-290,290), random.randint(-290,290)) # in this way Robot1 appears in a randomic position of the battle field each time that the game starts
score1 = RobotStatus()
score1.show_RobotStatus(nameR1 , 320, 200, colorR1, game)
missile1 = Missile(shape, colorM, 0, 0)
counter1_rand = random.randint(1,100) # randomic number used to randomly shoot missile1 

# Create Robot 2
nameR2 = "Robot 2"
colorR2 = "blue"
robot2 = Robot(shape, colorR2, 0, 0)
score2 = RobotStatus()
score2.show_RobotStatus(nameR2, 320, 150, colorR2, game)
missile2 = Missile(shape, colorM, 0, 0)
angleR2 = 60 # rebounce angle of robot2 

# Create Robot 3
nameR3 = "Robot 3"
colorR3 = "orange"
robot3 = Robot(shape, colorR3, 250, -250)
score3 = RobotStatus()
score3.show_RobotStatus(nameR3, 320, 100, colorR3, game)
missile3 = Missile(shape, colorM, 0, 0)



