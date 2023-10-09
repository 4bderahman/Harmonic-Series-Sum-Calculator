# intering the value of n
n = int(input("Enter the value of n: "))

s = 0

# Loop to calculate the sum
for i in range(1, n + 1):
    s += 1/i

# the result of the sum
print("The sum s for n =", n, "is:", s)
