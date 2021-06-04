class VM:
    def __init__(self, code):
        self.code = code
        self.sp = -1 # Stack Pointer
        self.pc = -1 # Program Counter
        self.instruction = 0
        self.data = 0
        self.stack = [None] * 5
        self.registers = {'a':None, 'b':None, 'c':None, 'd':None, 'pc':-1}

    def advance(self):
        self.registers['pc'] += 1

    def execute(self):
        self.instruction = self.code[self.registers['pc']]
        self.do_primitive()

    def push(self, data):
        self.sp += 1
        self.stack[self.sp] = data

    def pop(self):
        self.stack[self.sp] = None
        self.sp -= 1

    def run(self):
        while self.registers['pc'] < len(self.code) - 1:
            self.advance()
            self.execute()
            #print(self.stack)
            #print(self.registers)

            if self.instruction == 0: # halt
                exit_code = self.get_data()
                print(f"Exited with exit code {exit_code}")
                break

    def get_data(self):
        self.advance()
        return self.code[self.registers['pc']]

    def do_primitive(self):
        if self.instruction == 1: # push
            value = self.get_data()
            print(f"PSH {value}")
            self.push(value)

        if self.instruction == 2: # pop
            print(f"POP")
            self.pop()

        if self.instruction == 3: # add
            op1 = self.stack[self.sp - 1]
            op2 = self.stack[self.sp]
            ans = op1 + op2
            print(f"ADD {op1} + {op2} = {ans}")
            self.pop()
            self.pop()
            self.push(ans)

        if self.instruction == 4: # subtract
            op1 = self.stack[self.sp - 1]
            op2 = self.stack[self.sp]
            ans = op1 - op2
            print(f"SUB {op1} - {op2} = {ans}")
            self.pop()
            self.pop()
            self.push(ans)

        if self.instruction == 5: # divide
            op1 = self.stack[self.sp - 1]
            op2 = self.stack[self.sp]
            ans = op1 / op2
            print(f"DIV {op1} / {op2} = {ans}")
            self.pop()
            self.pop()
            self.push(ans)

        if self.instruction == 6: # multiply
            op1 = self.stack[self.sp - 1]
            op2 = self.stack[self.sp]
            ans = op1 * op2
            print(f"MUL {op1} * {op2} = {ans}")
            self.pop()
            self.pop()
            self.push(ans)

        if self.instruction == 7: # log
            if self.data == 0:
                print(self.stack[self.sp])

        if self.instruction == 8: # set
            reg = self.get_data()
            data = self.get_data()
            print(f"SET {reg} TO {data}")
            self.registers[reg] = data

        if self.instruction == 9: # mov
            reg_1 = self.get_data()
            reg_2 = self.get_data()
            print(f"MOV {reg_1} TO {reg_2}")
            self.registers[reg_1] = self.registers[reg_2]
            self.registers[reg_2] = None

        if self.instruction == 10: # gld
            reg = self.get_data()
            print(f"GLD {reg}")
            self.push(self.registers[reg])
            self.registers[reg] = None
        
        if self.instruction == 11: # gpt
            reg = self.get_data()
            print(f"GPT {reg}")
            self.registers[reg] = self.stack[self.sp]