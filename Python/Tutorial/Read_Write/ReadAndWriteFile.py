import sys
import os

rootPath = os.path.dirname(os.path.abspath(__file__))
print("* Root Path: {0}".format(rootPath))

filePath = os.path.join(rootPath, "pi_digits.txt")

# with open(filePath) as fileObject:
#     contents = fileObject.read()
#     print(contents.rstrip())


# with open(filePath) as fileObject:
#     contents = []
#     for line in fileObject:
#         # two \n
#         # there is an invisible \n at the end of each row in the file, and using print would add one more \n at the end
#         print(line.rstrip()) 

#         contents.append(line)
#     print(contents)


# with open(filePath) as fileObject:
#     lines = fileObject.readlines()
# print(lines)
# piString = ''
# for line in lines:
#     piString += line.strip()
# print(piString)

writeFilePath = os.path.join(rootPath, "test_file.txt")
with open(writeFilePath, 'r+') as fileObject:
    fileObject.write("This is the first line.\nThis is the second line.\n")