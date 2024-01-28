import math


def calculate_tf(term, doc_id):
    term_freq = term.term_freq_in_docs[doc_id]
    return 1 + math.log10(term_freq) if term_freq > 0 else 0


def calculate_idf(term, collection_size):
    term_freq = len(term.term_freq_in_docs)
    return math.log10(collection_size / term_freq)


def calculate_tf_idf(term, doc_id, collection_size):
    return calculate_tf(term, doc_id) * calculate_idf(term, collection_size)


def calculate_tf_for_query(term, query_tokens):
    freq = sum(1 for token in query_tokens if token == term)
    if freq > 0:
        return 1 + math.log10(freq)
    return 0


def calculate_weights_for_all_terms(dictionary, collection_size):
    for term in dictionary:
        postings_list = dictionary[term].get_docs()
        for doc_id in postings_list:
            dictionary[term].calculate_weight(doc_id, collection_size)
