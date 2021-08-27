#!/usr/bin/python
# shebang lets a Linux machine know to run this file with python

# import turtle module
from turtle import *
# import sys module to allow interaction between Python and Bash (in my case)
import sys

my_turtle = Turtle(shape="turtle")
square_quantity = 4

# I'm trying to segregate code to different functions as it looks tidier but also makes debugging alot easier

def argv_check():
	global square_quantity
	args_len = len(sys.argv)

	# if the user has provided a commandline argument to the script, check if this is a valid integer value and exit if it's not
	# if only the title of the script was passed to Python, draw 4 squares by default.
	
	if args_len == 2:
		arg_supplied = int(sys.argv[1])
		if isinstance(arg_supplied, int):
			square_quantity = arg_supplied
		else:
			print("Please provide an integer value for the number of desired squares or let it default to 4.")
			exit(1)

def staircase(xpos,line_l):
	# manipulate the global variable my_turtle- don't look for a local variable named my_turtle
	global my_turtle
	if xpos == "r":
		my_turtle.rt(90)
		my_turtle.fd(line_l)
		my_turtle.lt(90)
		my_turtle.fd(line_l)
	else:
		my_turtle.lt(90)
		my_turtle.fd(line_l)
		my_turtle.rt(90)
		my_turtle.bk(line_l)


def draw_squares(sq):
	global my_turtle
	# position the turtle in the bottom left hand corner of the screen
	my_turtle.pu() ; my_turtle.setpos(-320, -300)
	# rotate turtle 90 degrees left from its default starting position
	my_turtle.lt(90)
	# save the Screen object to the variable scr: this is used to alter properties of the popup window
	scr = Screen()
	# begin sketching by putting the pen down
	my_turtle.pd()
	line_len = 20
	# easiest way will be to draw the squares in two 'staircases': this is easy to loop  
	for i in range(0,2):
		for s in range(0,sq):
			if i == 0:
				staircase("r", line_len)
				# do not add 20 if this these are lines of the last quare: as it's added after the staircase function, this will cause the first line of the left staircase to be longer
				if s != (sq-1): line_len += 20
			else:
				staircase("l", line_len)
				if s != (sq-1): line_len -= 20
	# exit on click rather than automatically
	scr.exitonclick()

# code will only execute if the file is called directly as opposed to being included as a module in another script
# although irrelevant in this scenario, it seems like a good practice
if __name__ == "__main__":
	argv_check()
	draw_squares(square_quantity)