import sys


n = int(input())
data = dict()
for i in range(n):
    s1, s2 = str(input()).split(" ")
    data[s1] = s2
keys_ = list()
for line in sys.stdin:
    line = line.rstrip('\r\n')
    keys_.append(line)
for key in keys_:
    if key in data.keys():
        print(f"{key}={data[key]}")
    else:
        print("Not found")




