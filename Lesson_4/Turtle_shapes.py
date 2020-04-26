import turtle
s = turtle.getscreen()
t = turtle.Turtle()
for _ in range(4):
	t.forward(100)
	t.right(90)

for _ in range(2):
	t.forward(100)
	t.right(90)
	t.forward(50)
	t.right(90)

t.circle(20)
t.dot(20)