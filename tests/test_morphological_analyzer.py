import unittest
from sanskrit_grammar.morphological_analyzer import analyze_sanskrit_word, identify_pratyaya

class TestMorphologicalAnalyzer(unittest.TestCase):
    def test_analyze_sanskrit_word(self):
        # Test basic word analysis
        result = analyze_sanskrit_word('गच्छति')
        self.assertIsNotNone(result)
        self.assertIn('धातु', result)  # Should contain root
        self.assertIn('प्रत्यय', result)  # Should contain suffix
        
    def test_identify_pratyaya(self):
        # Test pratyaya (suffix) identification
        result = identify_pratyaya('करोति')
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, dict))
        
    def test_with_upasarga(self):
        # Test words with prefixes (upasarga)
        result = analyze_sanskrit_word('प्रगच्छति')
        self.assertIsNotNone(result)
        self.assertIn('उपसर्ग', result)
        self.assertEqual(result['उपसर्ग'], 'प्र')

    def test_invalid_input(self):
        # Test handling of invalid inputs
        result = analyze_sanskrit_word('')
        self.assertEqual(result, {})
        result = analyze_sanskrit_word('xyz123')
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()
