from utils.utils import get_input
import argparse

DAY = 4 # update this each day. 

def solve1():
    data = get_input(DAY,'txt')
    count_contains = 0
    for pair in data:
        range1,range2 = pair.split(',')
        lwr1, upr1 = map(int, range1.split('-'))
        lwr2, upr2 = map(int, range2.split('-'))
        if (lwr1 >= lwr2 and upr1<=upr2) or (lwr1 <= lwr2 and upr1>=upr2):
            count_contains += 1
    print(f'Number of overlaps: {count_contains}')



def solve2():
    data = get_input(DAY,'txt')
    count_contains = 0
    for pair in data:
        range1,range2 = pair.split(',')
        lwr1, upr1 = map(int, range1.split('-'))
        lwr2, upr2 = map(int, range2.split('-'))
        bools = [lwr1 <= lwr2 and upr1 >= lwr2,
                    lwr1 <= upr2 and upr1 >= upr2,
                    lwr2 <= lwr1 and upr2>=lwr1,
                    lwr2 <= upr1 and upr2 >= upr1]
        if sum(bools) > 0:
            count_contains += 1
    print(f'Number of overlaps: {count_contains}')

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