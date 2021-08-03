import turtle
import random
#name=input('Enter your name)

#set background
bg=turtle.Screen()
bg.bgcolor("black")
bg.title(f"HAPPY BIRTHDAY JANE")
#bg.title(f"Happy birthday")

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write("HAPPY BIRTHDAY JANE",align="center",font=("Courier",36,"normal"))

#Bottom line 1
turtle.penup()
turtle.goto(-170,-180)
turtle.color("magenta")
turtle.pendown()
turtle.forward(350)

#Mid line 2
turtle.penup()
turtle.goto(-160,-150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)

#First line 3
turtle.penup()
turtle.goto(-150,-120)
turtle.color("cyan")
turtle.pendown()
turtle.forward(250)

#Cake
turtle.penup()
turtle.goto(-100,-100)
turtle.color("pink")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()



#Candies
turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-60,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(30,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)


#Decoration

colors=["red","orange","yellow","green","blue","purple","black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()


for each_color in colors:
    angle = 360/len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)


#Happy birthday massage

turtle.penup()
turtle.goto(-150,50)
turtle.color("red")
turtle.pendown()
turtle.write("Happy Birhday Jane",None,None,"24pt bold")
turtle.color("red")