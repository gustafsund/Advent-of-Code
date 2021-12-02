
#%% Part 1
path = r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code\loop_instructions.csv'
with open(path) as csv_file:
    instructions = csv_file.readlines()

l = len(instructions)
for i in range(l):
    instructions[i] = instructions[i].split('\n')[0]

line = 1
lines = []
accumulator = 0
while line not in lines and line <= l:
    lines.append(line)
    command, arg = instructions[line-1].split(' ')
    if command == 'acc':
        if arg[0] == '+':
            accumulator+=int(arg[1:])
        elif arg[0] == '-':
            accumulator -= int(arg[1:])
        line+=1
    elif command == 'jmp':
        if arg[0] == '+':
            line += int(arg[1:])
        elif arg[0] == '-':
            line -= int(arg[1:])
    elif command == 'nop':
        line += 1
print(accumulator)
        
#%% Part 2


def try_run(ch_line):
    line = 1
    lines = []
    accumulator = 0
    while line not in lines and line <= l:
        lines.append(line)
        if line == ch_line:
            if instructions[line-1][:3] == 'jmp':
                command = 'nop'
            elif instructions[line-1][:3] == 'nop':
                command = 'jmp'
                arg = instructions[line-1][4:]
        else:
            command, arg = instructions[line-1].split(' ')
        if command == 'acc':
            if arg[0] == '+':
                accumulator+=int(arg[1:])
            elif arg[0] == '-':
                accumulator -= int(arg[1:])
            line+=1
        elif command == 'jmp':
            if arg[0] == '+':
                line += int(arg[1:])
            elif arg[0] == '-':
                line -= int(arg[1:])
        elif command == 'nop':
            line += 1
     
    if line in lines:
        return False, None
    else:
        return True, accumulator
     


def main():
    for i in range(l):
        if instructions[i][:3] == 'jmp' or instructions[i][:3] == 'nop':
            b,a = try_run(i)
            if b:
                print(a)
                print('i: ',str(i))

main()

#%% Hjälp från reddit
path = r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code\loop_instructions.csv'
with open(path) as csv_file:
    instructions = csv_file.readlines()

def run(code,visited, accumulator = 0, i = 0):
    l = len(code)
    while i not in visited and i < l:
        visited[i] = accumulator
        operation, number = code[i]
        
        if operation == 'acc':
            accumulator += number
        if operation == 'jmp':
            i += number -1
        
        i+=1
    return accumulator, i




for i in range(l):
    instructions[i] = instructions[i].split('\n')[0]

code,visited = [],dict()

for line in instructions:
    operation, number = line.split(' ')
    code.append((operation,int(number)))

accumulator,t = run(code,visited)
print(accumulator)

s = set(visited.keys())
for j in s:
    operation, number = code[j]    
    if (operation == "nop" and (i := j + number) not in visited) or \
        (operation == "jmp" and (i := j + 1) not in visited):
       # And continue just from the next instruction with restored state
        accumulator, i = run(code, visited, visited[j], i)
        if i >= len(code):
            print(accumulator)  # 2nd part
            break