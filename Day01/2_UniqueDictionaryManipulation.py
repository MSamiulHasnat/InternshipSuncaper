givenDict =  {'audi': 'q7', 'xiaomi': 'su7', 'mercedes': 'benz'}
newDict = {}

for brand, model in givenDict.items():
    newDict[model] = brand

print("Printing Original dictionary:")
for key, value in givenDict.items():
    print(f"brand- {key}, model- {value}")
print()


print("Printing new dictionary:")
for key, value in newDict.items():
    print(f"brand- {key}, model- {value}")
print()

