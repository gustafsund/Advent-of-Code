from utils.utils import get_input
import argparse
import numpy as np
DAY = 8 # update this each day. 

def check_edge(r,c):
    bools = [r == 0, 
            r == shape[0]-1, 
            c == 0, 
            c == shape[1]-1]
    return bools


def sum_visible(data):
    s = 0
    for r in range(shape[0]):
        for c in range(shape[1]):
            add = 0
            bools = check_edge(r,c)
            if sum(bools) > 0:
                add = 1
                s += 1
            if not bools[0] and add == 0:
                add = int(data[r,c] > max(data[:r,c]))
                s += add
            if not bools[1] and add == 0:
                add = int(data[r,c] > max(data[r+1:,c]))
                s += add
            if not bools[2] and add == 0:
                add= int(data[r,c] > max(data[r,:c]))
                s += add
            if not bools[3] and add == 0:
                add = int(data[r,c] > max(data[r,c+1:]))
                s += add
    return s


def scenic_scores(data):
    scores = np.zeros(shape = (shape[0],shape[1],4))
    for r in range(shape[0]):
        for c in range(shape[1]):
            val = data[r,c]
            bools = check_edge(r,c)
            if not bools[0]:
                look_up = data[:r,c][::-1]
                w = np.where(look_up >= val)[0]
                if len(w) == 0:
                    scores[r,c,0] = len(look_up)
                else:
                    scores[r,c,0] = w[0] + 1
            if not bools[1]:
                look_down = data[r+1:,c]
                w = np.where(look_down >= val)[0]
                if len(w) == 0:
                    scores[r,c,1] = len(look_down)
                else:
                    scores[r,c,1] = w[0] + 1
            if not bools[2]:
                look_right = data[r,:c][::-1]
                w = np.where(look_right >= val)[0]
                if len(w) == 0:
                    scores[r,c,2] = len(look_right)
                else:
                    scores[r,c,2] = w[0] + 1
            if not bools[3]:
                look_left = data[r,c+1:]
                w = np.where(look_left >= val)[0]
                if len(w) == 0:
                    scores[r,c,3] = len(look_left)
                else:
                    scores[r,c,3] = w[0] + 1
    prod = np.prod(scores,axis = 2)
    
    return int(prod.max())



def solve1():
    data = get_input(DAY,'txt')
    for i,line in enumerate(data):
        data[i] = list(map(int,[symbol for symbol in line]))
    data = np.array(data)
    global shape 
    shape = data.shape
    sol = sum_visible(data)
    print(sol)


def solve2():
    data = get_input(DAY,'txt')
    for i,line in enumerate(data):
        data[i] = list(map(int,[symbol for symbol in line]))
    data = np.array(data)
    global shape 
    shape = data.shape
    sol = scenic_scores(data)
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