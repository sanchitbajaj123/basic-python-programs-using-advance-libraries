import turtle
import time
vatsal = turtle.Turtle()
#turtle.delay(2)
vatsal.pensize(7)
turtle.Screen().bgcolor("#F5F5DC")
vatsal.speed(10)

# Move the turtle to the extreme left position
vatsal.penup()
vatsal.setposition(-200,-75)


# Draw the rectangle
vatsal.fillcolor("#46523C")
vatsal.begin_fill()
vatsal.pendown()
vatsal.forward(400)
vatsal.setheading(90)
vatsal.forward(150)
vatsal.setheading(180)
vatsal.forward(400)
vatsal.setheading(-90)
vatsal.forward(150)
vatsal.end_fill()

# Draw the left tire
vatsal.fillcolor("black")
vatsal.begin_fill()
vatsal.penup()
vatsal.setposition(-175,-75)
vatsal.pendown()
vatsal.forward(50)
vatsal.setheading(0)
vatsal.forward(75)
vatsal.setheading(90)
vatsal.forward(50)
vatsal.end_fill()

# Draw the right tire
vatsal.penup()
vatsal.setposition(100,-75)
vatsal.fillcolor("black")
vatsal.begin_fill()
vatsal.pendown()
vatsal.setheading(270)
vatsal.forward(50)
vatsal.setheading(0)
vatsal.forward(75)
vatsal.setheading(90)
vatsal.forward(50)
vatsal.end_fill()

# Draw the uppermost line

vatsal.penup()
vatsal.setposition(-137.5,200)
vatsal.pendown()
vatsal.setheading(0)
vatsal.forward(275)

# Draw the second uppermost line
vatsal.penup()
vatsal.setposition(-150,150)
vatsal.pendown()
vatsal.setheading(0)
vatsal.forward(300)

# Draw the left slanted line
vatsal.penup()
vatsal.setposition(-137.5,200)
vatsal.pendown()
vatsal.setposition(-175,75)

# Draw the right slanted line
vatsal.penup()
vatsal.setposition(137.5,200)
vatsal.pendown()
vatsal.setposition(175,75)

# Draw the left circle

vatsal.penup()
vatsal.setposition(-125,-25)
vatsal.pendown()
vatsal.fillcolor("#ECFFDC")
vatsal.begin_fill()
vatsal.circle(25)
vatsal.end_fill()
# Draw the right circle
vatsal.penup()
vatsal.setposition(125,-25)
vatsal.pendown()
vatsal.fillcolor("#ECFFDC")
vatsal.begin_fill()
vatsal.circle(25)
vatsal.end_fill()

# Draw the left wiper
vatsal.penup()
vatsal.setposition(-87.5, 75)
vatsal.pendown()
vatsal.setposition(-50, 112.5)

# Draw the right wiper
vatsal.penup()
vatsal.setposition(62.5, 75)
vatsal.pendown()
vatsal.setposition(100, 112.5)

# Draw the horizontal lines
vatsal.penup()
vatsal.setposition(-50, -37.5)
vatsal.pendown()
vatsal.setposition(-50, 0)
vatsal.penup()
vatsal.setposition(-15, -37.5)
vatsal.pendown()
vatsal.setposition(-15, 0)
vatsal.penup()
vatsal.setposition(15, -37.5)
vatsal.pendown()
vatsal.setposition(15, 0)
vatsal.penup()
vatsal.setposition(50, -37.5)
vatsal.pendown()
time.sleep(3)
turtle.Screen().bye()
