import CreateRobots

robot2.move(angle,game) # il robot 1 si muove in modo randomico sullo schermo
robot2.speed = 20

missile2.move()

if time%50 == 0: 
    angle *= -1

if time%10 == 0:
    missile2.fire(robot2,game)
