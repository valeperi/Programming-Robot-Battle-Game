import CreateObjects

# Behaviour of Robot1: It moves with a speed of 30. When it hits the battle field borders it bounces 
# with a randomic angle in the range (0°,360°). It shoots the missile in a randomic instant in the 
# range (0,100) clicles of the while loop, after the previous missile 

robot1.move(random.randint(0,360),game) # il robot 1 si muove in modo randomico sullo schermo
robot1.speed = 30
missile1.move()

if time == counter1_rand:
    missile1.fire(robot1,game)
    counter1_rand = random.randint(time,time+100) 

