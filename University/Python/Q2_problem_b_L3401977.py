#!/usr/bin/python3

import sys

# Calculates which shoes are the furthest in length from the target length 

# returns a tuple holding the actual_lens array and target_len float as items

def collect_input():
	target_len = 0 
	actual_lens = [] ; actual_lens_csv = [] ; actual_lens_arr = [] 

	# initialize the input list with given values
	try:
		for a in range(1,len(sys.argv)):
			
			if "," not in sys.argv[a]:
				target_len = float(sys.argv[a])
			else:
				actual_lens_csv.append(sys.argv[a])
			
		actual_lens_arr = ''.join(actual_lens_csv).split(",")
		# initialise the input with a non-empty list
		for arg in actual_lens_arr:
			if float(arg) > 0:	actual_lens.append(float(arg))
			else:	raise Exception()
		if len(actual_lens) == 0 or target_len == 0 or target_len < 0:	raise Exception()
	except:
		print("Usage: ./Q2_problem_b_L3401977.py <target length> <actual lengths in csv format>")
		print("e.g. ./Q2_problem_b_L3401977.py 1,2.4,7,4.5 13\n")
		print("Please provide one positive integer or float for target length and atleast two positive integers or floats for actual lengths.")
		exit(1)
	
	return actual_lens,target_len

def calc_diff(collection=[],*args):
	result = 0

	if isinstance(collection[0],list):
		act_lens = collection[0] ; target = collection[1]
	else:
		act_lens = collection[1] ; target = collection[0]

	for a in act_lens:
		if target > a:	diff = target - a
		else:	diff = a - target
		# set best to the first item in the list
		# if the item is greater than value stored in result:
		if diff > result: result = diff
	return print("The greatest difference is",str(round(result,1)))

if __name__ == "__main__":
	calc_diff(collect_input()) 
