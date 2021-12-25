import numpy as np

def get_lines():
    with open('input/dataday5.txt','r') as f:
        lines = f.readlines()
        v1 = []
        v2 = []
        max_x = 0
        max_y = 0
        for line in lines:
            m = line.rstrip('\n').split('->')
            a,b = [list(map(int,x.strip().split(','))) for x in m]
            a = np.array(a)
            b = np.array(b)
            v1.append(a)
            v2.append(b)
            max_x = max([max_x,a[0],b[0]])
            max_y = max([max_y,a[1],b[1]])
    v1 = np.stack(v1)
    v2 = np.stack(v2)
    return v1,v2,max_x,max_y

def setup_grid(v1,v2,max_x,max_y):
    grid = np.zeros(shape = (max_x+1,max_y+1))
    for s,e in zip(v1,v2):
        if s[0] == e[0]:
            mny,mxy = min(s[1],e[1]),max(s[1],e[1])
            grid[s[0],mny:mxy+1] += 1
        elif s[1] == e[1]:
            mnx,mxx = min(s[0],e[0]),max(s[0],e[0])
            grid[mnx:mxx+1,s[1]] += 1
    return grid

def setup_grid2(v1,v2,max_x,max_y):
    grid = np.zeros(shape = (max_x+1,max_y+1))
    for s,e in zip(v1,v2):
        if s[0] == e[0]:
            mny,mxy = min(s[1],e[1]),max(s[1],e[1])
            grid[s[0],mny:mxy+1] += 1
        elif s[1] == e[1]:
            mnx,mxx = min(s[0],e[0]),max(s[0],e[0])
            grid[mnx:mxx+1,s[1]] += 1
        elif (e[1]-s[1])/(e[0]-s[0]) == 1: 
            mnx = min(s[0],e[0])
            mny = min(s[1],e[1])
            l = abs(e[1]-s[1])
            for i in range(l+1):
                grid[mnx+i,mny+i] += 1
        elif (e[1]-s[1])/(e[0]-s[0]) == -1:
            mxx = max(s[0],e[0])
            mny = min(s[1],e[1])
            l = abs(s[1]-e[1])
            for i in range(l+1):
                grid[mxx-i,mny+i] += 1
                
    return grid

def main():
    v1,v2,max_x,max_y = get_lines()
    
    grid = setup_grid(v1,v2,max_x,max_y)
    nbr_of2s = (grid >= 2).sum()
    print(f'Puzzle 1, number of >=2 line intersections: {nbr_of2s}')

    grid2 = setup_grid2(v1,v2,max_x,max_y)
    nbr_of2s2 = (grid2 >= 2).sum()
    print(f'Puzzle 2, number of >=2 line intersections: {nbr_of2s2}')

if __name__ == '__main__':
    main()