# Initialize sum
sum = 0
# Add 0.01, 0.02, ..., 0.99, 1 to sum
count = 0
i = 0.01
while count < 100:
    sum += i
    i = i + 0.01
    count += 1 # Increase count
# Display result
print("\n The sum is", sum, "\n")