with open("input.txt") as infile:
    fileText = infile.read()

passports = fileText.split("\n\n")

passports = [string.replace("\n", " ") for string in passports]
    
passports = [string.split() for string in passports]

dictionary = {}

for item in passports:
    dictionary = {}
    for x in item:
        cat, value = x.split(":")
        dictionary[cat] = value
    
    item = dictionary

print(passports)
     