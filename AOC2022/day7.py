from utils.utils import get_input
import argparse
from utils.day7_classes import Filesystem

DAY = 7 # update this each day. 

def find_sum(dir, limit = 100000):
    if len(dir.children) == 0:
        s = dir.size
        if s <= limit:
            return s
        else:
            return 0
    else:
        sum_self = dir.size  
        sum_children = sum([find_sum(c) for c in dir.children])
        if sum_self <= limit:
            return sum_self + sum_children
        else:
            return sum_children 

def get_smallest(fs, need_to_reduce):
    ls = [x for x in fs.size_list if x >= need_to_reduce]
    return min(ls)


def solve1():
    data = get_input(DAY,'txt')
    fs = Filesystem(data)
    print(find_sum(fs.root))


def solve2():
    data = get_input(DAY,'txt')
    fs = Filesystem(data)
    tot_available = 70000000
    using = fs.root.size
    currently_unused = tot_available - using
    needed_total_space = 30000000
    need_to_reduce = needed_total_space - currently_unused
    sol = get_smallest(fs, need_to_reduce)
    print(sol)



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