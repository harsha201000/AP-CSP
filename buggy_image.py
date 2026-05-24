# a116_buggy_image.py

import turtle as trtl

# Create the spider body
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

# Configure spider legs
num_legs = 8
angle = 20  # Reduced angle for tighter leg grouping
distance = 70
spider.pensize(5)

'''
Draw legs on both sides
'''
leg = 0
while leg < num_legs:
    spider.penup()
    spider.goto(0, 20)  # Go back to body center
    spider.pendown()

    if leg < num_legs / 2:
        # Left side legs
        spider.setheading(angle * leg - 45)
    else:
        # Right side legs
        spider.setheading(angle * leg + 45)

    spider.forward(distance)
    leg += 1

spider.hideturtle()

'''
Add spider eyes
'''
eye = trtl.Turtle()
eye.penup()
eye.goto(-10, 40)  # Left eye position
eye.pendown()
eye.pensize(10)
eye.color("red")
eye.circle(2)

eye.penup()
eye.goto(10, 40)  # Right eye position
eye.pendown()
eye.circle(2)

eye.hideturtle()

# Keep window open
wn = trtl.Screen()
wn.mainloop()
