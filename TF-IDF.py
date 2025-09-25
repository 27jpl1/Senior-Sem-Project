# A method that return the list of terms and a histogram of how many documents each term appears in
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


def tfidf(corpus):
    doc_dict = {}           # A dictionary where keys are document names and values are a list of words of what the document says
    doc_list = []           # A list of the names of the documents (Can just get this from doc_dict keys I think)
    for line in corpus:     # For each line(document) in the corpus, add it to doc_dict and doc_list
        line = line.strip()
        doc, words = line.split("|")          # The document name comes before the | and the words come after
        doc_dict[doc] = words.split()         # Adds the document to the dictionary with the words split into a list
        doc_list.append(doc)                  # Adds the name of the document to the document list
    term_list, term_hist = filter_terms(doc_dict)

    print(doc_dict)
    print(term_list)
    print(term_hist)
    # I now have term list and number of documents each term is found in
    # Need to determine idf score and tf score next
    # Eventually return a dictionary with keys as documents and values as idf scores
    # TODO Remember that the list of idf scores need to include every term (so any term not found in a document has a score of 0)

    return 0


document = open("Who Wrote the Bible Verse Combinations", "r")
tfidf(document.readlines())
