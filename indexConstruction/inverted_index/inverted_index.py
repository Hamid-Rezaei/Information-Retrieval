import pickle
import heapq
from indexConstruction.preprocessor.preprocessor import Preprocessor


class PositionalPosting:
    def __init__(self, position):
        self.positions = []
        self.tf = 0
        self.insert_position(position)

    def insert_position(self, position):
        self.positions.append(position)
        self.update_tf()

    def update_tf(self):
        self.tf = len(self.positions)

    def get_tf(self):
        return self.tf

    def __repr__(self):
        return (
            f"tf: {self.tf}, "
            f"positions: {self.positions}, "
        )


class Term:
    def __init__(self, docID, position):
        self.docID = docID
        self.postings_list = {}  # docID -> PositionalPosting
        self.champions_list = {}
        self.doc_frequency = 0
        self.collection_frequency = 0
        self.insert_posting(self.docID, position)

    def insert_posting(self, docID: int, position: int):
        if docID not in self.postings_list:
            posting: PositionalPosting = PositionalPosting(position)
            self.postings_list[docID] = posting
        else:
            posting: PositionalPosting = self.postings_list[docID]
            posting.insert_position(position)

        self.update_doc_frequency()
        self.update_collection_frequency()

    def update_doc_frequency(self):
        self.doc_frequency += len(self.postings_list.keys())

    def update_collection_frequency(self):
        for posting in self.postings_list.values():
            self.collection_frequency += posting.get_tf()

    def get_document_frequency(self):
        return self.doc_frequency

    def get_collection_frequency(self):
        return self.collection_frequency

    def create_champions_list(self, k: int):
        for docID, posting in self.postings_list.items():
            if posting.get_tf() >= k:
                self.champions_list[docID] = posting

    def __repr__(self):
        return (
            f"doc_frequency: {self.doc_frequency}, "
            f"collection_frequency: {self.collection_frequency}, "
            f"posting_list: {self.postings_list}, "
            f"champions_list: {self.champions_list}"
        )


class InvertedIndex:
    def __init__(self, documents):
        self.dictionary = {}  # token -> postings list
        self._create_inverted_index(documents)
        self._deleteTheKMostRepeatedTerms(k=50)
        self._create_champions_list(k=4)

    def _create_inverted_index(self, documents):
        for docID, document in documents.items():
            content = document['content']
            preprocessor = Preprocessor()
            tokens = preprocessor.preprocess(content)

            for position, token in enumerate(tokens):
                if token not in self.dictionary.keys():
                    term = Term(docID, position)
                    self.dictionary[token] = term
                else:
                    term = self.dictionary[token]
                    term.insert_posting(docID, position)

    def _create_champions_list(self, k: int):
        for term in self.dictionary.keys():
            term.create_champions_list(k)

    def _deleteTerm(self, term):
        self.dictionary.pop(term)

    def _deleteTheKMostRepeatedTerms(self, k: int):
        max_heap = []
        for term in self.dictionary.keys():
            heapq.heappush(max_heap, (-self.dictionary[term].get_collection_frequency(), term))

        k_most_repeated = []
        for _ in range(k):
            item = heapq.heappop(max_heap)
            self._deleteTerm(item[1])
            k_most_repeated.append(item)

        return [(-key, value) for key, value in k_most_repeated]

    def getPostingList(self, term: str):
        if term not in self.dictionary:
            return None

        term: Term = self.dictionary[term]
        return term.postings_list

    def getChampionList(self, term: str):
        if term not in self.dictionary:
            return None

        term: Term = self.dictionary[term]
        return term.champions_list

    @classmethod
    def save(cls, index, path: str):
        with open(path, 'wb') as file:
            pickle.dump(index, file)

    @classmethod
    def load(cls, path: str, mode: str):
        with open(path, mode) as file:
            obj = pickle.load(file)
        return obj

    def __repr__(self):
        return str(self.dictionary)
