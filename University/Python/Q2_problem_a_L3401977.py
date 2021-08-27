#!/usr/bin/python3

import sys

# Takes a series of positive numbers and converts them into their corresponding shoe sizes

# check if user has supplied measurements in inches

def valid_inches():

	inches = []
	
	# initialize the input list with given values
	try:
		for arg in sys.argv[1::]:
			if float(arg) > 0:	inches.append(float(arg))
			else:	raise Exception()
		#inches = [float(arg) for arg in sys.argv[1::] if float(arg) > 0]
		if len(inches) == 0:	raise Exception()
	except:
		print("Usage: ./Q2_problem_a_L3401977.py <positive integer/float values separated by spaces>")
		print("e.g. ./Q2_problem_a_L3401977.py 1 2.7 4.5 13\n")

		print("Please provide atleast one positive integer or float value.")
		exit(1)
	
	return inches

# *args is so the function can accomodate a variable length of arguments
# passed parameters are stored in an array called inches

def convert_to_shoe_size(inches=[],*args):

	# initialise the output_list to the empty list
	# transform the input_value into an output_value
	# append the output_value to the output_list
	shoe_sizes = [round(m * 2) / 2 for m in inches]

	# print the output_list
	return print("Conversion results:",str(inches),"=>",str(shoe_sizes))

if __name__ == "__main__":

	# valid_inches() returns an array assigned to the name inches
	convert_to_shoe_size(valid_inches())
	exit(0)
