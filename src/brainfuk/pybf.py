# PyBrainfuck
# My implementation of a Brainfuck interpreter in Python
# Has come cool thingies added onto it so its just simply better


# Imports
import argparse


# Definitions
class AsciiInt(int):
    """An integer that has a range of 0-255"""
    
    # Modify addition and subtraction
    
    def __add__(self, other: int) -> int:
        res = super(AsciiInt, self).__add__(other)
        return self.__class__(min(max(res, 0), 255))
    
    
    def __sub__(self, other: int) -> int:
        res = super(AsciiInt, self).__sub__(other)
        return self.__class__(min(max(res, 0), 255))


def interpret(code: str) -> None:
    """Interpret the code"""
    
    memory = []
    pointer = 0
    
    for char in code:
        match char:
            case '+':
                memory[pointer] += 1
            case '-':
                memory[pointer] -= 1


def main(f: str, e: str, r: int) -> None:
    """Execute PyBrainfuck"""
    
    # Interpret a file
    if f is not None:
        with open(f, 'r') as file:
            c = ''.join(filter(lambda x: x in "+-<>.,[]", file.read()))
        interpret(c)
    
    # Interpret a string
    elif e is not None:
        interpret(e)


# Run
if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="PyBrainfuck interpreter")
    parser.add_argument("-f", help="File to interpret", type=str, default=None)
    parser.add_argument("-e", help="Evaluate a string", type=str, default=None)
    parser.add_argument("-r", help="Set the recursion limit", type=int, default=10000)
    args = parser.parse_args()

    # Run main function
    main(**args.__dict__)