csv_dir = r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code\questions_answered.csv'
with open(csv_dir) as csv_file:
    data = csv_file.readlines()
prev_space = 0
groups = []

for i in range(len(data)):
    if data[i] == '\n':
        new_space = i
        if prev_space == 0:
            groups.append(data[:new_space])
            prev_space = new_space + 1
        else:
            groups.append(data[prev_space:new_space])
            prev_space = new_space+1
    else:
        pass
groups.append(data[prev_space:])

sm = 0

for group in groups:
    checked = []
    for line in group:
        for ch in line:
            if ch != '\n':
                checked.append(ch)
    uniques = set(checked)
    for ch in uniques:
        if checked.count(ch) == len(group):
            sm+=1


print(sm)  