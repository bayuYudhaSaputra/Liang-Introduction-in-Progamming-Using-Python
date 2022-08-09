print("\n Multiplication Table \n")

# Display the number title
print("  |", end = '')

for j in range(1, 10):
    print(" ", format(j,"2d"), end = '')
print() # jump to the new line
print("------------------------------------------")

for i in range(1,10):
    print(i, "|", end = '')
    for j in range(1,10):
        # Display the product and align properly
        print(format(i * j,"4d"), end = '')
    print() # jump to the new line

print("------------------------------------------")