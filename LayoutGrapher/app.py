from argparse import ArgumentParser
from .layout_reader import read
from .layout_evaluator import evaluate
from .graph_generator import generate

def main():
    args = parse_args()
    data = open(args.input).read()
    keyboard_map = read(args.layout)
    result = evaluate(data, keyboard_map)
    generate(result, keyboard_map)

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', help="File that contains testing data")
    parser.add_argument('-l', '--layout', help="Layout to be tested as string. f.ex. qwerty: -l \"qwertyuiop asdfghjkl; zxcvbnm,./\"")
    return parser.parse_args()

if __name__ == '__main__':
    main()