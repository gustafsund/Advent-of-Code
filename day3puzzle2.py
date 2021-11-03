
def get_Xs(x_step,y_step,slope_map):
    X_counter = 0
    # O_counter = 0
    
    for i in range(len(slope_map)):
        row = i*y_step
        if row >= len(slope_map):
            break
        s = t = slope_map[row].strip('\n')
        
        pos = i*x_step
        while len(t) <= pos:
            t = t + s
        if t[pos] == '#':
            X_counter += 1
        else:
            pass
    return X_counter


def main():
    csv_dir = r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code\trees_map.csv'
    with open(csv_dir) as csv_file:
        map_list = csv_file.readlines()
    x11 = get_Xs(1,1,map_list)
    x31 = get_Xs(3,1,map_list)
    x51 = get_Xs(5,1,map_list)
    x71 = get_Xs(7,1,map_list)
    x12 = get_Xs(1,2,map_list)
    
    prod = x11*x31*x51*x71*x12
    print(prod)
    
    
main()
