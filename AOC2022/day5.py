from utils.utils import get_input
import argparse
from queue import LifoQueue

DAY = 5 # update this each day. 

def show_stacks(queue_lists):
    print()
    print()
    for i,line in enumerate(queue_lists):
        print(f'{i+1}  {line}')

def setup_lists(data):
    queue_lists = []
    for i in range(9):
        append_list = ''
        for x in data[:8]:
            app = x[4*i+1]
            if app != ' ':
                append_list += app
        queue_lists.append(append_list[::-1])

    print('setup')
    show_stacks(queue_lists)
    return queue_lists

def perform_action(action,queue_lists):

    _,move,__,from_pile,___,to_pile = action.split()
    move = int(move)
    from_pile = int(from_pile) - 1
    to_pile = int(to_pile) - 1 

    for i in range(move):
        queue_lists[to_pile] += queue_lists[from_pile][-1]
        queue_lists[from_pile] = queue_lists[from_pile][:-1]
    return queue_lists

def solve1():
    data = get_input(DAY,'txt')
    queue_lists = setup_lists(data)
    actions = data[10:]
    for i,action in enumerate(actions):
        queue_lists = perform_action(action,queue_lists)
    print('end')
    show_stacks(queue_lists)
    top_blocks = []
    for q in queue_lists:
        if len(q) > 0:
            top_blocks.append(q[-1])
    print(*top_blocks,sep='')


def perform_action2(action,queue_lists):

    _,move,__,from_pile,___,to_pile = action.split()
    move = int(move)
    from_pile = int(from_pile) - 1
    to_pile = int(to_pile) - 1 

    queue_lists[to_pile] += queue_lists[from_pile][-move:]
    queue_lists[from_pile] = queue_lists[from_pile][:-move]

    return queue_lists

def solve2():
    data = get_input(DAY,'txt')
    queue_lists = setup_lists(data)
    actions = data[10:]
    for i,action in enumerate(actions):
        queue_lists = perform_action2(action,queue_lists)
    print('end')
    show_stacks(queue_lists)
    top_blocks = []
    for q in queue_lists:
        if len(q) > 0:
            top_blocks.append(q[-1])
    print(*top_blocks,sep='')

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