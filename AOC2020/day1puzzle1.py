# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 17:06:26 2020

@author: gusta
"""


csv_dir = 'expense_report.csv'


def get_data():
    with open(csv_dir) as csv_file:
        data = csv_file.readlines()
        
    
    for i in range(len(data)):
        data[i] = int(data[i])
    return data
    
def find_pair(dat):
    for i in range(len(dat)):
        current = dat[i]
        for k in range(i,len(dat)):
            if current + dat[k] == 2020:
                pair = list([current,dat[k]])
            else:
                pass
    return pair

def main():
    data = get_data()
    p = find_pair(data)
    s = p[0]*p[1]
    print(s)
    print('Hej där!')

    
main()    
    
