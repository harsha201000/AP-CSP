#   a114_order_of_operations_2.py
#   This program uses some arithmetic to move the turtle and draw.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.shape("square")
painter.color("turquoise")

painter.stamp()
painter.forward((4-(5+7)*((2-18)/4))*2)
painter.stamp()

wn = trtl.Screen()
wn.mainloop()