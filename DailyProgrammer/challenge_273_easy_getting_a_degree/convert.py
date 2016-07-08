from sys import argv, exit

def typeConversion(string_to_be_converted):
	try:
		return int(string_to_be_converted) 		# tries to convert to int
	except ValueError:
		return float(string_to_be_converted)	# if ValueError is thrown then
												# it is converted to float

def degreeConversion(inputNumber, conversionInformation):
	if conversionInformation == "rd":
		return (inputNumber * 180) / 3.14
	elif conversionInformation == "dr":
		return (inputNumber * 3.14) / 180
	else:
		print "I can't do this conversion."


if(len(argv) != 2): 	# makes sure there is one argument after script call
	print "Input in incorrect format! Ex: 3.14rd."
	exit(0)


_input_ = argv[1] 	# gets input from command line argument

to_be_converted = _input_[0:-2]		# last 2 elements of the list are conversion
									# information, so 0:-2 gets only the number
									# that should be converted

conversionInformation = _input_[-2:] 	# gets conversion information from last
										# 2 elements

numberInput = typeConversion(to_be_converted)


#######	OUTPUT ######

print degreeConversion(numberInput, conversionInformation)



