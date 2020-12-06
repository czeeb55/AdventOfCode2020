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
            formattedPassport = formattedPassport.replace("\n", " ")
            formattedPassport = formattedPassport.strip()
            listOfPassports.append(formattedPassport)
            passport = []
    #print(listOfPassports)
    return listOfPassports

# Could have made this return True/False
def validate_passport(passport):
    # Make sure fields exists
    fields = ["byr:","iyr:","eyr:","hgt:","hcl:","ecl:","pid:"]
    for field in fields:
        if not (field in passport):
            return "Bad"
    # Validate data
    byr = passport.split("byr:")[1].split(" ")[0]
    if not (len(byr) == 4 and 1920 <= int(byr) <= 2002):
        return "Bad"
   
    iyr = passport.split("iyr:")[1].split(" ")[0]
    if not (len(iyr) == 4 and 2010 <= int(iyr) <= 2020):
        return "Bad"

    eyr = iyr = passport.split("eyr:")[1].split(" ")[0]
    if not (len(eyr) == 4 and 2020 <= int(eyr) <= 2030):
        return "Bad"

    hgt = passport.split("hgt:")[1].split(" ")[0]

    if "cm" in hgt:
        if not (150 <= int(hgt.split("cm")[0]) <= 193):
            return "Bad"
    elif "in" in hgt:
        if not (59 <= int(hgt.split("in")[0]) <= 76):
            return "Bad"
    else:
        return "Bad"

    hcl = passport.split("hcl:")[1].split(" ")[0]
    if (hcl[0] == "#") and (len(hcl[1:]) == 6):
        try:
            int(hcl[1:],16) # Verifies hex
        except:
            return "Bad"
    else:
        return "Bad"
            
    
    ecl = passport.split("ecl:")[1].split(" ")[0]
    if len(ecl) != 3 or ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return "Bad"
    
    pid = passport.split("pid:")[1].split(" ")[0]
    if not (len(pid) == 9):
        return "Bad"
    return "Good"
    

formedPassports = form_passports(puzzleInput)
goodPassports = []
for passport in formedPassports:
    testPassport = validate_passport(passport)
    if testPassport == "Good":
        goodPassports.append(passport)

print(len(goodPassports))


for passport in goodPassports:
    print(passport.split("ecl:")[1].split(" ")[0])