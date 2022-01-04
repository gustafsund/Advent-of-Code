
import numpy as np
import statistics

def solve1(data):
    positions = np.array(data)
    target = round(np.median(positions),0)*np.ones(len(positions))
    cost = np.absolute(target-positions).sum()
    cost = sum([abs(t-p) for t,p in zip(target,positions)])
    return int(cost)

def get_cost(arr):
    s = 0
    for x in arr:
        n = abs(x)
        s+= n*(n+1)/2
    return s


def solve2(data):
    positions = np.array(data)
    min_cost = 10**10 # some big number, should be easy to beat
    one = np.ones(len(positions))
    for b in range(min(positions),max(positions)+1):
        cost = get_cost(b*one-positions)
        if cost < min_cost:
            min_cost = cost
    return int(round(min_cost,0)), b




def main():
    data =  list(map(int,open('input/dataday7.txt','r').readlines()[0].split(',')))
    fuel = solve1(data)
    print(f'Puzzle 1: {fuel}')
    data =  list(map(int,open('input/dataday7.txt','r').readlines()[0].split(',')))
    fuel2,b = solve2(data)
    print(f'Puzzle 2: {fuel2}')



if __name__ == '__main__':
    main()