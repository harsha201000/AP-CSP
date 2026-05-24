#   Add your code here and add comments to your code
#   to describe what each section of code is doing

# Import required libraries
import turtle as t

# Create a painter object
painter = t.Turtle()

# Draw a grass
painter.penup()
painter.goto(-200,-150)
painter.pendown()
painter.pencolor("green")
painter.fillcolor("green")
painter.begin_fill()
painter.forward(400)
painter.right(90)
painter.forward(200)
painter.right(90)
painter.forward(400)
painter.right(90)
painter.forward(200)
painter.right(90)
painter.end_fill()

# Draw a sky
painter.penup()
painter.goto(-200,250)
painter.pendown()
painter.pencolor("lightblue")
painter.fillcolor("lightblue")
painter.begin_fill()
for i in range(4):
  painter.forward(400)
  painter.right(90)
painter.end_fill()

# Draw a sun
painter.penup()
painter.goto(150,150)
painter.pendown()
painter.pencolor("yellow")
painter.fillcolor("yellow")
painter.begin_fill()
painter.circle(30)
painter.end_fill()

# Draw a mountain
painter.penup()
painter.goto(-190,-150)
painter.pendown()
painter.pencolor("brown")
painter.fillcolor("brown")
painter.begin_fill()
side_length = int(input("Enter the side length: "))
for i in range(3):
  painter.forward(side_length)
  painter.left(120)
painter.end_fill()


# Create a screen object
win = t.Screen()
win.mainloop()