import turtle

t= turtle.Turtle()
s=turtle.Screen()

s.bgcolor("Black")
t.width(1)
t.speed(5000)

col=("yellow","green","red","blue","orange")

for i in range(5000):
    t.pencolor(col[col[1%8]])
    t.forward(1*8)
    t.right(400)

turtle.done()