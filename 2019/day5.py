"""
Finally, some notes:
    It is important to remember that the instruction pointer should increase by the number of values in the instruction after the instruction finishes. 
    Because of the new instructions, this amount is no longer always 4.
    Integers can be negative: 1101,100,-1,4,0 is a valid program (find 100 + -1, store the result in position 4).
The TEST diagnostic program will start by requesting from the user the ID of the system to test by running an input instruction - provide it 1, 
the ID for the ship's air conditioner unit.
It will then perform a series of diagnostic tests confirming that various parts of the Intcode computer, like parameter modes, function correctly. 
For each test, it will run an output instruction indicating how far the result of the test was from the expected value, where 0 means the test was successful. 
Non-zero outputs mean that a function is not working correctly; check the instructions that were run before the output instruction to see which one failed.
Finally, the program will output a diagnostic code and immediately halt. This final output isn't an error; an output followed immediately by a halt means the program finished. 
If all outputs were zero except the diagnostic code, the diagnostic program ran successfully.

After providing 1 to the only input instruction and passing all the tests, what diagnostic code does the program produce?
"""
"""
ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode,
                                  omitted due to being a leading zero
"""
def intcode(input):
    with open("2019/day5input.txt", 'r') as f:
        codes = [int(x) for x in f.read().split(",")]
        eip = 0
        while eip < len(codes):
            #check opcode and parameter modes
            #NOTE: will need to change this if we get 2digit opcodes, for now we assume 1,2,3,4 only, so can ignore 2nd digit from the right
            if str(codes[eip])[-2:] == '99':
                print("Halt")
                break
            opcode = str(codes[eip])[-1]
            parameters = padParameters(str(codes[eip])[:-2])

            #ADDITION
            if opcode == '1': #add eip+1(val1), eip+2(val2) -> eip+3 (dest) | inc eip 4
                if parameters[-1] == '1': #immediate mode, codes[eip] == value directly
                    src1 = codes[eip+1]
                else: #position mode, value is at location pointed to by codes[eip+1]
                    src1 = codes[codes[eip+1]]
                if parameters[-2] == '1': #immediate mode, codes[eip] == value directly
                    src2 = codes[eip+2]
                else: #position mode, value is at location pointed to by codes[eip+1]
                    src2 = codes[codes[eip+2]]
                #NOTE
                dst = codes[eip+3]
                codes[dst] = src1 + src2
                eip += 4

            #MULTIPLICATION
            elif opcode == '2': #multiply eip+1(val1), eip+2(val2) -> eip+3 (dest) | inc eip 4
                if parameters[-1] == '1': #immediate mode, codes[eip] == value directly
                    src1 = codes[eip+1]
                else: #position mode, value is at location pointed to by codes[eip+1]
                    src1 = codes[codes[eip+1]]
                if parameters[-2] == '1': #immediate mode, codes[eip] == value directly
                    src2 = codes[eip+2]
                else: #position mode, value is at location pointed to by codes[eip+1]
                    src2 = codes[codes[eip+2]]
                #NOTE
                dst = codes[eip+3]
                codes[dst] = src1 * src2
                eip += 4

            #INPUT
            #NOTE: probably going to have to handle input more directly latter
            elif opcode == '3': #input -> eip+1 (dest) | inc eip 2
                #NOTE
                dst = codes[eip+1]
                codes[dst] = input
                eip += 2

            #OUTPUT
            elif opcode == '4': #ouput -> eip+1 (output) | inc eip 2
                #NOTE
                dst = codes[eip+1]
                try:
                    print(codes[dst])
                except:
                    print(dst)
                eip += 2

            #JUMP IF TRUE
            elif opcode == '5': #jump if true -> if true (i.e. first parameter is non-zero) eip gets set to second parameter
                if parameters[-1] == '1': #immediate mode, codes[eip] == value directly
                    src1 = codes[eip+1]
                else: #position mode, value is at location pointed to by codes[eip+1]
                    src1 = codes[codes[eip+1]]
                if parameters[-2] == '1': #immediate mode, codes[eip] == value directly
                    src2 = codes[eip+2]
                else: #position mode, value is at location pointed to by codes[eip+1]
                    src2 = codes[codes[eip+2]]

                # if non-zero -> set eip to src2 value
                if src1 != 0:
                    eip = src2
                else: # we only inc eip if we didnt set it directly
                    eip += 3

            #JUMP IF FALSE
            elif opcode == '6': #jump if false -> if true (i.e. first parameter is zero) eip gets set to second parameter
                if parameters[-1] == '1': #immediate mode, codes[eip] == value directly
                    src1 = codes[eip+1]
                else: #position mode, value is at location pointed to by codes[eip+1]
                    src1 = codes[codes[eip+1]]
                if parameters[-2] == '1': #immediate mode, codes[eip] == value directly
                    src2 = codes[eip+2]
                else: #position mode, value is at location pointed to by codes[eip+1]
                    src2 = codes[codes[eip+2]]
                
                # if zero -> set eip to src2 value
                if src1 == 0:
                    eip = src2
                else: # we only inc eip if we didnt set it directly
                    eip += 3

            #LESS THAN
            elif opcode == '7': # if first parameter < second parameter -> store 1 in 3rd parameter
                if parameters[-1] == '1': #immediate mode, codes[eip] == value directly
                    src1 = codes[eip+1]
                else: #position mode, value is at location pointed to by codes[eip+1]
                    src1 = codes[codes[eip+1]]
                if parameters[-2] == '1': #immediate mode, codes[eip] == value directly
                    src2 = codes[eip+2]
                else: #position mode, value is at location pointed to by codes[eip+1]
                    src2 = codes[codes[eip+2]]
                dst = codes[eip+3]

                # if less than, store 1 in 3rd parameter
                if src1 < src2:
                    codes[dst] = 1
                else:
                    codes[dst] = 0
                
                eip += 4

            #EQUAL
            elif opcode == '8':
                if parameters[-1] == '1': #immediate mode, codes[eip] == value directly
                    src1 = codes[eip+1]
                else: #position mode, value is at location pointed to by codes[eip+1]
                    src1 = codes[codes[eip+1]]
                if parameters[-2] == '1': #immediate mode, codes[eip] == value directly
                    src2 = codes[eip+2]
                else: #position mode, value is at location pointed to by codes[eip+1]
                    src2 = codes[codes[eip+2]]
                dst = codes[eip+3]

                # if less than, store 1 in 3rd parameter
                if src1 == src2:
                    codes[dst] = 1
                else:
                    codes[dst] = 0
                
                eip += 4

            #HALT
            else: #opcode was 99 or something is broken -> halt
                break

#adds leading 0s to parameters: 10 -> 00010 (since these are always 3 ones or zeroes + opcode)
def padParameters(param):
    while len(param) < 3:
        param = '0' + param
    return param

# intcode(1) #The TEST diagnostic program will start by requesting from the user the ID of the system to test by running an input instruction - provide it 1
intcode(5)
