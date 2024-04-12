from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result_1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(result_1['label'], "SENT_POSITIVE") # unit tests
        result_2 = sentiment_analyzer("I hate working with Pyhton")
        self.assertEqual(result_2['label'], "SENT_NEGATIVE")
        result_3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(result_3['label'], "SENT_NEUTRAL")

unittest.main() # call the unit tests
