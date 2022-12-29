from utils.utils import get_input
import argparse

DAY = 6 # update this each day. 

def solve1():
    data = get_input(DAY,'txt')
    signal = data[0]

    for i in range(3,len(signal)):
        segment = signal[i-3:i+1]
        if len(set(segment)) == 4:
            print(i+1)
            break


def solve2():
    data = get_input(DAY,'txt')
    signal = data[0]

    for i in range(13,len(signal)):
        segment = signal[i-13:i+1]
        if len(set(segment)) == 14:
            print(i+1)
            break

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-p',default = 'both')
    args = arg_parser.parse_args()
    puzzle = args.p
    if puzzle == '1':
        print('----------------------')
        print('Puzzle nbr 1:')
        solve1()
    elif puzzle == '2':
        print('----------------------')
        print('Puzzle nbr 2:')
        solve2()
    else:
        print('----------------------')
        print('Puzzle nbr 1:')
        solve1()
        print('----------------------')
        print('Puzzle nbr 2:')
        solve2()