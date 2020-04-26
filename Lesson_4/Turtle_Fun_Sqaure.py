import turtle


turtle.title("Eden's Turtle")
t = turtle.Turtle()
t.pensize(5)
dict = {0: "red",1:"blue", 2: "green",3: "yellow"}

for num in range(4):
	for _ in range(2):
		t.forward(40)
		t.penup()
		t.forward(10)
		t.pendown()
	t.right(90)
	t.color(dict[num])