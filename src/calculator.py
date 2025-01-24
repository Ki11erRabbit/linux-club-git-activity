import argparse

def parse_number(token, index):
    return ((lambda: float(token)), index + 1)

def parse_factor(tokens, index):
    number, index = parse_number(tokens[index], index)
    if index == len(tokens):
        return number, index
    operator = tokens[index]
    expr, index = parse_addition(tokens, index + 1)
    return ((lambda: print(number(), operator, expr())), index)

def parse_addition(tokens, index):
    number, index = parse_factor(tokens[index], index)
    if index == len(tokens):
        return number, index
    operator = tokens[index]
    expr, index = parse_factor(tokens, index + 1)
    return ((lambda: print(number(), operator, expr())), index)

def parse_tokens(tokens):
    index = 0
    function, index = parse_addition(tokens, index)
    return function


def parse(string):
    tokens = string.split()
    return parse_tokens(tokens)



def main(expression):
    print(f'I am going to calculate: {expression}')
    parse(expression)()






if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            prog="Calculator",
            description="A simple calculator to teach git"
            )
    parser.add_argument('expression')
    args = parser.parse_args()
    main(args.expression)
