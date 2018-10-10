# ECE366Group9

This architecture concept is an accumulator-based architecture. 
Details:

- Sixteen instructions
- Eight 16-bit registers
- Implicit destination register assigned with SAR (Set Active Register)
- imm in [-4, 3] for all immediate instructions

- 0000 SAR -- set ra
- 0001 ADD -- ra = ra + rs
- 0010 MOV -- ra = rs
- 0011 AND -- ra = ra & rs
- 0100 SLL -- ra = ra << rs
- 0101 SRL -- ra = ra >> rs
- 0110 LOAD -- ra = M[rs]
- 0111 STOR -- M[rs] = ra
- 1000 SUB -- ra = ra - rs
- 1001 MLT -- ra = ra * rs
- 1010 BSLT -- PC = (ra < rs ? rp : PC + 1)

- 1011 MOVI -- ra = imm
- 1100 ADDI -- ra = ra + imm

- 1101 SPC -- rp = PC + rs

- 1110 B -- PC = rp
- 1111 STOP -- end execution
