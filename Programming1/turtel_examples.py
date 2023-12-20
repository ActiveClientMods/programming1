import turtle

canvas = turtle.Screen()
canvas.bgcolor("white")
draw = turtle.Turtle()
draw.speed(0)


draw.up()
draw.setpos(-30, -50)
draw.down()

for i in range(2):
    draw.forward(360)
    draw.left(90)
    draw.forward(240)
    draw.left(90)

draw.up()
draw.setpos(150, -15)
draw.down()
draw.fillcolor("red")
draw.begin_fill()
draw.circle(80)
draw.end_fill()
draw.hideturtle()
turtle.done()

# Rainbow Benzene

'''
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
canvas.bgcolor('black')
arr_len = len(colors)
for x in range(360):
    draw.pencolor(colors[x % arr_len])
    draw.width(x//100 + 1)
    draw.forward(x)
    draw.left(59)

draw.hideturtle()
turtle.done()

'''
