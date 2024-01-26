HALF_SPACE = '\u2009'
ZERO_WIDTH = '\u200C'
SPACE = ' '
REPLACE_MAP = {
    '\u200c': ZERO_WIDTH,
    '\u200B': ZERO_WIDTH,
    '\u200D': ZERO_WIDTH,
    '\u00ad': ZERO_WIDTH,
    '\xad': ZERO_WIDTH,
    '\u200f': ZERO_WIDTH,
    '\u0020': SPACE,
    '\u00a0': SPACE,
    '\u0009': SPACE,
    '\u000a': SPACE,
    '\u2002': SPACE,
    '\u2003': SPACE,
    '\u2004': SPACE,
    '\u2005': SPACE,
    '\u2006': SPACE,
    '\u2007': SPACE,
    '\u2008': SPACE,
    '\u2009': SPACE,
    '\u200a': SPACE,
    'ئ': 'ی',
    'ي': 'ی',
    'یٰ': 'ی',
    'ك': 'ک',
    'ة': 'ه',
    'ؤ': 'و',
    'آ': 'ا',
    'أ': 'ا',
    'ٱ': 'ا',
    'إ': 'ا',
    '1': '۱',
    '2': '۲',
    '3': '۳',
    '4': '۴',
    '5': '۵',
    '6': '۶',
    '7': '۷',
    '8': '۸',
    '9': '۹',
    '0': '۰',
    '-': ' ',
    '/': ' ',
    '\\': ' ',
    '﷽': "بسم-الله-الرحمن-الرحیم",
    'ﷻ': "الله-جل-جلاله",
    'ﷺ': "صلی-الله-علیه-وسلم",
    'ﷲ': "الله",
    'ﷳ': "اکبر",
    'ﷴ': "محمد",
    'ﷵ': "صلی-الله-علیه-وسلم",
    'ﷶ': "رسول",
    'ﷷ': 'علیه-السلام',
    'ﷸ': "صلی-الله-علیه-وسلم",
    'ﷹ': "صلی-الله-علیه-وسلم",
    '%': "درصد",
    '٪': "درصد",
    '_': ' ',
    'ـ': ' ',
    'ۀ': 'ه',
    'ة': 'ه',
}

DELETE_CHARACTER = [
    '\u064b', '\u064c', '\u064d', '\u064e', '\u064f', '\u0650', '\u0651', '\u0621', '\u0652', '\u0670',
    '\u0654', '\u0640', '۞', '۩', '\ufdf2', '\u0611', '\u0612', '\u0613', '\u0614', '\u0615', '\u0616',
    '\u0617', '\u0618', '\u0619', '\u0620', '!', ',', '?', ':', '،', '؛', '.', '(', ')', '؟', '«', '»',
    '#', '*', '《', '》', '\"', '[', ']', '{', '}'
]

PRE_SUBSTRING = [
    "ی", "ای", "ها", "های", "هایی", "تر", "تری", "ترین", "گر", "گری", "وری", "ام",
    "ات", "اش", "مان", "تان", "شان", "گانه"
]

POST_SUBSTRING = [
    "می", "نمی"
]

PERSIAN_NUMBERS = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']


class Normalizer:

    def invalid_character_handler(self, in_string: str):
        def replace_char(char):
            return REPLACE_MAP[char] if char in REPLACE_MAP else char

        result_list = [
            replace_char(char) if char not in DELETE_CHARACTER else ''
            for char in in_string
        ]

        # Compact consecutive space characters
        normal_string = ''.join(result_list)
        normal_string = normal_string.replace(SPACE * 2, SPACE)

        return normal_string

    def number_spacing_handler(self, in_string: str):
        normal_string = [
            (SPACE if char in PERSIAN_NUMBERS and prev_char not in PERSIAN_NUMBERS else "")
            + char
            for prev_char, char in zip([''] + list(in_string), in_string)
        ]

        return ''.join(normal_string)

    def word_spacing_handler(self, in_string: str):
        words = in_string.split(SPACE)

        normal_string = [
            (ZERO_WIDTH if i > 0 and words[i - 1] in PRE_SUBSTRING else "") + SPACE + word
            if i > 0
            else word
            for i, word in enumerate(words)
            if word  # Filter out empty strings
        ]

        return "".join(normal_string)

    def normalize(self, in_string: str):
        in_string = self.invalid_character_handler(in_string)
        in_string = self.number_spacing_handler(in_string)
        in_string = self.word_spacing_handler(in_string)
        return in_string


class Tokenizer:
    def tokenize(self, in_string):
        tokens = in_string.split(SPACE)
        return list(filter(None, tokens))


def stop_words_handler(in_string: str):
    ...


if __name__ == "__main__":
    s = "124 ي يآری سًژئأآة»]َُيك . جزء"
    print(Normalizer().invalid_character_handler(s))

    s = "کتاب داستان۴۵۶"
    print(Normalizer().number_spacing_handler(s))

    s = "می‌توانم من‌تر بهره‌وری"
    print(Normalizer().word_spacing_handler(s).split(' '))
