import turtle
window = turtle.Screen()
window.bgcolor("green")
brad = turtle.Turtle()
brad.shape("arrow")
brad.color("yellow")
brad.speed(100)
for i in range (1,37):
    brad.circle(30)
    brad.right(10)
for i in range (1,19):
    for j in range (1,4):
        brad.forward(100)
        brad.right(120)
    brad.right(20)
brad.right(90)
brad.forward(200)
    
    
