# Author: Lee Gainer
# Date: Aug 2017
# Course: NandtoTetris, final project
# Function: Translate any .asm file to binary (.hack)

#!/usr/bin/python

import sys
from helpers import *

# create empty symbol table, dict
# add pre-defined symbols

# 1st Pass - scan program
# 		   - add labels and their values to table

# 2nd Pass - scan program for each instruction
#		   - find binary value for each instruction and place in output file

x = ''

# get name for new file
title = sys.argv[1][0:3]

# concatenate title with ".hack"
title = title + '.hack'

# create hack file to write to
h = open(title, 'w')

# open file.asm to be translated
with open(sys.argv[1], 'r') as f:
    for line in f:

        # strip \n from each line
        line = line.strip('\n')
        
        # if line is a comment
        if '//' in line:
            x = 'comment'
            continue

        # if line is empty
        if not line:
            x = 'empty'
            continue

        # if line is a Register address (label)
        # if line[0] is '@' and line[1].isalpha():
        # 	pass

        # if line is an A instruction
        if line[0] == '@' and line[1].isdigit():
            x = findValueA(line)

        # if line is a C instruction
        if line[0].isalpha() and line[1] == '=':
            x = findValueC(line)

        # write x to hack file
        h.write(x + '\n')

h.close()
