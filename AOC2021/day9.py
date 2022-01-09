import numpy as np

def is_lowpoint(x,data,r,c):
    dirs = [-1,0,1]
    ret = True
    for dr in dirs:
        for dc in dirs:
            bools = [r+dr < 0, c+dc <0 ,dr == 0 and dc == 0,r+dr >= len(data),c + dc >= len(data[0])]
            if sum(bools) == 0:
                if x >= data[r+dr][c+dc]:
                    ret = False    
    return ret
                


def solve1():
    data = [] 
    for line in open('input/dataday9.txt','r').readlines():
        x = line.strip().rstrip('\n')
        data.append([int(i) for i in x])
    s = 0
    lowpoints = []
    for r,line in enumerate(data):
        for c,x in enumerate(line):
            if is_lowpoint(x,data,r,c):
                s += 1 + x
                lowpoints.append([r,c])
    return s, data, lowpoints

def basin(data,point,history):
    r,c = point    
    bools = [r < 0, c <0,r >= len(data),c >= len(data[0]),point in history]
    if sum(bools)>0:
        return 0
    elif data[r][c] == 9:
        return 0
    else:
        history.append(point)
        return 1 + basin(data,[r+1,c],history) + basin(data,[r-1,c],history) + basin(data,[r,c+1],history) + basin(data,[r,c-1],history) 



def solve2(data,lowpoints):
    sizes = []
    for point in lowpoints:
        sizes.append(basin(data,point,[]))
    return sorted(sizes)[-3:]




def main():
    s, data, lowpoints = solve1()
    print(f'Puzzle 1: {s}')
    sizes = solve2(data,lowpoints)
    ans2 = np.prod(sizes)
    print(f'Puzzle 2: {ans2}')


if __name__ == '__main__':
    main()