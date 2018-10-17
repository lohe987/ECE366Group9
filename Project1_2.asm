.data
	# 0: T: .word 12
	# 1: T: .word 0xABCDEF00
	# 2: T: .word -5
	T: 32 #0x2000
	best_matching_score: .word -1 #0x2004
	best_matching_count: .word -1 #0x2008
	# 0: Pattern_Array: .word 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20
	# 1: Pattern_Array: .word 0, 1, 2, 3, 4, -1, -2, -3, -4, 0xEEEEEEEE, 0x44448888, 0x77777777, 0x33333333, 0xAAAAAAAA, 0xFFFF0000, 0xFFFF, 0xCCCCCCCC, 0x66666666, 0x99999999
	# 2: Pattern_Array: .word 1, -2, 3, -4, 5, -6, 7, -8, 9, -10, -5, 5, -5, 5, -5, 1, -2, 3, -4, 5
	Pattern_Array: .word 32, 24, 32, 32, 32, 32, 32, 32, 32, 23, 32, 24, 32, 32, 32, 32, 32, 32, 32, 23
.text
	addi $s0, $0, 19		# set main counter
	lw   $s1, T($0)			# load target
MAIN_CHECK:
	beq $s0, -1, DONE		# if maincounter == 0 done
	# load value from array
	sll $t0, $s0, 2			# array_pointer = maincounter * 4 
	addi $a0, $s1, 0		# load target to argument 1
	lw   $a1, Pattern_Array($t0)	# load pattern from array
	jal CHECK_PATTERN		# v0 = how_many_bits_matched
	lw $t0, best_matching_score($0)	# load the current best score
	beq $v0, $t0, MAIN_MATCH	# matching best scores
	slt $t0, $v0, $t0		# new_score < current_best then t0 = 1
	beq $t0, 0, MAIN_BETTER		# if new_score is better then update the better
	j MAIN_UPDATE			# if not better and not matching just update 
MAIN_BETTER:
	addi $t0, $0, 1
	sw $t0, best_matching_count($0)	# best_matching_count = 1
	sw $v0, best_matching_score($0)	# take the return value and make it the best matching score
	j MAIN_UPDATE
MAIN_MATCH:
	lw $t0, best_matching_count($0)	# load the current matching count
	addi $t0, $t0, 1		# best_matching_count++
	sw $t0, best_matching_count($0)	# save best_matching_count
	j MAIN_UPDATE
MAIN_UPDATE:
	addi $s0, $s0, -1
	j MAIN_CHECK
###################################
# a0 = pattern to check against
# a1 = pattern to check for
# v0 = matching score
CHECK_PATTERN:
	addi $t0, $0, 32		# set counter 
	addi $v0, $0, 0			# reset v0
CHECK_PATTERN_CHECK:
	bne $t0, $0, CHECK_PATTERN_LOOP	# if counter != do the loop
	jr $ra
CHECK_PATTERN_LOOP:
	andi $t1, $a0, 0x00000001	# bit mask grab the first bit
	andi $t2, $a1, 0x00000001	# bit mask grab the first bit
	bne $t1, $t2, CHECK_PATTERN_NOT_EQUAL
	addi $v0, $v0, 1
CHECK_PATTERN_NOT_EQUAL:
	srl $a0, $a0, 1			# shift the bits right by one and save it back
	srl $a1, $a1, 1			# shift the bits right by one and save it back
	addi $t0, $t0, -1		# counter--
	j CHECK_PATTERN_CHECK
#----------------------------------
DONE:
	addi $v0, $0, 10
	syscall 









