# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

# text = input("Please enter some text: ")
#
# for char in text:
#     if char in'AEIOUaeiou' or char in ' ':
#         continue
#     else:
#         x = set(char)
#         print(sorted(x),end='')

sampleText = "Python is a very powerful language"
vowels = frozenset("aeiou")
finalSet = set(sampleText).difference(vowels)

finalList = sorted(finalSet)
print(finalList)