file = open("num.txt", "r")

nums = []

for num in file:
    nums.append(int(num))

file.close()

for num in nums:
    if 2020 - num in nums:
        print(num * (2020 - num))
        break

