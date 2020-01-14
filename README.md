# Programming Robot Battle Game

A programming game is a game based on computer programming. Unlike arcade type games which require human inputs controlling some object, all strategy in a Programming Robot Battle Game must be complete before the actual game begins. Game strategy is condensed into a language that the player will use to design and write their Robot AI.  Multiple Robots will battle against each other in a virtual arena. Only one will win. 

Rules:
- Each robot has 3 lives
- Each robot can shoot missiles depending on their AI
- If RobotA shoots RobotB, RobotB loses 100 scores and 1 life, while    RobotA acquires 100 scores and 1 life
- If RobotA and RobotB have a collision each of them loses 50 scores. If the number of collisions reaches 2 the robot loses 1 life
- Each time that a robot is hit by a missile or has a collision it appears in a randomic position of the screen and starts again the game

The game screen is developed through the turtle module. It is a 600 x 600 screen whose center has coordinates (x = 0,y = 0)

![Screenshot](BattleField.png)
