# Write a Program which takes the path of a file from the user and outputs the number of words used in the file
filename = input("Please enter path of a Text file: ")
print(filename)
f = open(filename)
numberofwords = 0
for line in f: 
    words = line.split()
    numberofwords = numberofwords + len(words)

print("number of words are: ")
print(numberofwords)
