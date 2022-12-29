from utils.utils import get_input
import argparse

DAY = 10 # update this each day. 

def solve1():
    data = get_input(DAY,'txt')
    xvals = [1]
    pausing = False
    addage = 0
    l = len(data)
    i = 0
    while i < l:
        line = data[i]
        if pausing:
            i += 1
            x = xvals[-1] + addage
            xvals.append(x)
            pausing = False
        elif line[:4] == 'addx':
            x = xvals[-1]
            xvals.append(x)
            addage = int(line.split(' ')[1])
            pausing = True
        elif line == 'noop':
            i += 1
            x = xvals[-1]
            xvals.append(x) 
    xvals = xvals[1:]
    print(len(xvals))
    periods = [20,60,100,140,180,220]
    for i in periods:
        print(i,xvals[i-1])
    print()
    sol = sum([i*xvals[i-1] for i in periods])
    print(sol)

        



def solve2():
    data = get_input(DAY,'txt')

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