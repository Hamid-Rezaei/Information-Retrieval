from preprocessor.utils import SPACE


class Tokenizer:
    def tokenize(self, in_string):
        tokens = in_string.split(SPACE)
        return list(filter(None, tokens))
