#  a113_forward_and_right_6times.py
import turtle as trtl

painter = trtl.Turtle()

# Move forward 20 and turn right 20,
# six times to create an arc
for i in range(6):
  painter.forward(20)
  painter.right(20)

wn = trtl.Screen()
wn.mainloop()