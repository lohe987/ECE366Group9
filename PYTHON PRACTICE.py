input_file=open("input_machine_code.txt","r")
output_file=open("Output_assembly_code.txt","w")
for line in input_file:
    opcode = line[1] + line[2] + line[3] + line[4]
    if(opcode=="0000"):
        op_name="SAR"
        register=line[5]+line[6]+line[7]
        print("register_string= ",register)
        register=int(register,2)
        print("register_nam= ",register)
        register=str(register)
        output_file.write(op_name+" "+register+"\n")

    elif (opcode == "0010"):
        op_name = "MOV"
        register = line[5] + line[6] + line[7]
        print("register_string= ", register)
        register = int(register, 2)
        print("register_nam= ", register)
        register = str(register)
        output_file.write(op_name +" "+register+"\n")

    elif (opcode == "0011"):
        op_name = "MOVI"
        register = line[5] + line[6] + line[7]
        print("register_string= ", register)
        register = int(register, 2)
        print("register_nam= ", register)
        register = str(register)
        output_file.write(op_name + " " + register+"\n")

    elif (opcode == "0100"):
        op_name = "AND"
        register = line[5] + line[6] + line[7]
        print("register_string= ", register)
        register = int(register, 2)
        print("register_nam= ", register)
        register = str(register)
        output_file.write(op_name + " " + register+"\n")

    elif (opcode == "0101"):
        op_name = "SLL"
        register = line[5] + line[6] + line[7]
        print("register_string= ", register)
        register = int(register, 2)
        print("register_nam= ", register)
        register = str(register)
        output_file.write(op_name + " " + register+"\n")

    elif (opcode == "0110"):
        op_name = "LD"
        register = line[5] + line[6] + line[7]
        print("register_string= ", register)
        register = int(register, 2)
        print("register_nam= ", register)
        register = str(register)
        output_file.write(op_name + " " + register+"\n")

    elif (opcode == "0111"):
        op_name = "STR"
        register = line[5] + line[6] + line[7]
        print("register_string= ", register)
        register = int(register, 2)
        print("register_nam= ", register)
        register = str(register)
        output_file.write(op_name + " " + register+"\n")

    elif (opcode == "1000"):
        op_name = "ADDI"
        register = line[5] + line[6] + line[7]
        print("register_string= ", register)
        register = register.int
        print("register_nam= ", register)
        register = str(register)
        output_file.write(op_name + " " + register+"\n")

    elif (opcode == "1001"):
        op_name = "SUB"
        register = line[5] + line[6] + line[7]
        print("register_string= ", register)
        register = int(register, 2)
        print("register_nam= ", register)
        register = str(register)
        output_file.write(op_name + " " + register+"\n")

    elif (opcode == "1010"):
        op_name = "BCMP"
        register = line[5] + line[6] + line[7]
        print("register_string= ", register)
        register = int(register, 2)
        print("register_nam= ", register)
        register = str(register)
        output_file.write(op_name + " " + register+"\n")

    elif (opcode == "1011"):
        op_name = "B"
        register = line[5] + line[6] + line[7]
        print("register_string= ", register)
        register = int(register, 2)
        print("register_nam= ", register)
        register = str(register)
        output_file.write(op_name + " " + register+"\n")

    elif (opcode == "1100"):
        op_name = "SRL"
        register = line[5] + line[6] + line[7]
        print("register_string= ", register)
        register = int(register, 2)
        print("register_nam= ", register)
        register = str(register)
        output_file.write(op_name + " " + register+"\n")

    elif (opcode == "1101"):
        op_name = "MLT"
        register = line[5] + line[6] + line[7]
        print("register_string= ", register)
        register = int(register, 2)
        print("register_nam= ", register)
        register = str(register)
        output_file.write(op_name + " " + register+"\n")

    elif (opcode == "1111"):
        op_name = "CMPLT"
        register = line[5] + line[6] + line[7]
        print("register_string= ", register)
        register = int(register, 2)
        print("register_nam= ", register)
        register = str(register)
        output_file.write(op_name + " " + register+"\n")




