import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--boolargument', '-B', help='флаг включения чего-то')
parser.parse_args()
print(parser.boolargument)
