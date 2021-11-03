import pandas as pd

# def get_data(csv_dir,COLUMN_NAMES):
#     df = pd.DataFrame(columns = COLUMN_NAMES)
#     print('hej')
#     with open(csv_dir) as csv_file:
#         data = csv_file.readlines()
#     for i in range(len(data)):
#         step1 = data[i].split(' ')
#         lwr,upr = step1[0].split('-')
#         char = step1[1].split(':')
#         password = step1[2]
#         df = df.append({'lwr':int(lwr),'upr':int(upr),'char':char,'password':password},ignore_index = True)   
#     return df

# def main():
#     csv_dir = r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code\password_policies.csv'
#     COLUMN_NAMES = ['lwr','upr','char','password']
#     dat = get_data(csv_dir,COLUMN_NAMES)
#     print('hej')
#     d = 2
#     print(d)
    
# main()

csv_dir = r'C:\Users\gusta\OneDrive\Dokument\Jag\Advent of Code\password_policies.csv'
COLUMN_NAMES = ['lwr','upr','char','password','valid']
with open(csv_dir) as csv_file:
    data = csv_file.readlines()
df = pd.DataFrame(columns = COLUMN_NAMES)
for i in range(len(data)):
     step1 = data[i].split(' ')
     lwr,upr = step1[0].split('-')
     lwr = int(lwr)
     upr = int(upr)
     char = step1[1].split(':')
     ch = char[0]
     password = step1[2].split('\n')[0]
     valid = password.count(ch) in range(lwr,upr+1)
     df = df.append({'lwr':lwr,'upr':upr,'char':ch,'password':password,'valid':valid},ignore_index = True)     

df['valid'].value_counts()
     
     
     
     
     
     