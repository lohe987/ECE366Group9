.data
	P: .word 1005
	R: .word -1
.text
# MULT ($a0 = number 1, $a1 = number 2) -> $v0 = result
# MOD  ($a0 = Base, $a1 = Mod) -> $v0 = result
MAIN:
	addi $s0, $0, 6		# $s0 = 6 (base number)
	addi $s1, $0, 17	# $s1 = 17 (mod number)
	lw   $s2, P($0)		# $s2 = exponent
	addi $s3, $0, 1		# save value = 1
	addi $s4, $0, 0		# counter = 0
MAIN_LOOP:
	# step 1 in the loop is to check the counter
	beq  $s4, $s2, EXIT	# when counter == exponent finish program
	# step 2 MULTIPLY the saved value ad the base number
	addi $a0, $s0, 0	# $a0 = base number
	addi $a1, $s3, 0	# $a1 = saved value
	jal  MULT		# MULT($a0, $a1)
	# step 3 MOD the result which right now is in v0
	addi $a0, $v0, 0	# number to be modded = MULT($a0, $a1)
	addi $a1, $s1, 0	# mod number = mod number
	jal  MOD		# MOD($a0, $a1)
	# step 4 save the result in the save value and jump back to the loop
	addi $s3, $v0, 0	# save value = MOD($a0, $a1)
	sw   $s3, R($0)
	addi $s4, $s4, 1	# counter = counter + 1
	j    MAIN_LOOP
#################################################
MOD:	# a0 = Base number, a1 = Modulus number, v0 = remainder
	slt $t0, $a1, $a0	# condition to check whether to stop the mod
	bne $t0, $0, MOD_SUB	# branch to the subtraction step if the mod is not less than the base number
	# if it didn't branch then save the remainder into 
	addi $v0, $a0, 0	# v0 = a0
	jr $ra
MOD_SUB:
	sub $a0, $a0, $a1	# remaining = remaining - modulus number 
	beq $0, $0, MOD		# loop back
#------------------------------------------------
#################################################
MULT:	# a0 = one number, a1 = one number, v0 = answer
	bne $a0, $0, MULT_STEP
	addi $v0, $t0, 0
	jr $ra
MULT_STEP:
	add $t0, $t0, $a1
	addi $a0, $a0, -1
	j MULT
#------------------------------------------------
EXIT:
	addi $v0, $0, 10
	syscall 
