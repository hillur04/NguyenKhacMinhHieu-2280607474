nhapchuoi = input("nhập x, y: ")
dimension = [int(x) for x in nhapchuoi.split(',')]
sodong = dimension[0]
socot = dimension[1]
multilist = [[0 for col in range(socot)] for row in range(sodong)]
for row in range(sodong):
    for col in range(socot):
        multilist[row][col] = row * col
print (multilist)