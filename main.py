import argparse

def is_valid_byte(byte):
    try:
        byte_value = ord(byte)
        return 0 <= byte_value <= 255
    except TypeError:
        return False


class BrainfuckInterpreter:
    def __init__(self):
        self.data = [0] * 30000 
        self.pointer = 0

    def interpret(self, code):
        code_ptr = 0

        while code_ptr < len(code):
            command = code[code_ptr]

            if command == '>':
                self.pointer += 1
            elif command == '<':
                self.pointer -= 1
            elif command == '+':
                self.data[self.pointer] += 1
            elif command == '-':
                self.data[self.pointer] -= 1
            elif command == '[':
                if self.data[self.pointer] == 0:
                    depth = 1
                    while depth > 0:
                        code_ptr += 1
                        if code[code_ptr] == '[':
                            depth += 1
                        elif code[code_ptr] == ']':
                            depth -= 1
                else:
                    pass
            elif command == ']':
                if self.data[self.pointer] != 0:
                    depth = 1
                    while depth > 0:
                        code_ptr -= 1
                        if code[code_ptr] == ']':
                            depth += 1
                        elif code[code_ptr] == '[':
                            depth -= 1
                else:
                    pass
            elif command == '.':
                print(chr(self.data[self.pointer]), end='')
            elif command == ',':
                byte = input("\nEnter a byte: ")
                while not is_valid_byte(byte):
                    print("Invalid byte!")
                    byte = input("Enter a byte: ")
                self.data[self.pointer] = ord(byte)

            code_ptr += 1

code = []
validChars = ['>', '<', '+', '-', '.', ',', '[', ']']

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Bterp',
        description='A simple Brainfuck interpreter'
    )
    parser.add_argument("file", help="A valid text file containing brainfuck code")
    args = parser.parse_args()

    code = ""
    with open(args.file) as file:
        for line in file:
            for letter in line:
                if letter in validChars:
                    code += letter
    

    interpreter = BrainfuckInterpreter()
    interpreter.interpret(code)