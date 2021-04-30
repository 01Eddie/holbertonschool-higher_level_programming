#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    s = len(sys.argv) - 1
    if s != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if op == '+':
        r = add(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, r))
    elif op == '-':
        r = int(sub(a, b))
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, r))
    elif op == '*':
        r = mul(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, r))
    elif op == '/':
        r = int(div(a, b))
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, r))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
