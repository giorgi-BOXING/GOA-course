from turtle import*



#we want to paint a house


#step 1: draw a square
speed(30)
color("green")
width(7)
begin_fill()
forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)
end_fill()
#end of square


#drawing a door

forward (70)
color("brown")
begin_fill()
left(90)
forward(120)  # height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill() 

penup()
goto(150,150)
pendown()
color("yellow")
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
