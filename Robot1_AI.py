import CreateObjects

# Behaviour of Robot1: Robot1 moves forward and when touches the wall of the screen game it bounces with of randomic angle in [0,360]. 
# Robot 1 fires the missile in a randomic way between [0,100] cicles of the while loop

robot1.move(random.randint(0,360),game) # il robot 1 si muove in modo randomico sullo schermo
robot1.speed = 30
missile1.move()

if time == counter1_rand:
    missile1.fire(robot1,game)
    counter1_rand = random.randint(time,time+100) 

