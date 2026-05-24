#   a113_flower.py
#   This code draws a flower with twice
#   as many petals as the original
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)

# draw flower
painter.color("darkorchid")
painter.goto(20,180)

for petal in range(36):
  painter.right(10)
  painter.forward(15)
  painter.stamp()

wn = trtl.Screen()
wn.mainloop()