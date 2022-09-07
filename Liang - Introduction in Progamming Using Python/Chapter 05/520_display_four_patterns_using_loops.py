print("-----------------")
print("Pattern A")
print("-----------------")
for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print("\n")
print("-----------------\n")

print("-----------------")
print("Pattern B")
print("-----------------")
for i in range(6, 0, -1):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print("\n")
print("-----------------\n")

print("-----------------")
print("Pattern C")
print("-----------------")
for i in range(1, 7):
    for j in range(6, 0, -1):
        if (j - i <= 0):
            print(j, end = ' ')
        else:
            print(" ",end = ' ')
    print("\n")
print("-----------------\n")