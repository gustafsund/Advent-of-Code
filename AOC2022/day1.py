from utils.utils import get_input
import argparse
import numpy as np
DAY = 1

def solve1():
    data = get_input(DAY,'txt')
    elves = []
    s = 0
    for x in data:
        if x == '\n':
            elves.append(s)
            s = 0
        else:
            s += int(x.rstrip('\n')) 
    print(f'Heaviest loaded elf: {np.argmax(elves)+1}')
    print(f'Heaviest load: {max(elves)}')

def solve2():
    data = get_input(DAY,'txt')
    elves = []
    s = 0
    for x in data:
        if x == '\n':
            elves.append(s)
            s = 0
        else:
            s += int(x.rstrip('\n'))
    top3 = sum(sorted(elves)[-3:])
    print(f'Top 3 loads combined: {top3}')

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-p',default = 'both')
    args = arg_parser.parse_args()
    puzzle = args.p
    if puzzle == '1':
        print('Puzzle nbr 1:')
        solve1()
    elif puzzle == '2':
        print('Puzzle nbr 2:')
        solve2()
    else:
        print('Puzzle nbr 1:')
        solve1()
        print('Puzzle nbr 2:')
        solve2()







