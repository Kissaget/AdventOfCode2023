def main():
    inputFile = open("puzzleinput.txt", "r")
    calibrationValue = 0

    for line in inputFile:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(int(char))

        calibrationValue += int(str(digits[0])+str(digits[-1]))

    inputFile.close()
    print(f"SOLUTION: Sum of all the calibration values is {calibrationValue}") 

if __name__== "__main__":
    main()
