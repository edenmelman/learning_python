import turtle
import random

def change_color():
	ran_num = random.randint(1,50)
	if ran_num % 2 == 0:
		t.color("red")
	if ran_num % 3 == 0:
		t.color("green")
	if ran_num % 5 == 0:
		t.color("yellow")
	if ran_num % 7 == 0:
		t.color("purple")
	else:
		t.color("blue")

#def draw_a_drop(size):


turtle.title("Pure Art")
t = turtle.Turtle()
t.left(20)
t.forward(30)

for _ in range(60):
	t.right(4)
	t.forward(1)
t.left(10)
t.forward(30)

