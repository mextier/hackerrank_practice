data = list(map(int,reversed("{0:b}".format(int(input())))))
print(data)

max_ = 0
seq = 0
for i in data:
    if i:
        seq += 1
    else:
        seq = 0
    max_ = max(max_,seq)

print(max_)