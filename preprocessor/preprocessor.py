# from parsivar import FindStems
#
# from preprocessor.normalizer import Normalizer
# from preprocessor.tokenizer import Tokenizer
#
#
# class Preprocessor:
#     def __init__(self):
#         ...
#
#     def preprocess(self, in_string: str):
#         normalizer = Normalizer()
#         tokenizer = Tokenizer()
#         stemmer = FindStems()
#
#         normal_string = normalizer.normalize(in_string)
#         tokens = tokenizer.tokenize(normal_string)
#
#         stem_tokens = [stemmer.convert_to_stem(token) for token in tokens]
#
#         return stem_tokens
