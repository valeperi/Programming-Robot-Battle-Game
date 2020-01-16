import CreateObjects

# Behaviour of Robot2: it moves with a speed of 20. When it hits the battle field borders it bounces 
# with 60°, that changes sign after 50 cicles of the while loop. It shoots the missile at multiples 
# of 10 cicles.
robot2.move(angleR2,game) 
missile2.move()

if time%50 == 0: 
    angleR2 *= -1

if time%10 == 0:
    missile2.fire(robot2,game)

