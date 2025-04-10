import unittest
from sanskrit_grammar.sandhi import sandhi_handler, apply_vowel_sandhi, apply_consonant_sandhi

class TestSandhi(unittest.TestCase):
    def test_vowel_sandhi(self):
        # Test vowel sandhi combinations
        self.assertEqual(apply_vowel_sandhi('राम', 'इति'), 'रामेति')
        self.assertEqual(apply_vowel_sandhi('देव', 'आलय'), 'देवालय')
        
    def test_consonant_sandhi(self):
        # Test consonant sandhi combinations
        self.assertEqual(apply_consonant_sandhi('वाक्', 'देवी'), 'वाग्देवी')
        self.assertEqual(apply_consonant_sandhi('तत्', 'कार'), 'तत्कार')

    def test_sandhi_handler(self):
        # Test the main sandhi handler function
        self.assertEqual(sandhi_handler('राम', 'इति'), 'रामेति')
        self.assertEqual(sandhi_handler('देव', 'आलय'), 'देवालय')

    def test_invalid_inputs(self):
        # Test handling of invalid inputs
        with self.assertRaises(IndexError):
            sandhi_handler('', 'word')
        with self.assertRaises(IndexError):
            sandhi_handler('word', '')

if __name__ == '__main__':
    unittest.main()
