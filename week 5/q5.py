import string
sentence = input()
# Convert to lowercase
sentence = sentence.lower()
# Remove punctuation
for ch in string.punctuation:
    sentence = sentence.replace(ch, "")
# Split into words
words = sentence.split()
# Count occurrences
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

