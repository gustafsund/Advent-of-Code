import pandas as pd
import numpy as np


def seat_id(row):
    s = row.to_dict()
    r = s['row']
    c = s['col']
    return 8*r + c

def find_rows(row):
    s = row.to_dict()
    d = s['Boarding Pass']
    return find_row(d[:7],0,127)

def find_cols(row):
    s = row.to_dict()
    d = s['Boarding Pass']
    return find_col(d[7:],0,7)

def find_row(s,lwr,upr):    
    if len(s) == 1:
        if s[0] == 'F':
            return int(lwr)
        elif s[0] == 'B':
            return int(upr)
    else:
        mid = (upr+lwr)//2
        if s[0] == 'F':
            return find_row(s[1:],lwr,mid)
        elif s[0] == 'B':
            return find_row(s[1:],mid+1,upr)
        
def find_col(s,lwr,upr):
    if len(s) == 1:
        if s[0] == 'L':
            return int(lwr)
        elif s[0] == 'R':
            return int(upr)
    else:
        mid = (upr+lwr)//2
        if s[0] == 'L':
            return find_col(s[1:],lwr,mid)
        elif s[0] == 'R':
            return find_col(s[1:],mid+1,upr)


def main():
    csv_dir = r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code\boarding_passes.csv'
    df = pd.read_csv(csv_dir)
    df['row'] = df.apply(find_rows,axis = 1)
    df['col'] = df.apply(find_cols,axis = 1)
    print(df.head())
    df['seat ID'] = df.apply(seat_id,axis = 1)
    print(df.head())
    m = np.zeros((127,8))
    print(len(df))
    
    for i in range(len(df)):
        m[df.at[i,'row']][df.at[i,'col']] = 1
        
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == 0:
                print('row',str(r),'col',str(c))
                
# ugly solution, just read the output and calculated 8*81 + 1 = 649.
main()
