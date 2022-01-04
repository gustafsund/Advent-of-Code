

def solve1():
    raw_data = open('input/dataday8.txt','r').readlines()
    outputs = []
    inputs = []
    for x in raw_data:
        outputs.append(x.split('|')[1].strip().strip('\n').split(' '))
        inputs.append(x.split('|')[0].strip().strip('\n').split(' '))

    uniques = [2,3,4,7] # the unique lengths
    count = 0
    for line in outputs:
        count += sum(len(set(x)) in uniques for x in line)

    return count,inputs,outputs

def matches(s1,s2):
    l = len(s1)
    if l != len(s2):
        return False
    return sum(i in s2 for i in s1) == l

def find_match(s,keys):
    for k in keys:
        if matches(s,k):
            return k
    return 'FAIL'

def overlap(m,s):
    return sum(i in s for i in m)

def decode(nums):
    decoder = {}
    rev_decoder = {}
    mysteries = []
    for x in nums:
        l = len(x)
        if l== 2:
            decoder[x] = 1
            rev_decoder[1] = x
        elif l == 3:
            decoder[x] = 7
            rev_decoder[7] = x
        elif l == 4:
            decoder[x] = 4
            rev_decoder[4] = x
        elif l == 7:
            decoder[x] = 8
            rev_decoder[8] = x
        else:
            mysteries.append(x)
    for m in mysteries:
        if len(m) == 6: # 0 or 6
            if overlap(m,rev_decoder[1]) == 2:
                if overlap(m,rev_decoder[4]) == 4:
                    decoder[m] = 9
                else:
                    decoder[m] = 0
            else: 
                decoder[m] = 6
        else:
            if overlap(m,rev_decoder[1]) == 2:
                decoder[m] = 3
            elif overlap(m,rev_decoder[4]) == 2:
                decoder[m] = 2
            else:
                decoder[m] = 5

    return decoder
        



def solve2(inputs,outputs):
    s = 0
    for ins,outs in zip(inputs,outputs):
        decoder = decode(ins)
        for i, x in enumerate(outs):
            m = find_match(x,decoder.keys())
            if m != 'FAIL':
                s+= decoder[m]*10**(len(outs)-1-i)
            else:
                print(m)
    return s
            



def main():
    count,inputs,outputs = solve1()
    print(f'Puzzle 1: {count}')
    ans2 = solve2(inputs,outputs)
    print(f'Puzzle 2: {ans2}')




if __name__ == '__main__':
    main()