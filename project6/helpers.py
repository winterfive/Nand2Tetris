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
n = 0

# get name for new file
title = sys.argv[1]

# split name from file type
title = title.split('.')
title = title[0]

# concatenate title with ".hack"
title = title + '.hack'

# create hack file to write to
h = open(title, 'w')

# open file.asm to be translated
with open(sys.argv[1], 'r') as f:
    
    # first loop: find labels, store labels in table
    for line in f:
        
        if '()' in line:
            x = handleLabelDec(line, n)
            
        n += 1
        
    # reset n
    n = 0
            
    # evaluate all lines, find binary values for each
    for line in f:
        
        # prep line for analysis
        line = prepLine(line)
            
        # if line is an A instruction
        if '@' in line:
            x = findValueA(line, n)

        # if line is a C instruction
        # if line[0].isalpha() and line[1] == '=':
        else:
            x = findValueC(line)

        # write x to hack file
        h.write(x + '\n')
        
        n += 1

h.close()
