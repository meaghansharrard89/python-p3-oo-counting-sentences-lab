#!/usr/bin/env python3

import re


class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
        self._value = value

    @property
    def value(self):
        """The value property."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Setter for the value property"""
        if not isinstance(new_value, str):
            print("The value must be a string.")
        self._value = new_value

    def is_sentence(self):
        """Evaluates if the sentence has a period or not."""
        return self._value.endswith(".")

    def is_question(self):
        """Evaluates whether there's a question mark or not."""
        return self.value.endswith("?")

    def is_exclamation(self):
        """Evaluates whether the sentence ends in an exclamation point or not"""
        return self.value.endswith("!")

    def is_sentence(self):
        """Check if the instance ends with a punctuation"""
        return any(self._value.endswith(punctuation) for punctuation in [".", "!", "?"])

    def count_sentences(self):
        """Counts how many sentences are in the instance"""
        punctuations = r"[.!?]+"
        sentences = re.split(punctuations, self._value)
        non_empty_sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(non_empty_sentences)

    pass
