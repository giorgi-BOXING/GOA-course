import turtle


screen = turtle.Screen()
screen.bgcolor("black")  


pen = turtle.Turtle()
pen.color("green")       
pen.hideturtle()         
pen.penup()
pen.goto(0, 0)           
pen.write("GOA", align="center", font=("Arial", 100, "bold"))


turtle.done()