assert '1001' == '1001'[::-1]
target = 0
for i in range(1000):
    for j in range(i, 1000):
        ij = i*j
        if str(ij) == str(ij)[::-1] and ij > target:
            target = ij

print(target)
