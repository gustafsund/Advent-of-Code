# import sys
# sys.path.insert(1,r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code')
# import day6puzzle2

csv_dir = r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code\bag_rules.csv'
with open(csv_dir) as csv_file:
    rules = csv_file.readlines()




def summing(color):
    for rule in rules:
            temp = rule.split(' ')
            if temp[:2] == color.split(' '):
                root = rule
    d = root.split('contain ')
    if d[1].count('no other') > 0:
        return 1
    s = d[1]
    t = s.split(', ')
    colors = []
    nbrs = []
    for sats in t:
        temp = sats.split(' bag')
        d = temp[0]
        print(d)
        tal = int(d[0])
        col = d[2:]
        colors.append(col)
        nbrs.append(tal)
    l = len(colors)
    if l == 0:
        return 1
    sm = 0    
    for i in range(l):
        sm+= nbrs[i]*summing(colors[i])
    return sm

color = 'shiny gold'
ans= summing(color)
print(ans)


# def get_dict(color):
#     for rule in rules:
#         temp = rule.split(' ')
#         if temp[:2] == color.split(' '):
#             root = rule
#     d = root.split('contain ')
#     s = d[1]
#     t = s.split(', ')
#     di = {}
#     for sats in t:
#         temp = sats.split(' bags')
#         d = temp[0]
#         tal = int(d[0])
#         col = d[2:]
#         di.update({col:tal})
#     if len(di) == 0:
#         return None
#     hyp = {color:di}
#     for thing in hyp[color]:
#         print(hyp[color][thing])
#     return hyp

# def main():
#     n = get_dict('shiny gold')
#     print(n)
# main()



