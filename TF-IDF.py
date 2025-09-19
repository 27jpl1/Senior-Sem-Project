# TODO: Make decision about how to represent data (probably check with Dr. Ferrer then implement
def tfidf(corpus):
    ## probably have corpus be a list of documents, where each document is just the string of words
    ## make list of every term in each document
    ## could also make a histogram with term as the key and number of documents seen in as the value
    ## to help with histogram can use a set for list of terms so quick check if term has already been seen
    ## while going through could also make histogram for each document
    ## I do need some way to label document, or maybe a list of histograms

    ## so I think I need a list of lists containing all terms in a given document
    ## A list of histograms of number of times a term shows up in a given document (could just be frequency of that term)
    ## A histogram of the number of documents a term is found in
    return 0

## possibly have a list of every term in each document to help with idf
## could have a list of those lists so just iterate through the list and then check if term in the sublists#
## probably remove tf and just make a histogram of frequency of terms in a document and use to determine tf
