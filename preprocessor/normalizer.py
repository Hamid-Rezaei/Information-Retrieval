from preprocessor.utils import REPLACE_MAP, DELETE_CHARACTER, SPACE, PERSIAN_NUMBERS, PRE_SUBSTRING, ZERO_WIDTH


class Normalizer:

    def replace_invalid_character(self, in_string: str):
        replaced_list = [REPLACE_MAP.get(char, char) for char in in_string]
        normal_string = ''.join(replaced_list)

        return normal_string

    def delete_invalid_character(self, in_string: str):
        result_list = [
            char if char not in DELETE_CHARACTER else ''
            for char in in_string
        ]
        normal_string = ''.join(result_list)

        return normal_string

    def correct_number_spacing(self, in_string: str):
        normal_string = [
            (SPACE if char in PERSIAN_NUMBERS and prev_char not in PERSIAN_NUMBERS else "")
            + char
            for prev_char, char in zip([''] + list(in_string), in_string)
        ]

        return ''.join(normal_string)

    def correct_word_spacing(self, in_string: str):
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
        in_string = self.delete_invalid_character(in_string)
        in_string = self.replace_invalid_character(in_string)
        in_string = self.correct_number_spacing(in_string)
        in_string = self.correct_word_spacing(in_string)
        return in_string


if __name__ == "__main__":
    s = "124 ي يآری سًژئأآة»]َُيك . جزء"
    print(Normalizer().delete_invalid_character(s))

    s = "124 ي يآری سًژئأآة»]َُيك . جزء"
    print(Normalizer().replace_invalid_character(s))

    s = "کتاب داستان۴۵۶"
    print(Normalizer().correct_number_spacing(s))

    s = "می‌توانم من‌تر بهره‌وری"
    print(Normalizer().correct_word_spacing(s).split(' '))
