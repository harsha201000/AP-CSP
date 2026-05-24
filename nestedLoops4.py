#   a114_nested_loops_4.py 
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)   # faster drawing
painter.penup()
painter.goto(-200, 0)
painter.pendown()

x = -200
y = 0
move_x = 1
move_y = 1

# ---- First pattern: starts by going UP ----
while (x < 2):

  while (y < 100):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = -1
  
  while (y > 0):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = 1

# ---- Second pattern: starts by going DOWN ----
x = -200  # reset back to left side
y = 0
painter.penup()
painter.goto(x, y)
painter.pendown()
move_x = 1
move_y = -1   # opposite direction

while (x < 2):

  while (y > -100):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = 1

  while (y < 0):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = -1

wn = trtl.Screen()
wn.mainloop()
