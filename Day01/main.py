tryList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
givenDict =  {'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}




"""matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposedMatrix = []
    for _ in range(cols):
        transposedMatrix.append([])

    for i in range(rows):
        for j in range(cols):
            transposedMatrix[j].append(matrix[i][j])
    return transposedMatrix

transposedMatrix = transpose(matrix)


# Print the result
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposedMatrix:
    print(row)"""


"""myString = "qwertyuioppoiuytrewq"

newString = ""

strLength = len(myString)
while strLength > 0:
    newString += myString[strLength-1]
    strLength -= 1

if myString == newString:
    print("Palindrom")
else: print("Not Palindrom")

print(myString)
print(newString)"""


"""newDict = {}
for key, value in givenDict.items():
    newDict[value] = key
#    newDict[key] = value

for key, value in newDict.items():
    print(f"key: {key}, value: {value}")"""

"""listLength = len(tryList) - 1

while listLength>=0:
    print(tryList[listLength])
    listLength -= 1"""

"""a = "AQuickBrownFoxJumpsOverTheLazyDog"
length = len(a)
while(length > 0):
    print(a[length])
    length -= 1"""

"""a = "AQuickBrownFoxJumpsOverTheLazyDog"
length = len(a) - 1  # Start from the last index (zero-based indexing)
while length >= 0:  # Loop until the first index (inclusive)
    print(a[length])  # Print the character at the current index
    length -= 1  # Decrement the index"""

