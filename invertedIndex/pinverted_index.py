import pickle

from invertedIndex.vectorspace import calculate_tf_idf


class Term:
    def __init__(self):
        self.collect_freq = 0
        self.position_in_docs = {}
        self.term_freq_in_docs = {}
        self.weight_in_docs = {}
        self.champions_list = {}

    def create_champ_list(self, k):
        self.champions_list = dict(sorted(self.weight_in_docs.items(), key=lambda item: item[1], reverse=True)[:k])

    def get_champ_list(self):
        return self.champions_list

    def calculate_weight(self, doc_id, collection_size):
        self.weight_in_docs[doc_id] = calculate_tf_idf(
            self,
            doc_id,
            collection_size
        )

    def get_weight_in_doc(self, doc_id):
        return self.weight_in_docs[doc_id]

    def get_docs(self):
        return self.position_in_docs.keys()

    def update_postings_list(self, doc_id, term_position):
        if doc_id not in self.position_in_docs:
            self.position_in_docs[doc_id] = []
            self.term_freq_in_docs[doc_id] = 0
        self.position_in_docs[doc_id].append(term_position)
        self.term_freq_in_docs[doc_id] += 1
        self.collect_freq += 1


class InvertedIndex:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def save(self, path: str):
        with open(path, 'wb') as file:
            pickle.dump(self.dictionary, file)

    def load(self, path: str):
        with open(path, 'wb') as file:
            dictionary = pickle.load(file)
        return dictionary
