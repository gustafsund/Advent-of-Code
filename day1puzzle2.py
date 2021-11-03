# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 17:36:02 2020

@author: gusta
"""

csv_dir = r'C:\\Users\\gusta\\OneDrive\\Dokument\\Jag\\Advent of Code\\expense_report.csv'


def get_data():
    with open(csv_dir) as csv_file:
        data = csv_file.readlines()
        
    
    for i in range(len(data)):
        data[i] = int(data[i])
    return data
    
def find_triplet(dat):
    for i in range(len(dat)):
        base = dat[i]
        for j in range(len(dat)):
            middle = dat[j]
            for k in range(len(dat)):
                if base + middle + dat[k] == 2020:
                    trip = list([base,middle,dat[k]])
                else:
                    pass
    return trip

def main():
    data = get_data()
    trip = find_triplet(data)
    s = trip[0]*trip[1]*trip[2]
    print(s)
    
main()