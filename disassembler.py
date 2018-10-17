op_to_ins = {
    '0000': 'SAR',
    '0001': 'ADD',
    '0010': 'MOV',
    '0011': 'AND',
    '0100': 'SLL',
    '0101': 'SRL',
    '0110': 'LOAD',
    '0111': 'STOR',
    '1000': 'SUB',
    '1001': 'MLT',
    '1010': 'BSLT',
    '1011': 'MOVI',
    '1100': 'ADDI',
    '1101': 'SPC',
    '1110': 'B',
    '1111': 'STOP'
}

fileName = 'machine_encode_2'

with open(f'./{fileName}.txt', 'r') as binFile, open(f'./{fileName}_to_asm.txt', 'w+') as asmFile:
    for line in binFile:
        instruction = None
        if line[0] is '#':
            asmFile.write(f'{line}')
            continue
        elif line[1:5] not in op_to_ins:
            print("Error that op code is not linked to an instruction")
            break
        else:
            instruction = op_to_ins[line[1:5]]
        if 'I' in instruction:
            # binary to decimal with sign
            if line[5] is '1':
                asmFile.write(f'{instruction} {-8 + int(line[5:], 2)}\n')
            else:
                asmFile.write(f'{instruction} {int(line[5:], 2)}\n')
        elif instruction is 'B' or instruction is 'STOP':
            asmFile.write(f'{instruction}\n')
        else:
            # binary to decimal no sign
            asmFile.write(f'{instruction} {int(line[5:], 2)}\n')
        
        
