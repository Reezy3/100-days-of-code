import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
y_positions = [-100, -50, 0, 50, 100, 150]
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)





# john = Turtle(shape="turtle")
# john.color("orange")
# john.penup()
# john.goto(x=-240, y=-50)
#
# kim = Turtle(shape="turtle")
# kim.color("green")
# kim.penup()
# kim.goto(x=-240, y=0)
#
# ben = Turtle(shape="turtle")
# ben.color("blue")
# ben.penup()
# ben.goto(x=-240, y=50)
#
# paul = Turtle(shape="turtle")
# paul.color("purple")
# paul.penup()
# paul.goto(x=-240, y=100)
#
# ken = Turtle(shape="turtle")
# ken.color("yellow")
# ken.penup()
# ken.goto(x=-240, y=150)


screen.exitonclick()
