#!/usr/bin/env python3

import re 

class MyString:
    def __init__(self, value=''):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        self.__value = new_value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = re.split(r'[.!?]+', self.value)
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)


simple_string = MyString("one. two. three?")
empty_string = MyString()
complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")


assert simple_string.count_sentences() == 3
assert empty_string.count_sentences() == 0
assert complex_string.count_sentences() == 4