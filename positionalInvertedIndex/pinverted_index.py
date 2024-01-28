class Term:
    def __init__(self):
        self.collect_freq = 0
        self.position_in_docs = {}
        self.term_freq_in_docs = {}
        self.weight_in_doc = {}
        self.champions_list = {}

    def update_posting(self, doc_id, term_position):
        if doc_id not in self.position_in_docs:
            self.position_in_docs[doc_id] = []
            self.term_freq_in_docs[doc_id] = 0
        self.position_in_docs[doc_id].append(term_position)
        self.term_freq_in_docs[doc_id] += 1
        self.collect_freq += 1

    def get_docs(self):
        return self.position_in_docs.keys()

    def get_weight_in_doc(self, doc_id):
        return self.weight_in_doc[doc_id]

    def calculate_weight(self, doc_id, collection_size):
        self.weight_in_doc[doc_id] = calculate_tf_idf(self, doc_id, collection_size)

    def create_champ_list(self, k):
        self.champions_list = dict(sorted(self.weight_in_doc.items(), key=lambda item: item[1], reverse=True)[:k])

    def get_champ_list(self):
        return self.champions_list
