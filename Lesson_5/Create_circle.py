import turtle
import math as m

turtle.title("Pure Art")
t = turtle.Turtle()


def create_drop(length,alpha):
	linear_steps = (length) * m.tan(m.radians(45 - (alpha / 2)))
	print(linear_steps)
	t.left(alpha)
	t.forward(linear_steps)


	radius = length * m.tan(m.radians(alpha)) * m.tan(m.radians(45 - (alpha / 2)))
	diameter = 2 * radius
	full_circle_steps = 2 * m.pi * radius
	angle_per_step = diameter / 360
	remaining_circle_steps = full_circle_steps * ((1 + m.sin(m.radians(alpha))) / 2)
	print (remaining_circle_steps)

	for _ in range(int(remaining_circle_steps)):
		t.right(angle_per_step)
		t.forward(1)


create_drop(70,20)

