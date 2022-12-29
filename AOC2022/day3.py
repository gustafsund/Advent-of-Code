from utils.utils import get_input
import argparse

DAY = 3 # update this each day. 
ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority = {ALPHABET[i]: i+1 for i in range(len(ALPHABET))}

def solve1():
    data = get_input(DAY,'txt')
    prio_sum = 0
    for x in data:
        if x != '\n':
            contents = x.rstrip('\n')
            nbr_items = len(contents)
            comp1,comp2 = contents[:nbr_items//2], contents[nbr_items//2:]
            for element in comp1:
                if element in comp2:
                    prio_sum += priority[element]
                    break
    print(f'Sum of priorities: {prio_sum}')



def solve2():
    data = get_input(DAY,'txt')
    prio_sum = 0
    for i in range(0,len(data),3):
        pack1 = data[i].rstrip('\n')
        pack2 = data[i+1].rstrip('\n')
        pack3 = data[i+2].rstrip('\n')
        
        for item in pack1:
            if item in pack2 and item in pack3:
                prio_sum += priority[item]
                break
    print(f'Sum of priorities: {prio_sum}')


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