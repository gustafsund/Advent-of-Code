
def build_recursive(data,dir):
    end_rec = False
    file_system = {}
    dir_list = []
    file_list = []

    start_idx = int(np.where(data == f'$ cd {dir}')[0][0])
    print(start_idx)
    for i,line in enumerate(data[2:]):
        if line[:4] == '$ cd':
            if line == '$ cd ..':
                end_rec = True
            end_idx = i+2
            break
    
    for i,line in enumerate(data[start_idx+2:end_idx]):
        if line[:3] == 'dir':
            dir_list.append(line.split('dir ')[1])
        else:
            file_list.append(int(line.split(' ')[0]))

    if len(file_list) > 0:
        file_system['files'] = sum(file_list)
    else:
        file_system['files'] = 0
    
    if end_rec:
        return file_system
    else:
        file_system['dirs'] = {}
        for dir in dir_list:
            file_system[dir] = build_recursive(data[end_idx:],dir)
        return file_system
    
def build_filesystem(data):
    
    file_system = {}
    dir_list = []
    file_list = []

    for i,line in enumerate(data[2:7]):
        if line[:3] == 'dir':
            dir_list.append(line.split('dir ')[1])
        else:
            file_list.append(int(line.split(' ')[0]))

    file_system['/'] = {}
    file_system['/']['dirs'] = {}

    if len(file_list) > 0:
        file_system['/']['files'] = sum(file_list)
    else:
        file_system['/']['files'] = 0

    for dir in dir_list:
        file_system['/']['dirs'][dir] = build_recursive(data[7:],dir)
    
    return file_system

def build_filesystem2(data):
    pass
