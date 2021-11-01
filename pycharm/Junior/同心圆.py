import turtle as t

cx,cy=0,0
r=100
d=20

colors=["red","orange","yellow","green"]

for c in colors:
    t.pu()
    t.goto(cx,cy-r)
    t.pd()
    t.pencolor(c)
    t.circle(r)
    r+=d