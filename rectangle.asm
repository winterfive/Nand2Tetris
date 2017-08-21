//Program: Rectangle.asm
// Draws a filled rectangle at the screen's top left corner
// The rectangle's width is 16 px, height is RAM[0]
// Usage: put a non-negative number (rectangle's height) in RAM[0]

	@R0
	D=M
	@n     // R16
	M=D    // n = RAM[0]

	@i     // R17
	M=0    // i = 0

	@SCREEN
	D=A
	@address    // R18
	M=D    // address = 16384 (base address of hack screen)

(LOOP)
	@i
	D=M
	@n
	D=D-M

	@27
	D;JGT

	@address
	A=M
	M=-1

	@i
	M=M+1

	@32
	D=A

	@address
	M=D+M

	@10
	0;JMP

	@27
	0;JMP
