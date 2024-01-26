from preprocessor.utils import REPLACE_MAP, DELETE_CHARACTER, SPACE, PERSIAN_NUMBERS, PRE_SUBSTRING, ZERO_WIDTH


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


if __name__ == "__main__":
    s = "124 ي يآری سًژئأآة»]َُيك . جزء"
    print(Normalizer().invalid_character_handler(s))

    s = "کتاب داستان۴۵۶"
    print(Normalizer().number_spacing_handler(s))

    s = "می‌توانم من‌تر بهره‌وری"
    print(Normalizer().word_spacing_handler(s).split(' '))
