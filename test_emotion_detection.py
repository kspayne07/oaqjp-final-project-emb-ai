import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result1 = emotion_detector('I am glad this happened')
        self.assertTrue(result1['dominant_emotion'], 'joy')

        result2 = emotion_detector('I am really mad about this')
        self.assertTrue(result2['dominant_emotion'], 'anger')

        result3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertTrue(result3['dominant_emotion'], 'disgust')

        result4 = emotion_detector('I am so sad about this')
        self.assertTrue(result4['dominant_emotion'], 'sadness')

        result5 = emotion_detector('I am really afraid that this will happen')
        self.assertTrue(result5['dominant_emotion'], 'fear')

unittest.main()