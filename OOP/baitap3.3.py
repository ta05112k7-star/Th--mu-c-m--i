def print_grid4():
    line1 = "+ - - - - " * 4 + "+"
    line2 = "|         " * 4 + "|"
    for i in range(4):
        print(line1)
        for j in range(4):
            print(line2)
    print(line1)
print_grid4()