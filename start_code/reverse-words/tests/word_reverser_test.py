import unittest
from src.word_reverser import *

class TestWordReverse(unittest.TestCase):
    

    # Have unit tests for the following sentences 

    # "Hello this is a test fantastic"
    def test_word_reverser(self):
        word_reverser = WordReverser("Hello this is a test fantastic")
        result = word_reverser.reverse_string(word_reverser)
        self.assertEqual("olleH this is a test citsatnaf ", result)

    # "The cat was cute and he was called Azzazel"
    def test_word_reverser_2(self):
        word_reverser = WordReverser("The cat was cute and he was called Azzazel")
        result = word_reverser.reverse_string(word_reverser)
        self.assertEqual("The cat was cute and he was dellac lezazzA ", result)

    # "Very cool hat"
    def test_word_reverser_3(self):
        word_reverser = WordReverser("Very cool hat")
        result = word_reverser.reverse_string(word_reverser)
        self.assertEqual("Very cool hat ", result)
    
