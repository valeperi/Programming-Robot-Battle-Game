# Programming Robot Battle Game

*A programming game is a game based on computer programming. Unlike arcade type games which require human inputs controlling some object, all strategy in a Programming Robot Battle Game must be complete before the actual game begins. Game strategy is condensed into a language that the player will use to design and write their Robot AI.  Multiple Robots will battle against each other in a virtual arena. Only one will win.*

The game is developed in python programming language

**Rules:**
- Each robot is characterised by its own AI. The Robot AI determines the movement of the robot and how often it shoots the missile
- Each robot has 3 lives
- If RobotA shoots RobotB, RobotB loses 100 scores and 1 life, while RobotA acquires 100 scores and 1 life
- If RobotA and RobotB have a collision each of them loses 50 scores. If the number of collisions reaches 2 the robot loses 1 life
- Each time that a robot is hit by a missile or has a collision it appears in a randomic position of the screen and starts again the game
- If the number of lives of Robot i becomes 0, Robot i disappears from the screen and the message "GAME OVER" appears
- The game stops when just one robot stays alive. When this happens the last robot stops on the screen and the message "WINNER" appears

The game screen is developed through the Turtle module of python. It is a 600 x 600 screen whose center has coordinates (x = 0,y = 0). The scores, lives and messages for each robot are shown in the right corner of the screen. The Battle Field is shown in the figure below.

![Screenshot](BattleField.png)

**Files**
The repository contains 5 files .py. 
- main.py: it contains the classes used to create the objects of the game and the infinite while loop 
- e CreateObects.py 
