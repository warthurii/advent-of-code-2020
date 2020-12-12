with open("input.txt") as infile:
    fileText = infile.read()

passports = fileText.split("\n\n")

passports = [string.replace("\n", " ") for string in passports]
    
passports = [string.split() for string in passports]

dictionaryList = []

for item in passports:
    dictionary = {}
    for x in item:
        cat, value = x.split(":")
        dictionary[cat] = value
    
    dictionaryList.append(dictionary)
valid = 0
valid2 = 0

def hasValidVals(item):
    validbyr = 1920 <= int(item["byr"]) <= 2002
    validiyr = 2010 <= int(item["iyr"]) <= 2020
    valideyr = 2020 <= int(item["eyr"]) <= 2030

    validhgt = False
    unit = item["hgt"][-2:]
    if(unit == "cm"):
        height = int(item["hgt"][:-2])
        validhgt = 150 <= height <= 193
    elif(unit == "in"):
        height = int(item["hgt"][:-2])
        validhgt = 59 <= height <= 76


    def validString(string):
        val = string.lower()
        isvalid = True

        for char in val:
            if char not in "0123456789abcdef":
                isvalid = False
                break
        return isvalid

    validhcl = False
    if(len(item["hcl"]) == 7):
        digits = item["hcl"][1:]
        validhcl = validString(digits)

    validecl = item["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def is_valid_passport_id(value):
        is_valid = False
        
        if len(value) == 9:
            is_valid = True
 
            for character in value:
                if character not in "0123456789":
                    is_valid = False
                    break
        
        return is_valid

    validpid = is_valid_passport_id(item["pid"])

    return(
        validbyr and validiyr and
        valideyr and validhgt and
        validhcl and validecl and
        validpid
    )

for item in dictionaryList:
    if("byr" in item and "iyr" in item and "eyr" in item and "hgt" in item and "hcl" in item and "ecl" in item and "pid" in item):
        if(hasValidVals(item)):
            valid2 += 1
        valid += 1

print(valid2)
     