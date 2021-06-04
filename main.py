from vm import VM


def compile(text):
    mapping = {
        'hlt':0,
        'psh':1,
        'pop':2,
        'add':3,
        'sub':4,
        'div':5,
        'mul':6,
        'log':7,
        'set':8,
        'mov':9,
        'gld':10,
        'gpt':11,
        'if':12
    }
    compiled = []
    for i in text:
        if type(i) is str and i.isnumeric():
            compiled.append(int(i))
        elif type(i) is str and len(i) > 1:
            compiled.append(mapping[i])
        else:
            compiled.append(i)
    return compiled


def lexer(text):
    pos = -1
    words = []
    cur = ''
    while pos < len(text) - 1:
        pos += 1
        char = text[pos]

        if char.isalpha():
            cur += char

        if char.isnumeric():
            cur += char
        
        if char.isspace() or char == '\n':
            words.append(cur)
            cur = ''
    words.append(cur)

    return words
    

def get_text(file):
    with open(file, 'r') as f:
        text = f.read()
    
    return text

'''
REGISTERS:
    A => GENERAL PURPOSE
    B => GENERAL PURPOSE
    C => GENERAL PURPOSE
    D => GENERAL PURPOSE

INSTRUCTIONS:
    0 => HLT => STOPS PROGRAM

    1 => PSH => PUSHES TO TOP OF STACK
    2 => POP => POPS FROM TOP OF STACK

    3 => ADD => ADDS TOP TWO NUMBERS ON STACK
    4 => SUB => SUBS TOP TWO NUMBERS ON STACK
    5 => DIV => DIVS TOP TWO NUMBERS ON STACK
    6 => MUL => MULTS TOP TWO NUMBERS ON STACK

    7 => LOG => OUTPUTS TOP OF STACK TO CONSOLE

    8 => SET => SETS REGISTER
    9 => MOV => MOVES VALUE FROM ONE REGISTER TO ANOTHER REGISTER
    10 => GLD => LOADS REGISTER TO THE STACK
    11 => GPT => PUSHES TOP OF STACK TO GIVEN REGISTER
'''

def main():
    '''
    I'll add an actual Compiler later, the current "compiler" should be enough for now
    '''
    code = [
        'set', 'a', 5,
        'psh', 5,
        'psh', 10,
        'mul',
        'psh', 25,
        'div',
        'gpt', 'a',
        'psh', 5,
        'psh', 20,
        'add',
        'gpt', 'b',
        'gld', 'a',
        'gld', 'b',
        'log',
        'pop',
        'log',
        'hlt', 0
    ]

    text = get_text('test.txt')
    code = lexer(text)
    
    compiled = compile(code)
    vm = VM(compiled)
    vm.run()
    #print(new)


if __name__ == '__main__':
    main()