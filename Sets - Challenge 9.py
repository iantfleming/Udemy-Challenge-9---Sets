sampleText = "Python is a very powerful language"
vowels = frozenset("aeiou")
finalSet = set(sampleText).difference(vowels)

finalList = sorted(finalSet)
print(finalList)