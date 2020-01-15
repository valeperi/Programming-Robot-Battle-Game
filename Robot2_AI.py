import CreateObjects

robot2.move(angleR2,game) # il robot 1 si muove in modo randomico sullo schermo

missile2.move()

if time%50 == 0: 
    angleR2 *= -1

if time%10 == 0:
    missile2.fire(robot2,game)

