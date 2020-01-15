# Programming Robot Battle Game

*A programming game is a game based on computer programming. Unlike arcade type games which require human inputs controlling some object, all strategy in a Programming Robot Battle Game must be complete before the actual game begins. Game strategy is condensed into a language that the player will use to design and write their Robot AI.  Multiple Robots will battle against each other in a virtual arena. Only one will win.*

The game is developed in python programming language

# Game Description:
**Battle Field:**
The game screen is developed through the Turtle module of python. It is a 600 x 600 screen whose center has coordinates (x = 0,y = 0). The scores, lives and messages for each robot are shown in the right corner of the screen. The Battle Field is shown in the figure below.
![Screenshot](BattleField.png)

**Robot:**
- Each robot is characterised by its own AI. The Robot AI determines the behaviour of the robot, in terms of movement and how often it shoots a missile
- Each robot has 3 lives and starts with 0 score

**Missile**\n
Each robot can shoot a missile if and only if the previous one has reached the border of the battle field

**Collision**
Two types of collision are handled
- collision R-R: it happens when two robots are in same position on the battle field. Both of them lose 50 scores and reappears in a randomic position between x = (-250,250) and y = (-250,250). If the number of R-R collisions of a robot reaches 2, the robot loses 1 life
- collision R-M: it happens when the missile of a robot and another robot are in the same position on the battle field. The robot hit by the missile loses 100 scores and 1 life and reappears in a randomic position between x = (-250,250) and y = (-250,250), while the robot that shooted the missile acquires 100 scores and 1 life

**Losers and Winners**
- A robot dies if its number of lives becomes 0. In this case the robot disappears from the screen and the message "GAME OVER" appears
- The game stops when just one robot stays alive. When this happens the last robot stops on the screen and the message "WINNER" appears

**Files**
The repository contains 5 files .py. 
- main.py: it contains the classes used to create the objects of the game and the infinite while loop 
- e CreateObects.py 
