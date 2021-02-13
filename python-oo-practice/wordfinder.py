"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """
    A class used to get a random word from a dictionary file

    Attributes
    -------------
    word_list: list 
        list of all words in dictionary file

    >>> w = WordFinder('test_dict.txt')
    8 words read

    >>> w.random() in ["specialism","specialist","specialistic","speciality","specialization","specialize","specialized","specializer"]
    True
    """

    def __init__(self, filepath):
        """Create list of word attributes"""
        dictionary = open(filepath, "r")
        self.word_list = self.generate_dict(dictionary)

        print(f"{len(self.word_list)} words read")

    def __repr__(self):
        """creates string description of the instance"""
        return f"WordFinder(filename={self.filename} file_object={self.file_object})"

    def generate_dict(self, dictionary):
        """Create list of all dictionary file words"""
        return [word.strip() for word in dictionary]

    def random(self):
        """Randomly generate word from dictionary"""
        return random.choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """Special word finder that excludes blank lines and comments"""

    def generate_dict(self, dictionary):
            """Create list of all dictionary file words"""
            return [word.strip() for word in dictionary if word.strip() and not word.startswith("#")]