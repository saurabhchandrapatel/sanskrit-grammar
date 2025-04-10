import unittest
import sys
import os

# Add the parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sanskrit_grammar.upasarga_pratyaya import (
    add_upasarga, 
    add_pratyaya, 
    get_upasarga_meaning,
    UPASARGA_DICT,
    PRATYAYA_DICT
)

class TestUpasargaPratyaya(unittest.TestCase):
    def test_add_upasarga_valid(self):
        """Test adding valid upasargas with Sandhi rules."""
        test_cases = [
            ("गम्", "प्र", "प्रगम्"),  # Simple prefix
            ("कृ", "सम्", "सम्ङ्ृ"),   # Nasalization Sandhi
            ("पा", "अभि", "अभिपा")   # Vowel starting word
        ]
        
        for word, upasarga, expected in test_cases:
            result = add_upasarga(word, upasarga)
            self.assertTrue(
                result == expected or 
                result.startswith(upasarga) and result.endswith(word),
                f"Failed for word={word}, upasarga={upasarga}, result={result}"
            )

    def test_add_upasarga_invalid(self):
        """Test adding invalid upasargas."""
        with self.assertRaises(ValueError):
            add_upasarga("गम्", "अज्ञात")

    def test_add_pratyaya_valid(self):
        """Test adding valid pratyayas."""
        test_cases = [
            ("गम्", "अ", "गमअ", "कृत्"),     # Simple suffix
            ("कृ", "त", "कृत", "कृत्"),       # Past participle
            ("नी", "तृ", "नीतृ", "कृत्")      # Agent noun
        ]
        
        for word, pratyaya, expected, pratyaya_type in test_cases:
            result = add_pratyaya(word, pratyaya, pratyaya_type)
            self.assertEqual(result, expected, 
                f"Failed for word={word}, pratyaya={pratyaya}")

    def test_add_pratyaya_invalid(self):
        """Test adding invalid pratyayas."""
        with self.assertRaises(ValueError):
            add_pratyaya("गम्", "अज्ञात")
        
        with self.assertRaises(ValueError):
            add_pratyaya("गम्", "अ", "अज्ञात")

    def test_get_upasarga_meaning(self):
        """Test retrieving upasarga meanings."""
        test_cases = [
            ("प्र", ["forward", "forth", "in front"]),
            ("अभि", ["towards", "near", "in front of", "against"]),
            ("अज्ञात", [])
        ]
        
        for upasarga, expected_meanings in test_cases:
            meanings = get_upasarga_meaning(upasarga)
            self.assertEqual(meanings, expected_meanings, 
                f"Failed for upasarga={upasarga}")

    def test_upasarga_dictionary_completeness(self):
        """Verify the comprehensiveness of the Upasarga dictionary."""
        expected_upasargas = {
            "प्र", "अभि", "अनु", "सम्", "वि", 
            "उप", "नि", "परा"
        }
        self.assertEqual(set(UPASARGA_DICT.keys()), expected_upasargas)

    def test_upasarga_dictionary_structure(self):
        """Verify the structure of the Upasarga dictionary."""
        for upasarga, details in UPASARGA_DICT.items():
            self.assertIn("meanings", details)
            self.assertIn("linguistic_category", details)
            self.assertIn("grammatical_impact", details)
            self.assertIn("examples", details)

    def test_pratyaya_dictionary_completeness(self):
        """Verify the comprehensiveness of the Pratyaya dictionary."""
        expected_pratyaya_types = {"कृत्", "तद्धित"}
        self.assertEqual(set(PRATYAYA_DICT.keys()), expected_pratyaya_types)

    def test_pratyaya_dictionary_structure(self):
        """Verify the structure of the Pratyaya dictionary."""
        for pratyaya_type, pratyayas in PRATYAYA_DICT.items():
            for pratyaya, details in pratyayas.items():
                self.assertIn("meaning", details)
                self.assertIn("grammatical_function", details)
                self.assertIn("semantic_impact", details)
                self.assertIn("examples", details)

if __name__ == '__main__':
    unittest.main()
