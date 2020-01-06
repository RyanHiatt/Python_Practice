#Converting to a command line interface
#Runs in command line
#argparse means argument parser

import argparse
import sys
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='add',
                        help='What operation? (add, sub, mul, or div')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):

    if args.operation == 'add':
        return x + y
    elif args.operation == 'sub':
        return x - y
    elif args.operation == 'mul':
        return x * y
    elif args.operation == 'div':
        return x / y

if __name__ == '__main__':
    main()