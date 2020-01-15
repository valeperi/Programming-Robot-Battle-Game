import CreateObjects

# COLLISION BETWEEN ROBOTS
# robot1 and robot2
robot1.collision_RR(score1, "Robot1", 320, 200, "red", robot2, score2, "Robot2", 320, 150, "blue", game)
# robot1 and robot3
robot1.collision_RR(score1, "Robot1", 320, 200, "red", robot3, score3, "Robot3", 320, 100, "orange", game)
# robot2 and robot3
robot2.collision_RR(score2, "Robot2", 320, 150, "blue", robot3, score3, "Robot3", 320, 100, "orange", game)

# COLLISION BETWEEN ROBOT AND MISSILE
# robot1 and missile of robot2
robot1.collision_RM(score1, "Robot1", 320, 200, "red", missile2, robot2, score2, "Robot2", 320, 150, "blue", game)
# robot1 and missile of robot3
robot1.collision_RM(score1, "Robot1", 320, 200, "red", missile3, robot3, score3, "Robot3", 320, 100, "orange",game)
# robot2 and missile of robot1
robot2.collision_RM(score2, "Robot2", 320, 150, "blue", missile1,robot1, score1, "Robot1", 320, 200, "red",game)
# robot2 and missile of robot3
robot2.collision_RM(score2, "Robot2", 320, 150, "blue", missile3,robot3, score3, "Robot3", 320, 100, "orange",game)
# robot3 and missile of robot1
robot3.collision_RM(score3, "Robot3", 320, 100, "orange", missile1,robot1, score1, "Robot1", 320, 200, "red",game)
# robot3 and missile of robot2
robot3.collision_RM(score3, "Robot3", 320, 100, "orange", missile2, robot2, score2, "Robot2", 320, 150, "blue",game)

