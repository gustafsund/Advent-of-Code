from utils.utils import get_input
import argparse
import numpy as np
DAY = 9 # update this each day. 


def solve1():
    data = get_input(DAY,'txt')
    lim = 1 + sum([int(x.split(' ')[-1]) for x in data])
    head,tail = np.zeros((lim,2)), np.zeros((lim,2))
    dirs = {'U':np.array([1,0]),
            'D':np.array([-1,0]),
            'L':np.array([0,-1]),
            'R':np.array([0,1])}
    base = 0
    for i,line in enumerate(data):
        dir, steps = line.split(' ')
        steps = int(steps)
        for s in range(steps):
            base += 1
            head[base,:] = head[base-1,:] + dirs[dir]
            diff = head[base,:] - tail[base-1,:]
            # print(head[base,:],' - ',tail[base-1,:], ' = ',diff, 'sum ', np.sqrt(np.matmul(diff.T,diff)))
            if np.sqrt(np.matmul(diff.T,diff)) >=2:
                tail[base,:] = head[base-1,:]
            else:
                tail[base,:] = tail[base-1,:]
     
    unique_positions = set(zip(tail[:,0],tail[:,1]))
    # for pos in unique_positions:
    #     print(tuple(map(int,pos)))
    print(len(unique_positions)) 


def disp_knots(knots):
    print('H      1     2     3     4     5     6     7     8     9')
    for i in range(knots.shape[0]):
        s = ''
        for p in range(10):
            x,y = map(int,knots[i,p:p+2])
            s += f'{x},{y}   '
        print(s)



def solve2():
    data = get_input(DAY,'txt')
    lim = 1 + sum([int(x.split(' ')[-1]) for x in data])
    dirs = {'U':np.array([1,0]),
            'D':np.array([-1,0]),
            'L':np.array([0,-1]),
            'R':np.array([0,1])}

    n_knots = 10
    knots = np.zeros((lim,2*n_knots))
    base = 0
    for i,line in enumerate(data):
        dir, steps = line.split(' ')
        steps = int(steps)
        for s in range(steps):
            base += 1
            knots[base,:2] = knots[base-1,:2] + dirs[dir] # head movement
            for knot in range(2,2*n_knots,2):
                diff = knots[base,knot-2:knot] - knots[base-1,knot:knot+2]
                addage = np.array([0,0])
                if abs(diff[0]) > 1:
                    addage[0] = np.sign(diff[0])
                    if diff[1] != 0:
                        addage[1] = np.sign(diff[1])
                elif abs(diff[1]) > 1:
                    addage[1] = np.sign(diff[1])
                    if diff[1] != 0:
                        addage[0] = np.sign(diff[0])
                knots[base,knot:knot+2] = knots[base-1,knot:knot+2] + addage    

    unique_positions = set(zip(knots[:,-2],knots[:,-1]))
    
    print(len(unique_positions)) 


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