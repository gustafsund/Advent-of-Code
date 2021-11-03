csv_dir = r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code\bag_rules.csv'
with open(csv_dir) as csv_file:
    rules = csv_file.readlines()


colors = set()
for rule in rules:
    if rule.count('shiny gold') > 0:
        temp = rule.split(' ')
        color = temp[0] + ' ' + temp[1]
        if color != 'shiny gold':
            colors.add(color)

new_colors = set()
new_colors.update(colors)
new_colors.add('a')

while len(new_colors) > len(colors):
    if 'a' in new_colors:
        new_colors.remove('a')
    colors.update(new_colors)
    for rule in rules:
        for color in colors:
            if rule.count(color) > 0:
                temp = rule.split(' ')
                c = temp[0] + ' ' + temp[1]
                if c != 'shiny gold' and c not in colors:
                    new_colors.add(c)
print('Answer: ', str(len(colors)))
