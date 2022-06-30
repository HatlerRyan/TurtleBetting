from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
user_bet = screen.textinput("Make your bet!", "Which turtle will win the race? Enter the color! ")
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
height_needed = len(colours) * 100
screen.setup(500, height_needed)
coloured_turtles = {}
even_turtle_position = 0
odd_turtle_position = 0


for colour in colours:
    new_turtle = Turtle()
    new_turtle.name = colour
    new_turtle.color(colour)
    new_turtle.shape("turtle")
    new_turtle.penup()
    # print(new_turtle.name)
    coloured_turtles[new_turtle] = new_turtle.name
    if len(coloured_turtles) == 1:
        new_turtle.goto(-230, 0)
    elif len(coloured_turtles) % 2:
        even_turtle_position += 25
        new_turtle.goto(-230, even_turtle_position)
        # print(even_turtle_position)
    else:
        odd_turtle_position -= 25
        new_turtle.goto(-230, odd_turtle_position)
rand_distance = random.randint(0, 10)
# print(coloured_turtles)
if user_bet:
    is_race_on = True

while is_race_on:
    for moving_turtle in coloured_turtles:
        # if user_bet == moving_turtle.name:
        #     moving_turtle.forward(10)
        # print(moving_turtle.name)
        rand_distance = random.randint(0, 10)
        moving_turtle.forward(rand_distance)
        if moving_turtle.xcor() > 230:
            if user_bet == moving_turtle.name:
                is_race_on = False
                screen.textinput('Congrats! ', f'The {moving_turtle.name} turtle won. ').lower

            else:
                is_race_on = False
                screen.textinput(f'Too bad, the {moving_turtle.name} turtle won. ', 'Better luck next time').lower


# print(coloured_turtles)
#
#
# # tim = Turtle()
# # tim.shape("turtle")
# # tim.color("blue")
# # tim.speed(0)
# # tim.penup()
# # tim.goto(-230,0)
# # def move_forwards():
# #     tim.forward(100)
# # def move_backwards():
# #     tim.backward(100)
# # def turn_left():
# #     new_heading = tim.heading() + 10
# #     tim.setheading(new_heading)
# # def turn_right():
# #     new_heading = tim.heading() - 10
# #     tim.setheading(new_heading)
# # def clear_screen():
# #     tim.clear()
# #     tim.penup()
# #     tim.home()
# #     tim.pendown()
# # screen.listen()
# # screen.onkeypress(move_forwards, "w")
# # screen.onkeypress(move_backwards, "s")
# # screen.onkeypress(turn_left, "a")
# # screen.onkeypress(turn_right, "d")
# # screen.onkeypress(clear_screen, "c")
#
screen.exitonclick()
