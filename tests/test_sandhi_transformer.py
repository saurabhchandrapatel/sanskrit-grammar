import unittest
import sys
import os

# Add the parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sanskrit_grammar.upasarga_pratyaya import SandhiTransformer

class TestSandhiTransformer(unittest.TestCase):
    def test_vowel_sandhi(self):
        """Test vowel combination rules."""
        test_cases = [
            ("अ", "इ", "ए"),
            ("अ", "उ", "ओ"),
            ("इ", "अ", "या"),
            ("उ", "अ", "वा"),
            ("क", "ख", None)  # Non-vowel combination
        ]
        
        for first_vowel, second_vowel, expected in test_cases:
            result = SandhiTransformer.apply_vowel_sandhi(first_vowel, second_vowel)
            self.assertEqual(result, expected, 
                f"Failed for {first_vowel} + {second_vowel}")

    def test_consonant_sandhi_nasalization(self):
        """Test nasalization Sandhi rules."""
        test_cases = [
            # Prefix ending with म्
            ("सम्", "कृ", "सङ्कृ"),   # Before ka_varga
            ("सम्", "चल", "सञ्चल"),  # Before ca_varga
            ("सम्", "टीका", "सण्टीका"),  # Before ta_varga
            ("सम्", "पाठ", "सम्पाठ")   # Before pa_varga
        ]
        
        for prefix, word, expected in test_cases:
            result = SandhiTransformer.apply_consonant_sandhi(prefix, word)
            self.assertEqual(result, expected, 
                f"Failed for prefix={prefix}, word={word}")

    def test_visarga_sandhi(self):
        """Test visarga Sandhi transformation rules."""
        test_cases = [
            ("अतः", "कथा", "अतःकथा"),
            ("गतः", "पथ", "गतःपथ"),
            ("एतः", "चर्या", "एतःचर्या")
        ]
        
        for prefix, word, expected in test_cases:
            result = SandhiTransformer.apply_consonant_sandhi(prefix, word)
            self.assertEqual(result, expected, 
                f"Failed for prefix={prefix}, word={word}")

    def test_word_structure_analysis(self):
        """Test comprehensive word structure analysis."""
        test_cases = [
            ("गच्छति", {
                "original_word": "गच्छति",
                "vowels": ["अ", "इ"],
                "consonants": ["ग", "च", "छ", "त"],
                "potential_roots": []
            }),
            ("राम", {
                "original_word": "राम",
                "vowels": ["आ"],
                "consonants": ["र", "म"],
                "potential_roots": []
            })
        ]
        
        for word, expected in test_cases:
            result = SandhiTransformer.analyze_word_structure(word)
            
            # Compare specific keys
            for key in expected.keys():
                self.assertEqual(result[key], expected[key], 
                    f"Failed for {key} in word {word}")

    def test_consonant_groups(self):
        """Verify consonant group classifications."""
        # Verify presence of key consonant groups
        expected_groups = {
            "sparsha": ["ka_varga", "ca_varga", "ta_varga", "pa_varga"],
            "antastha": ["य", "र", "ल", "व"],
            "ushman": ["श", "ष", "स"],
            "jihvamuliya": ["ह"]
        }
        
        for group, subgroups in expected_groups.items():
            if group == "sparsha":
                # Check sparsha subgroups
                for subgroup in subgroups:
                    self.assertIn(subgroup, SandhiTransformer.CONSONANT_GROUPS[group])
            else:
                # Check direct consonant lists
                self.assertEqual(
                    set(SandhiTransformer.CONSONANT_GROUPS[group]), 
                    set(subgroups)
                )

if __name__ == '__main__':
    unittest.main()
