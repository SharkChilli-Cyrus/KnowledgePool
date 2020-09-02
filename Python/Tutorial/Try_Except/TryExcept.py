import sys
import os

print("Enter 'q' to quit.")

activeOption = True
while activeOption == True:
    firstNumber = input("\nFirst Number: ")
    if firstNumber == 'q':
        activeOption = False
        break
    else:
        pass

    secondNumber = input("\nSecond Number: ")
    if secondNumber == 'q':
        activeOption = False
        break
    else:
        pass

    result = int(firstNumber) / int(secondNumber)
    print("\nResult: {0}".format(result))
