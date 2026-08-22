# Find most frequent word in a text file, ignore punctuation and case
import string

file = open("text.txt", "r")
text = file.read().lower()
file.close()

# Remove punctuation
for p in string.punctuation:
    text = text.replace(p, "")

words = text.split()

count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

max_word = ""
max_count = 0

for word in count:
    if count[word] > max_count:
        max_count = count[word]
        max_word = word

print("Most frequent word:", max_word)
print("Frequency:", max_count)