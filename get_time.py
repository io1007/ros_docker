import sys

args = sys.argv

with open('/home/ubuntu/log/{}'.format(args[1])) as f:
    lines = [s.strip() for s in f.readlines()]

s_time = [line for line in lines if 'Durtation' in line]

if len(s_time) == 0:
    print('error')

with open('/home/ubuntu/log/{}'.format(args[2]),mode='w') as f:
    f.writelines('\n'.join(s_time))
