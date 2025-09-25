# TODO: Make decision about how to represent data (probably check with Dr. Ferrer then implement)
def tfidf(corpus):
    doc_dict = {}           # A dictionary where keys are document names and values are a list of words of what the document says
    doc_list = []           # A list of the names of the documents (Can just get this from doc_dict keys I think)
    for line in corpus:     # For each line(document) in the corpus, add it to doc_dict and doc_list
        line = line.strip()
        doc, words = line.split("|")          # The document name comes before the | and the words come after
        doc_dict[doc] = words.split()         # Adds the document to the dictionary with the words split into a list
        doc_list.append(doc)                  # Adds the name of the document to the document list
    term_list = []          # A list of all terms found in the corpus (This may need to be a set then convert to list)
    for key in doc_dict.keys():     # Loops through all document and adds any new terms to the term_list
        for term in doc_dict[key]:
            if term not in term_list:
                term_list.append(term)
    print(doc_dict)
    print(term_list)

    # I now have term list, need to determine idf score and tf score next
    # Could maybe find # of documents a term is in in above loop

    return 0


document = open("Who Wrote the Bible Verse Combinations", "r")
tfidf(document.readlines())

## possibly have a list of every term in each document to help with idf
## could have a list of those lists so just iterate through the list and then check if term in the sublists#
## probably remove tf and just make a histogram of frequency of terms in a document and use to determine tf

## probably have corpus be a list of documents, where each document is just the string of words
## make list of every term in each document
## could also make a histogram with term as the key and number of documents seen in as the value
## to help with histogram can use a set for list of terms so quick check if term has already been seen
## while going through could also make histogram for each document
## I do need some way to label document, or maybe a list of histograms

## so I think I need a list of lists containing all terms in a given document
## A list of histograms of number of times a term shows up in a given document (could just be frequency of that term)
## A histogram of the number of documents a term is found in

## Have file as
## Book Chapters Verse : Words (Ex: Genesis 2:1-3:14 | Blah Blah Blah)
## Can then use the | to split the line the left half becomes the key to a dictionary,
## the right then becomes split again into its individual words and stored as the value
## While creating the dictionary could also run through all words and add to word list
## once all run through, then create another dictionary mapping to idf scores
## That dictionary could then be passed to k-means clustering

## Things I need:
## List of terms in all documents               (List)
## The numbers of documents each term is in     (Histogram: Term -> Number)
## The frequency of a term in a given document  (Dictionary: Document -> Dictionary : Term -> Number)

## Could find IDF score first then pass list of terms to find term frequency
## This would have a dictionary with each term as the key and the value as the idf score
