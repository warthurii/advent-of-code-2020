def removeN(groups):
    for group in groups:
        group = group.replace("\n", "")
    return(groups)

def getCount(groups):
    count = 0
    for group in groups:
        questions = []
        for letter in group:
            if(letter not in questions):
                questions.append(letter)
        count += len(questions)

    return count


with open("input.txt") as infile:
    fileText = infile.read()

groups = []
groups = fileText.split("\n\n")
groups = removeN(groups)

print(getCount(groups))