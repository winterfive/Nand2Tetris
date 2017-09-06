# create dict symbolDict
symbolDict = {'SP': '0', 'R0': '0', 'LCL': '1', 'R1': '1', 'ARG': '2', 'R2': '2',
	'THIS': '3', 'R3': '3', 'THAT': '4', 'R4': '4', 'R5': '5', 'R6': '6', 'R7': '7',
	'R8': '8', 'R9': '9', 'R10': '10', 'R11': '11', 'R12': '12', 'R13': '13',
	'R14': '14', 'R15': '15', 'SCREEN': '16384', 'KBD': '24576'}
	
destDict = {'null': '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100',
	'AM': '101', 'AD': '110', 'AMD': '111'}
	
compDict = {'0': '101010', '1': '111111', '-1': '111010', 'D': '001100', 'A': '110000',
	'!D': '001101', '!A': '110001', '-D': '001111', '-A': '110011', 'D+1': '011111',
	'A+1': '110111', 'D-1': '001110', 'A-1': '110010', 'D+A': '000010', 'D-A': '010011',
	'A-D': '000111', 'D&A': '000000', 'D|A': '010101', 'M': '110000', '!M': '110001',
	'-M': '110011', 'M+1': '110111', 'M-1': '110010', 'D+M': '000010', 'D-M': '010011',
	'M-D': '000111', 'D&M': '000000', 'D|M': '010101'}
	
jumpDict = {'null': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT': '100',
	'JNE': '101', 'JLE': '110', 'JMP': '111'}
	
def cleanLine(line):
	
	# remove newline char
    line = line.strip('\n')
    
    # remove in-line comments
    if '/' in line:
	    line = line.split('/')
	    line = line[0]
    
    # remove whitespace from each line
    line = line.strip()
    
    return line
	
def storeSymbol(value, n):
	# Label Declaration
	# Purpose: Place label name & value in Dict
	# Stub: string, int -> null
	
	# remove () from value
	value = value.strip('()')

	# create variable to hold value keyname
	keyName = value

	# replace label with n (line count via arguement)
	value = n + 1

	# place new symbol in Dict
	symbolDict[keyName] = value

def findValueA(value, n):
	# A instruction
	# Purpose: return 16bit binary value of the arguement
	# Stub: string, int -> string

	# remove @ from string
	value = value.strip('@')

	# if symbol in Dict, return value
	if value in symbolDict:
		value = symbolDict[value]

	# change value to an int
	value = int(value)

	# find value in binary
	value = format(value, 'b')

	# if value(len) < 16:
	value = value.zfill(16)

	# return value
	return value
	
def findSymbol(value, n):
	# Symbol Declaration
	# Purpose: return 16bit binary value of argement
	# Stub: string, int -> string
	
	# TODO

def findValueC(value):
	# C Instruction or Jump
	# Purpose: return 16bit binary value of the arguement
	# Stub: string -> string

	# if value is a jump
	if ';' in value:

		# if jump contains dest, comp, and jump
		if '=' in value:
			# parse jump data
			value = value.split(';')
			compAndDest = value[0]
			jump = value[1]

			# parse comp and dest
			compAndDest = compAndDest.split('=')
			dest = compAndDest[0]
			comp = compAndDest[1]

			# find value of a
			a = findAbitValue(comp)

			# find values for comp, jump, dest
			dest = destDict[dest]
			comp = compDict[comp]
			jump = jumpDict[jump]
			
		# jump contains only comp and jump
		else:
			# parse the comp and dest data
			value = value.split(';')
			comp = value[0]
			jump = value[1]
			
			# find value of a
			a = findAbitValue(comp)
			
			# find values for comp, jump, dest
			comp = compDict[comp]
			jump = jumpDict[jump]
			dest = destDict['null']
		
	# value isn't a jump
	else:
		# parse the dest and comp data
		value = value.split('=')
		dest = value[0]
		comp = value[1]
		
		# find value of a
		a = findAbitValue(comp)
		
		# find values for each
		comp = compDict[comp]
		dest = destDict[dest]
		jump = jumpDict['null']
		
	# concatenate parts and store value
	value = ('111' + a + comp + dest + jump)
	
	# return value
	return value
	
def findAbitValue(comp):
	# A Value in a C Instruction
	# Purpose: Find 1bit value for a
	#Stub: string -> string
	
	# find value for a
	if 'M' in comp:
		a = '1'
	else:
		a = '0'
		
	return  a
