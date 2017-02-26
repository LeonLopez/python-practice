import turtle

def draw_shape(brad):
	for i in range(1,5):

		brad.forward(100)
		brad.right(90)

def draw_art():

	window = turtle.Screen()
	window.bgcolor('red')

	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.speed(7)
	brad.color('blue')
	for j in range(1,37):
		draw_shape(brad)
		brad.right(10)

	window.exitonclick()

draw_art()