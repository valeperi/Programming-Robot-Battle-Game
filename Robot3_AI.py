import CreateObjects

# Behaviour of Robot2: Robot2 moves forward and when touches the wall of the screen game it bounces with a 30 degree angle. 
# Robot 1 fires the missile in a randomic way between [0,100] cicles of the while loop

robot3.move(30,game)
robot3.speed = 10

if time%10 == 0:
    robot3.rotate(45,game)

#robot3.rt(90) # il robot 1 si muove in modo randomico sullo schermo
missile3.move()

if time%5 == 0:
    missile3.fire(robot3,game)
