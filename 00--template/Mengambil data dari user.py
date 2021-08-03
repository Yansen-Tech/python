import  turtle

t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor('black')
t.width(0)
t.speed(1000)

col=("red","purple","green","orange")

for i in range (5000):
    t.pencolor (col[1%4])
    t.forward(i*4)
    t.right(137)

turtle.done()
