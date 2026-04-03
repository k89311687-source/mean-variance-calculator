import math

# Input numbers
numbers = list(map(float, input("Enter numbers separated by space: ").split()))

# Step 1: Mean
mean = sum(numbers) / len(numbers)

# Step 2: Variance
variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)

# Step 3: Standard Deviation
std_dev = math.sqrt(variance)

# Output
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)