class File:

    def __init__(self,line: str):
        size, name = line.split(' ')
        self.line = line
        self.size = int(size)
        self.name = name

    def match_line(self,line):
        return line == self.line
    
    def to_string(self):
        return f'- {self.name} (file, size = {self.size})'

class Directory:

    def __init__(self,line: str, parent: File = None):
        _, name = line.split(' ')
        if parent: 
            self.parent = parent
        else:
            assert name == '/'
        self.name = name
        self.line_to_match = f'$ cd {self.name}'
        self.children = []
        self.files = []
        self.size = 0
    
    def has_children(self):
        return len(self.children > 0)

    def add_file(self,file:str):
        self.files.append(File(file))
    
    def add_child(self,line):
        self.children.append(Directory(line, self))
    
    def match_line(self,line):
        return line == self.line_to_match
    
    def to_string(self):
        return f'- {self.name} (dir)'
        

class Filesystem: 

    def __init__(self, lines: list):
        assert self.is_move_down(lines[0])
        root_line = lines[0].split('$ ')[1]
        
        self.root = Directory(root_line)
        self.lines = lines[1:]
        self.build()
        self.size_list = []
        self.set_all_sizes()
        
    def build(self):
        cdir = self.root
        listing = False
        for line in self.lines:
            if self.is_ls(line):
                listing = True
            elif listing and self.is_file(line):
                cdir.add_file(line)
            elif listing and self.is_directory(line):
                cdir.add_child(line)
            elif self.is_move_down(line):
                listing = False
                cdir = self.match_line(cdir.children,line)
            elif self.is_move_up(line):
                listing = False
                cdir = cdir.parent


    def match_line(self,dirlist,line):
        for dir in dirlist:
            if dir.match_line(line):
                return dir

    def is_move_down(self,line):
        return line[:4] == '$ cd' and line[-2:] != '..'
    
    def is_move_up(self,line):
        return line == '$ cd ..'

    def is_directory(self,line):
        return line[:3] == 'dir'
    
    def is_file(self,line):
        spl = line.split(' ')
        return len(spl) == 2 and spl[0] not in ['$','dir']

    def is_ls(self,line):
        return line == '$ ls'

    def set_all_sizes(self):
        self.root_size = self.set_size(self.root)

    def set_size(self,dir):
        if len(dir.children) == 0:
            if len(dir.files) > 0:
                size = sum([f.size for f in dir.files])
            else:
                size = 0
            dir.size = size
            self.size_list.append(size)
            return size
        else:
            if len(dir.files)>0:
                own_files = sum([f.size for f in dir.files])
            else:
                own_files = 0
            children_size = sum([self.set_size(c) for c in dir.children])
            dir.size = own_files + children_size
            self.size_list.append(dir.size)
            return dir.size
    
    def display_system(self):
        return self.to_string(self.root, level = 0)

    def to_string(self, dir, level = 0):
        if len(dir.children) == 0:
            print(' '*(level+1) + dir.to_string())
            for f in dir.files:
                print(' '*(level + 2) + f.to_string())
        else:
            print(dir.to_string())
            for c in dir.children:
                self.to_string(c,level+1)
            for f in dir.files:
                print(' '*(level+1) + f.to_string())