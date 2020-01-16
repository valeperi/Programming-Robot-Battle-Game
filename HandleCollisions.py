import CreateObjects

# COLLISION BETWEEN ROBOTS
# robot1 and robot2
robot1.collision_RR(score1, nameR1, 320, 200, colorR1, robot2, score2, nameR2, 320, 150, colorR2, game)
# robot1 and robot3
robot1.collision_RR(score1, nameR1, 320, 200, colorR1, robot3, score3, nameR3, 320, 100, colorR3, game)
# robot2 and robot3
robot2.collision_RR(score2, nameR2, 320, 150, colorR2, robot3, score3, nameR3, 320, 100, colorR3, game)

# COLLISION BETWEEN ROBOT AND MISSILE
# robot1 and missile of robot2
robot1.collision_RM(score1, nameR1, 320, 200, colorR1, missile2, robot2, score2, nameR2, 320, 150, colorR2, game)
# robot1 and missile of robot3
robot1.collision_RM(score1, nameR1, 320, 200, colorR1, missile3, robot3, score3, nameR3, 320, 100, colorR3,game)
# robot2 and missile of robot1
robot2.collision_RM(score2, nameR2, 320, 150, colorR2, missile1,robot1, score1, nameR1, 320, 200, colorR1, game)
# robot2 and missile of robot3
robot2.collision_RM(score2, nameR2, 320, 150, colorR2, missile3,robot3, score3, nameR3, 320, 100, colorR3, game)
# robot3 and missile of robot1
robot3.collision_RM(score3, nameR3, 320, 100, colorR3, missile1,robot1, score1, nameR1, 320, 200, colorR1, game)
# robot3 and missile of robot2
robot3.collision_RM(score3, nameR3, 320, 100, colorR3, missile2, robot2, score2, nameR2, 320, 150, colorR2, game)

