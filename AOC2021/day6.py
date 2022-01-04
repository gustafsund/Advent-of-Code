def update_fish(fishlist):
    ret = []
    for fish in fishlist:
        if fish == 0:
            ret.append(6)
            ret.append(8)
        else:
            ret.append(fish-1)
    return ret
# ^ this method does not work for problem 2, too long time to process/memory problems.

def solve_p2(fishlist,nbr_days):
    states = [0]*9
    for x in fishlist:
        states[x] += 1
    for i in range(nbr_days):
        states = states[1:] + [states[0]]
        states[6] += states[-1]
    return sum(states)



def main():
    fish = list(map(int,open('input/dataday6.txt','r').readlines()[0].split(',')))
    nbr_days = 80
    for i in range(nbr_days):
        fish = update_fish(fish)
    print(f'Puzzle 1, nbr of fish: {len(fish)}')
    fish = list(map(int,open('input/dataday6.txt','r').readlines()[0].split(',')))
    
    nbr_fish2 = solve_p2(fish,256)
    print(f'Puzzle 2, nbr of fish: {nbr_fish2}')



if __name__ == '__main__':
    main()