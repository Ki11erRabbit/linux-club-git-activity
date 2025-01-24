import argparse











def main(expression):
    print(f'I am going to calculate: {expression}')






if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            prog="Calculator",
            description="A simple calculator to teach git"
            )
    parser.add_argument('expression')
    args = parser.parse_args()
    main(args.expression)
