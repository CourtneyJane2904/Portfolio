# Problem: Check if any of three numbers is equal to the square of the other two summed
# Input: a as an integer from 1 to 100 
# Input: b as an integer from 1 to 100 
# Input: c as an integer from 1 to 100 

import sys

# check if user has supplied 3 integers as arguments with the script, if so assign values to a, b and c accordingly.

def argv_check():
	global a,b,c
	args_len = len(sys.argv)

	# if the user has provided a commandline argument to the script, check if this is a valid integer value and exit if it's not
	# if only the title of the script was passed to Python, draw 4 squares by default.
	
	if args_len == 4:
		for arg in range(1,args_len):
			try:
				arg_supplied = int(sys.argv[arg])
				if arg_supplied < 0 or arg_supplied > 100 :	raise Exception()
			except:
				print("Please provide an integer value between 1-100.")
				exit(1)
		
		# assign the integer value of arguments 1 to 3 to variables a, b and c respectively
		
		a = int(sys.argv[1]) ; b = int(sys.argv[2]) ; c = int(sys.argv[3])	
		
# determine if a, b or c is the sum of the others and print the result to stdout

def calc(a, b, c):
	if a == (b + c) ** 2 : 
	    answer = 'a is the square of the sum of the others'  
	elif b == (a + c) ** 2 :
	    answer = 'b is the square of the sum of the others'
	elif c == (a + b) ** 2 : 
	    answer = 'c is the square of the sum of the others'
	else :
	    answer = 'No number is the square of the sum of the others'
	print(answer)

if __name__ == "__main__":
	a = 64 ; b = 4 ; c = 4 
	argv_check() ; calc(a,b,c)