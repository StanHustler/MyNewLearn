import turtle

turtle.pensize(2)
for i in range(4):
    turtle.fd(200)
    turtle.left(90)
turtle.left(360 - 45)
turtle.circle(100 * pow(2, 0.5))
input()
