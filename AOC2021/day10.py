from queue import LifoQueue
import numpy as np

def solve1():
    data = open('input/dataday10.txt','r').readlines()
    for i, line in enumerate(data):
        data[i] = line.rstrip('\n')
    score_table = {')':3,']':57,'}':1197,'>':25137}
    inverses = {')':'(',']':'[','}':'{','>':'<'}
    score = 0
    corrupted = []
    for i,line in enumerate(data):
        q = LifoQueue()
        for symb in line:
            if symb in score_table.keys():
                if q.empty() or q.get() != inverses[symb]:
                    score += score_table[symb]
                    corrupted.append(i)
                    break
            else:
                q.put(symb)
    return data,score,corrupted


def solve2(inpt,corrupted):
    data = [inpt[i] for i in range(len(inpt)) if i not in corrupted]
    inverses2 = {'(':')','[':']','{':'}','<':'>'}
    score_table2 = {')':1,']':2,'}':3,'>':4}
    scores = []
    for line in data:
        q = LifoQueue()
        seq = ''
        score = 0
        for symb in line:
            if symb in score_table2.keys():
                q.get()
            else:
                q.put(symb)
        for i in range(q.qsize()):
            next_symb = inverses2[q.get()]
            seq += next_symb
            score = score*5 + score_table2[next_symb]
        scores.append(score)
    ret = np.median(scores)
    return int(ret)







def main():
    data,score,corrupted = solve1()
    print(f'Puzzle 1: {score}')
    s2 = solve2(data,corrupted)
    print(f'Puzzle 2: {s2}')






if __name__ == '__main__':
    main()