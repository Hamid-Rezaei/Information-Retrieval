# import json
#
# from invertedIndex.inverted_index.inverted_index import InvertedIndex
#
# PATH = "D:\Data\Docs\\University\\term7\Inforamtion Retrieval\project\search_engine\Dataset\IR_data_news_12k.json"
#
#
# def constructor():
#     with open(PATH, 'r') as news:
#         documents = json.load(news)
#
#     # inverted_index = InvertedIndex(documents=documents)
#     # inverted_index.save(inverted_index, 'inverted_index.pkl')
#
# class Term:
#     def __init__(self):
#         self.total_freq = 0
#         self.pos_in_doc = {}
#         self.freq_in_doc = {}
#
#     def update_posting(self, doc_id, term_position):
#       if doc_id not in self.pos_in_doc:
#             self.pos_in_doc[doc_id] = []
#             self.freq_in_doc[doc_id] = 0
#       self.pos_in_doc[doc_id].append(term_position)
#       self.freq_in_doc[doc_id] += 1
#       self.total_freq += 1
#
# def positional_indexing(preprocessed_docs):
#     p_inv_index = {}
#     for doc_id in range(len(preprocessed_docs)):
#         for pos in range(len(preprocessed_docs[doc_id])):
#             term = preprocessed_docs[doc_id][pos]
#             if term in p_inv_index:
#                 term_obj = p_inv_index[term]
#             else:
#                 term_obj = Term()
#             term_obj.update_posting(doc_id, pos)
#             p_inv_index[term] = term_obj
#
#     return p_inv_index
#
#
# if __name__ == "__main__":
#     # constructor()
#
#     def preprocess(contents, rm_sw=True, stemming=True):
#         preprocessed_docs = []
#         for content in contents:
#
#             # normalizing
#             normalized_content = normalizer.normalize(content)
#             content_tokens = tokenizer.tokenize_words(normalized_content)
#             tokens = []
#             for token in content_tokens:
#                 # stemming
#                 if stemming:
#                     token = stemmer.convert_to_stem(token)
#                 # remove stopwords
#                 if rm_sw:
#                     if token in stopwords:
#                         continue
#                 tokens.append(token)
#             preprocessed_docs.append(tokens)
#             # tokens of each doc
#         return preprocessed_docs
#
#     positional_index = positional_indexing(preprocessed_docs)
#
#     # ii: InvertedIndex = InvertedIndex.load('inverted_index.pkl', 'rb')
#     # print(ii.dictionary['ها'])

