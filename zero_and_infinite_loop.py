#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# Add a loop with a zero-iteration condition
run = 'n'

while (run == 'y'):
  painter.pencolor('green')
  painter.pensize(3)
  for i in range(4):
    painter.forward(50)
    painter.right(90)
  painter.pencolor('red')
  painter.pensize(5)
  for i in range(4):
    painter.forward(50)
    painter.right(90)
  

# Add an infinite loop
run = 'y'

while (run == 'y'):
  painter.pencolor('green')
  painter.pensize(3)
  for i in range(4):
    painter.forward(50)
    painter.right(90)
  painter.pencolor('red')
  painter.pensize(5)
  for i in range(4):
    painter.forward(50)
    painter.right(90)


wn = trtl.Screen()
wn.mainloop()