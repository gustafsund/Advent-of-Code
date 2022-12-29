from pathlib import Path
import pandas as pd
HERE = Path(__file__).parent.parent

def get_input(day=1,filetype = 'txt', sep = None,names = None):
    if filetype != 'csv':
        with open(str(HERE/'input'/f'day{day}.{filetype}')) as file:
            if day == 1: 
                return file.readlines()
            data = [x.rstrip('\n') for x in file.readlines()]
    else:
        data = pd.read_csv(str(HERE/'input'/f'day{day}.{filetype}'),sep=sep, header= None,names = names)
    return data

def as_integers(data,handle_newlines = 'exclude'):
    neat_data = []
    for x in data:
        if x != '\n':
            neat_data.append(int(x.rstrip('\n')))
        else:
            if handle_newlines == 'zero':
                neat_data.append(0)
            elif handle_newlines == 'exclude':
                continue

    return neat_data