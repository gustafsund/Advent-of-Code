from utils.utils import get_input
import argparse

DAY = 2 # update this each day. 

def solve1():
    data = get_input(DAY,'csv', sep = ' ',names = ['opponent','you'])
    outcome_score = []
    data['equalizer'] = data.you.map({'X':'A','Y':'B','Z':'C'})
    for i,row in data.iterrows():
        if row['opponent'] == row['equalizer']:
            outcome_score.append(3)
        elif row['opponent'] == 'A':
            if row['you'] == 'Y':
                outcome_score.append(6)
            else:
                outcome_score.append(0)
        elif row['opponent'] == 'B':
            if row['you'] == 'X':
                outcome_score.append(0)
            else:
                outcome_score.append(6)
        elif row['opponent'] == 'C':
            if row['you'] == 'X':
                outcome_score.append(6)
            else:
                outcome_score.append(0)
    data['outcome_score'] = outcome_score        
    data['shape_score'] = data.you.map({'X':1,'Y':2,'Z':3})
    data['round_total'] = data.shape_score + data.outcome_score
    print(f'Overall score: {data.round_total.sum()}')

def solve2():
    data = get_input(DAY,'csv', sep = ' ',names = ['opponent','strategy'])
    you_play = []
    lose_map = {'A':'C','B':'A','C':'B'}
    win_map = {'A':'B','B':'C','C':'A'}
    for i,row in data.iterrows():
        if row['strategy'] == 'X':
            you_play.append(lose_map[row['opponent']])
        elif row['strategy'] == 'Y':
            you_play.append(row['opponent'])
        elif row['strategy'] == 'Z':
            you_play.append(win_map[row['opponent']])
    data['you_play'] = you_play
    data['shape_score'] = data.you_play.map({'A':1,'B':2,'C':3})
    data['outcome_score'] = data.strategy.map({'X':0,'Y':3,'Z':6})
    data['round_total'] = data.shape_score + data.outcome_score
    print(f'Overall score: {data.round_total.sum()}')


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-p',default = 'both')
    args = arg_parser.parse_args()
    puzzle = args.p
    if puzzle == '1':
        print('Puzzle nbr 1:')
        solve1()
    elif puzzle == '2':
        print('Puzzle nbr 2:')
        solve2()
    else:
        print('Puzzle nbr 1:')
        solve1()
        print('Puzzle nbr 2:')
        solve2()