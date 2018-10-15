ins_to_op = {
    'SAR': '0000',
    'ADD': '0001',
    'MOV': '0010',
    'AND': '0011',
    'SLL': '0100',
    'SRL': '0101',
    'LOAD': '0110',
    'STOR': '0111',
    'SUB': '1000',
    'MLT': '1001',
    'BSLT': '1010',
    'MOVI': '1011',
    'ADDI': '1100',
    'SPC': '1101',
    'B': '1110',
    'STOP': '1111'
}

def CleanImmediate(value_of_immediate:str)->str:       
    if '-' not in value_of_immediate:
        return format(int(value_of_immediate), '03b')
    return format(0b111 - int(value_of_immediate.replace("-","") ) + 1, '03b')

def AssignParity(line:str)->str:
    num_of_ones = sum(c == '1' for c in line)
    if num_of_ones % 2 != 0:
        return f'1{line}'
    else:
        return f'0{line}'

with open("./program2.txt", "r") as f:
    with open("./machine_encode_2.txt", "w+") as wf:
        for line in f:
            line_list = line.split(' ')
            # clean list by filtering out all spaces
            line_list = [i for i in line_list if i != '' and i != ' ']
            op = '' if line_list[0] not in ins_to_op else ins_to_op[line_list[0]] # get the op code
            if ':' in line or line.isspace() or op == '':
                #wf.write(f'BAD LINE: {line}') # for right now just write the bad lines
                print(f'BAD LINE: {line}')
            elif op == '1111' or op == '1110':
                wf.write('11111111\n') if ins_to_op[line_list[0]] == '1111' else wf.write('01110111\n')
            else:
                immVal = CleanImmediate(line_list[1])
                wf.write(AssignParity(f'{op}{immVal}') + '\n')


