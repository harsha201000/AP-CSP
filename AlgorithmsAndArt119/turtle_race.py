# Import Required Libraries
import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
is_race_on = False

# List of colors and starting y positions for turtles
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

# Draw the finish line
finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(230, 200)
finish_line.pendown()
finish_line.color("black")
finish_line.right(90)
finish_line.forward(400)
finish_line.hideturtle()

# Create, position, and color turtles
for index in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)
    
# Start the race
is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # Check if any turtle has crossed the finish line
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            print(f"The winner is the {winning_color} turtle!")
        
        # Move each turtle forward by a random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


# Keep the screen open until clicked
screen.exitonclick()