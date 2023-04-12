# Exercises on Recursion

given_list = [1, 2, 3, 4, 5, -4, -2, -2, -1]
total = 0

for num in given_list:
    if num < 0:
        total += num
print(total)
