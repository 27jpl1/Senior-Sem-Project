w = open("Genesis/Genesis 7", "r").readlines()
verses = []
for part in w:
    verses.append(part.split())

terms = {}
word_count = 0
for verse in verses:
    for word in verse:
        word_count += 1
        if word not in terms.keys():
            terms[word] = 1
        else:
            terms[word] += 1

term_frequency = {}
for key in terms.keys():
    term_frequency[key] = terms[key]/word_count

words = terms.keys()
print(words)

## And then I could return words, and update a global histogram of word count for corpus
## Also would return term_frequency
## Would then probably have to convert it to all words once all documents were processed