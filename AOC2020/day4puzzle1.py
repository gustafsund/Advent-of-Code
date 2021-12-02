import pandas as pd


def is_valid(row):
    valid = True
    row = row.to_dict()
    for key in row:
        if key == 'cid':
            pass
        else:
            if row[key] == 'N/A':
                valid = False
            else:
                pass
    return valid

csv_dir = r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code\passport_data.csv'
with open(csv_dir) as csv_file:
    data = csv_file.readlines()
prev_space = 0
list_entries = []

for i in range(len(data)):
    if data[i] == '\n':
        new_space = i
        if prev_space == 0:
            list_entries.append(data[:new_space])
            prev_space = new_space + 1
        else:
            list_entries.append(data[prev_space:new_space])
            prev_space = new_space+1
    else:
        pass
list_entries.append(data[prev_space:])
# l = len(list_entries)
# # some kind of reference I guess...
ls = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid'] 
ls_sorted = sorted(ls)
df = pd.DataFrame(columns = ls_sorted)


for e in list_entries:
    collect_tuples = {}
    for s in e:
        step1 = s.split('\n')
        step2 = step1[0].split(' ') # contains pairs.
        for p in step2:
            d = p.split(':')
            header = d[0]
            value = d[1]
            collect_tuples.update({header:value})
    for col in ls_sorted:
        if col not in collect_tuples.keys():
            collect_tuples.update({col:'N/A'})
    inpt = dict(sorted(collect_tuples.items()))
    df = df.append(inpt,ignore_index = True)

df['valid'] = df.apply(is_valid,axis = 1)

# df.to_csv(r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code\new_passports.csv')
                
print(df['valid'].value_counts())