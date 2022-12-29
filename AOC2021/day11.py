import numpy as np

def make_step(data):
    data += 1
    flashed = np.zeros(shape = data.shape)
    flashed[data>9] = 1
    flashers = np.where(data>9)
    data[data>9] = 0
    dirs = [-1,0,1]
    while len(flashers[0]) > 0:
        for row, col in zip(flashers[0],flashers[1]):
            for r_dir in dirs:
                for c_dir in dirs:
                    bools = [r_dir == 0 and c_dir == 0, 
                            row + r_dir not in range(data.shape[0]), 
                            col + c_dir not in range(data.shape[1])]
                    if sum(bools) == 0 and flashed[row+r_dir,col+c_dir] == 0:
                        data[row+r_dir,col+c_dir] += 1

        flashed[data>9] = 1
        flashers = np.where(data>9)
        data[data>9] = 0
        
    first = flashed.sum() == data.size
    first = data.sum() == 0
    return data,flashed.sum(),first

                


def solve():
    data = [[int(s) for s in x.rstrip('\n')] for x in open('input/dataday11.txt','r').readlines()]
    data = np.array(data)
    steps = 100
    tot_flashes = 0
    first_flash = -1
    for i in range(steps):
        data,flashed,first = make_step(data)
        tot_flashes += flashed
        if first:
            first_flash = i
    return tot_flashes,first_flash


def main():
    tot_flashes,first = solve()
    tot_flashes = int(tot_flashes)
    print(f'Puzzle 1: {tot_flashes}')
    print(f'Puzzle 2: {first}')

if __name__ == '__main__':
    main()