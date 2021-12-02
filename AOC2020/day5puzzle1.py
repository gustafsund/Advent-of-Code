import pandas as pd

def seat_id(row):
    s = row.to_dict()
    d = s['Boarding Pass']    

    return 8*find_row(d[:7],0,127) + find_col(d[7:],0,7)


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
    # print(df.head())
    df['seat ID'] = df.apply(seat_id,axis = 1)
    print(df.head())
    print(df['seat ID'].max())
    
    
main()


            