import turtle
import pygame 
t = turtle.Pen()
t.pencolor("red")
t.screen.bgcolor("orange")

# t.screen.onclick(turtle.goto) # Subsequently clicking into the TurtleScreen will

# t.left(90)
# t.forward(90)
# t.left(90)

for i in range(19):
    n =3
    fdgree = 90
    rdegree = 60
    ldegree = 120
    distance = 70
    
    t.begin_fill()
    t.forward(distance)
    t.left(fdgree)
    t.color("blue")
    t.end_fill()

    if (n == i):
        n +=3
        t.right(rdegree)
        t.forward(fdgree)
        t.end_fill()


t.screen.mainloop()

#     t.forward(90)
#     t.left(90)
#     t.right(90)
#     t.back(90)
    
