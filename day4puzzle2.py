import pandas as pd

def is_valid2(row):
    row = row.to_dict()
    if not row['valid']:
        return False
    
    validv = [False,False,False,False,False,False,False]
    
    for key in row:
        if key == 'cid' or key == 'Unnamed: 0' or key == 'valid':
            pass
        else:
            if key == 'byr':
                validv[0] = valid_byr(row[key])
            if key == 'iyr':
                validv[1] = valid_iyr(row[key])
            if key == 'eyr':
                validv[2] = valid_eyr(row[key])
            if key == 'hgt':
                validv[3] = valid_hgt(row[key])
            if key == 'hcl':
                validv[4] = valid_hcl(row[key])
            if key == 'ecl':
                validv[5] = valid_ecl(row[key])
            if key == 'pid':
                validv[6] = valid_pid(row[key])
            else:
                pass
    # print(validv)
    return False not in validv

def valid_byr(key):
    if not type(key) == float: 
        return False
    k = int(key)
    if k not in range(1920,2003):
        return False
    return True

def valid_iyr(key):
    if not type(key) == float:
        return False
    k = int(key)
    if k not in range(2010,2021):
        return False
    return True

def valid_eyr(key):
    if not type(key) == float:
        return False
    k = int(key)
    if k not in range(2020,2031):
        return False
    return True

def valid_hgt(key):
    if not type(key) == str:
        return False
    if len(key) not in range(4,6):
        return False
    if len(key) == 5:
        if key[3:] != 'cm':
            return False
        t = int(key[:3])
        if t not in range(150,194):
            return False
    if len(key) == 4:
        if key[2:] != 'in':
            return False
        d = int(key[:2])
        if d not in range(59,77):
            return False
    return True

def valid_hcl(key):
    if not type(key) == str:
        return False
    if len(key) != 7 or key[0] != '#':
        return False
    for symb in key[1:]:
        if symb not in ('a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9'):
            return False
    return True

def valid_ecl(key):
    if not type(key) == str:
        return False
    if len(key) != 3:
        return False
    if key not in ('amb','blu','brn','gry','grn','hzl','oth'):
        return False    
    return True

def valid_pid(key):
    if not type(key) == str:
        return False                
    if len(key) != 9:
        return False
    # if key[0] != '0':
    #     return False
    for symb in key[1:]:
        if symb not in ('0','1','2','3','4','5','6','7','8','9'):
            return False
    return True

def main():
    csv_dir = r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code\new_passports.csv'
    df2 = pd.read_csv(csv_dir)
    df2['valid2'] = df2.apply(is_valid2,axis = 1)
    print(df2['valid2'].value_counts())
    # print(df2[15:16])    
    # df2.to_csv(r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code\newer_passports.csv')

main()    
        