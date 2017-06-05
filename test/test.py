import unittest

import HTMLConfiguration
import PhraseSearcher

class MyTest(unittest.TestCase):
    def test_HTMLConfiguration(self):
        self.assertTrue(HTMLConfiguration.createHtml("pen", "apple"),
                       "http://www.tekstowo.pl/piosenka,pen,apple.html")

    def test_containsGood(self):
        self.assertTrue(PhraseSearcher.contains(
            ['a', 'b'],['a', 'b', 'c']))

    def test_containsWrong(self):
        self.assertFalse(PhraseSearcher.contains(
            ['a', 'b'],['a', 'c']))

    def test_containsWrongOrderMatters(self):
        self.assertFalse(PhraseSearcher.contains(
            ['a', 'b'],['b', 'a']))

    def test_containsWrongOneAfterOne(self):
        self.assertFalse(PhraseSearcher.contains(
            ['a', 'b'],['a', 'c', 'b']))
