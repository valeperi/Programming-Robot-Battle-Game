import CreateObjects

# Behaviour of Robot3: it moves with a speed of 10. When it hits the battle field borders it bounces 
# with 30°. At multiples of 10 cicles it performs a right rotation of 45°. It shoots the missile at multiples 
# of 5 cicles.
  

robot3.move(30,game)
robot3.speed = 10

if time%10 == 0:
    robot3.rotate(45,game)

#robot3.rt(90) # il robot 1 si muove in modo randomico sullo schermo
missile3.move()

if time%5 == 0:
    missile3.fire(robot3,game)
