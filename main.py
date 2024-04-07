import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--boolargument', default=False, help='флаг включения чего-то', type=bool)
parser.parse_args()
print(parser.boolargument)
