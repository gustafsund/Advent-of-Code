
import numpy as np

def setup_game():
    with open('input/dataday4.txt','r') as f:
        lines = f.readlines()
        draws = list(map(int,lines[0].strip().rstrip('\n').split(',')))
        boards = []
        i = 1
        while i < len(lines):
            if lines[i] == '\n':
                board = np.zeros(shape = (5,5))
                for j in range(5):
                    i+=1
                    board[j,:] = list(map(int,lines[i].strip().rstrip('\n').split()))
                    # board.append(list(map(int,lines[i].strip().rstrip('\n').split())))
                boards.append(board)
            i+=1
    boards = np.stack(boards)
    return draws,boards

def is_winner(stat):
    return np.any(stat.sum(axis=0) == 5) or np.any(stat.sum(axis=1) == 5)

def play_game(draws,boards):
    stats = np.zeros(shape = boards.shape)
    for i,draw in enumerate(draws):
        stats += boards == draw
        stats[stats > 1] = 1
        for b,board in enumerate(boards):
            if is_winner(stats[b]):
                return i,b,board,stats[b]
    return None,None,None,None


def play_game_losing(draws,boards):
    stats = np.zeros(shape = boards.shape)
    nbr_boards = stats.shape[0]
    winners = []
    loser = None
    for i,draw in enumerate(draws):
        nbr_losers = nbr_boards
        stats += boards == draw
        stats[stats > 1] = 1
        for b,board in enumerate(boards):
           if b not in winners:
               if is_winner(stats[b]):
                   winners.append(b)
        if len(winners) == nbr_boards - 1:
            loser = [x for x in range(nbr_boards) if x not in winners][0]
        elif len(winners) == nbr_boards:
            return i,loser,boards[loser],stats[loser]
    


def main():
    draws,boards = setup_game()
    moves,board_nbr,board,stat = play_game(draws,boards)
    score = int(board[stat == 0].sum()*draws[moves]) 
    print(f'Score for puzzle 1: {score}')
    moves,board_nbr,board,stat = play_game_losing(draws,boards)
    score = int(board[stat == 0].sum()*draws[moves])
    print(f'Score for puzzle 2: {score}')

if __name__ == '__main__':
    main()