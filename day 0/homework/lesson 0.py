from turtle import*



#we want to paint a house


#step 1: draw a square
speed(30)
color("purple")
width(7)
forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)
#end of square


#drawing a door

forward (70)
color("yellow")
left(90)
forward(120)  # height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("red")
right(150)
forward(200)
left(120)
forward(200) 
forward(10)
penup()
goto(150,150)
pendown()
left(120)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
penup()
goto(50,150)
pendown()
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)



exitonclick()
