y_positions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []
for i in range(0,7):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x= -230, y = y_positions[i])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You have won")
            else:
                print("you have lost")
            print(f"The {winning_color} turtle has won" )
        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)


screen.exitonclick()
