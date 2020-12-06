puzzleInput = open("day4.txt").readlines()

def form_passports(completeInput):
    listOfPassports = []
    passport = []
    for idx,line in enumerate(completeInput):
        if line != "\n":
            passport.append(line)
        if line == "\n" or idx == (len(completeInput) -1):
            formattedPassport = ""
            for row in passport:
                formattedPassport += row
            listOfPassports.append(formattedPassport)
            passport = []
    #print(listOfPassports)
    return listOfPassports

def validate_passport(passport):
    fields = ["byr:","iyr:","eyr:","hgt:","hcl:","ecl:","pid:"]
    for field in fields:
        if not field in passport:
            return "Bad"
    return "Good"



formedPassports = form_passports(puzzleInput)
goodPassports = []
for passport in formedPassports:
    testPassport = validate_passport(passport)
    if testPassport == "Good":
        goodPassports.append(passport)

print(len(goodPassports))