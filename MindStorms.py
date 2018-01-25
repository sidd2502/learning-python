import turtle
window = turtle.Screen()
window.bgcolor("green")

def drawSquare():
    brad1 = turtle.Turtle()
    brad1.shape("turtle")
    brad1.color("yellow")
    brad1.speed(1000)
    angle = 0
    
    while (angle < 360):
        st1 = 0
        brad1.right(angle)
        while (st1 < 4):
            brad1.forward(50)
            brad1.right(90)
            st1 = st1 + 1
        angle = angle + 1
        
def drawCircle():
    brad1 = turtle.Turtle()
    brad1.shape("arrow")
    brad1.color("blue")
    brad1.speed(1000)
    angle = 0
    brad1.forward(200)
    while (angle < 360):
        st1 = 0
        brad1.right(angle)
        while (st1 < 4):
            brad1.circle(20)
            st1 = st1 + 1
        angle = angle + 1

def drawTriangle():
    brad1 = turtle.Turtle()
    brad1.shape("classic")
    brad1.color("grey")
    brad1.speed(1000)
    angle = 0
    brad1.backward(200)
    while (angle < 360):
        st1 = 0
        brad1.right(angle)
        while (st1 < 3):
            brad1.forward(70)
            brad1.right(120)
            st1 = st1 + 1
        angle = angle + 1
        
drawSquare()
drawCircle()
drawTriangle()
