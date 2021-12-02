csv_dir = r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code\trees_map.csv'
with open(csv_dir) as csv_file:
    map_list = csv_file.readlines()
    
x_step = 3
y_step = 1
X_counter = 0
O_counter = 0

for i in range(len(map_list)):
    row = i*y_step
    map_list[row] = map_list[row].strip('\n')
    s = map_list[row]
    pos = i*x_step
    while len(map_list[row]) <= pos:
        map_list[row] = map_list[row] + s
    if map_list[row][pos] == '#':
        map_list[row] = map_list[row][:pos]+ 'X' + map_list[row][pos+1:]
        X_counter += 1
    # elif map_list[row][pos] == '.':
    #     map_list[row] = map_list[row][:pos]+ 'O' + map_list[row][pos+1:]
    #     O_counter += 1
    
    else:
        pass
    
print(X_counter)








