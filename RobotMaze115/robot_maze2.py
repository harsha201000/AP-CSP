#   a115_robot_maze2.py
from shutil import move
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = 50
starty = 100
turtle_scale = 1.5

#------ robot commands
def move_backward():
  robot.dot(10)
  robot.back(50)

def move_forward():
  robot.dot(10)
  robot.forward(50)

def turn_right():
  robot.speed(0)
  robot.rt(90)
  robot.speed(2)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze2.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# turn robot right with turn_right()
# sample for loop:
move_backward()
turn_left()
for i in range(3):
  move_backward()
  turn_right()
for i in range(2):
  move_forward()
turn_left()
for i in range(3):
  move_backward()
turn_left()
for i in range(3):
  move_forward()
turn_right()
for i in range(2):
  move_forward()

#---- end robot movement 

wn.mainloop()
