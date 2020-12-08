infile = open("input.txt", "r")

count = 0
treeCount = 0

for line in infile:
    line.strip()

    if(line[count] == "#"):
        treeCount += 1

    count += 3

    if(count > 30):
        count = count - 30
        if(count > 0):
            count -= 1

print(treeCount)

infile.close()