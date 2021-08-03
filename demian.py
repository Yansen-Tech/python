from turtle import *
import matplotlib.pyplot as plt
import numpy as np
speed(1)
bgcolor("Black")
penup()
goto(-50,60)
pendown()
color("#00adef")
begin_fill()
goto(100,100)
goto(100,-100)
goto(-50,-60)
goto(-50,60)

end_fill()
color("Black")
width(10)
goto(15,-100)
penup()
goto(100,0)
pendown()
goto(-100,0)

done()

t=np.linspace(0,3,5)
print(t)
y=np.array([12,31,45,55,70])
print(y)
plt.plot(t,y)
plt.show()