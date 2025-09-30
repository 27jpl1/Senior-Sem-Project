# A method that returns the list of terms for all documents and a histogram of how many documents each term appears in
import math


def filter_terms(document_dictionary):
    term_list = []          # A list of all terms found in the corpus (This may need to be a set then convert to list)
    term_hist = {}          # A histogram of the number of documents the term appears in
    for key in document_dictionary.keys():     # Loops through all document and adds any new terms to the term_list and creates a term_hist
        terms_seen = set()          # For each document keep track of all the terms seen as to not double count
        for term in document_dictionary[key]:
            if term not in term_list:       # If term has not been seen in any document before, add it to the list
                term_list.append(term)
            if term not in terms_seen:      # If term has not been seen in this document before, increase its count in the histogram
                terms_seen.add(term)
                if term not in term_hist.keys():    # If term never seen before, set its histogram value to 1
                    term_hist[term] = 1
                else:
                    term_hist[term] += 1
    return term_list, term_hist

# A function to create a histogram of the number of times each term in a document appears
def document_term_frequency(doc_contents: list):
    doc_hist = {}
    for term in doc_contents:
        if term not in doc_hist.keys():
            doc_hist[term] = 1
        else:
            doc_hist[term] += 1
    return doc_hist


def tfidf(corpus):
    doc_dict = {}           # A dictionary where keys are document names and values are a list of words of what the document says
    doc_scores = {}         # A dictionary where keys a document names and values are idf scores for that document
    for line in corpus:     # For each line(document) in the corpus, add it to doc_dict and doc_list
        line = line.strip()
        doc, words = line.split("|")          # The document name comes before the | and the words come after
        doc_dict[doc] = words.split()         # Adds the document to the dictionary with the words split into a list
    term_list, term_hist = filter_terms(doc_dict)
    for doc in doc_dict.keys():
        doc_term_hist = document_term_frequency(doc_dict[doc])      # get the frequency of terms in a document
        idf_scores = []                       # A list of idf score for each term
        for term in term_list:                # Append the score of each term to the list
            if term in doc_term_hist.keys():
                score = (doc_term_hist[term]/len(doc_dict[doc])) * math.log(len(doc_dict.keys())/term_hist[term])
                idf_scores.append(score)
            else:
                idf_scores.append(0)
        doc_scores[doc] = idf_scores

    # could have a function create a list of term_idf_scores
    # then just loop through documents and find term frequency for every term and multiply to get score
    # keep scores in list and then have it as a value to a document key
    print(doc_dict)
    print(term_list)
    print(term_hist)
    for doc in doc_dict:
        print(doc, doc_scores[doc])
    return doc_scores


document = open("Who Wrote the Bible Verse Combinations", "r")
tfidf(document.readlines())
