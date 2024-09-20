def main():
    inputFile = open("puzzleinput.txt", "r")
    calibrationValue = 0
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    for line in inputFile:
        firstDigit = 0
        lastDigit = 0
        checkDigit = ""
        reverseLine = line [::-1]
        for char in line: #Find first digit
            if firstDigit != 0:
                break
            elif char.isdigit(): #If int, assign
                firstDigit = int(char)
                checkDigit = ""
            else: #If not, add to string to check dictionary for it
                checkDigit += str(char)
                for number in digits.keys():
                    if number in checkDigit:
                        firstDigit = int(digits[number])
                        checkDigit = ""
        char = ""
        for char in reverseLine: #Find last digit
            if lastDigit != 0:
                break
            elif char.isdigit():
                lastDigit = int(char)
                checkDigit = ""
            else: #Add to string in reverse order
                checkDigit = str(char)+checkDigit
                for number in digits.keys():
                    if number in checkDigit:
                        lastDigit = int(digits[number])
                        checkDigit = ""

        calibrationValue += int(str(firstDigit)+str(lastDigit))

    inputFile.close()
    print(f"SOLUTION: Sum of all the calibration values is {calibrationValue}") 

if __name__== "__main__":
    main()
