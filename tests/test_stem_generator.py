import unittest
from sanskrit_grammar.stem_generator import generate_sanskrit_compound

class TestStemGenerator(unittest.TestCase):
    def test_generate_compound(self):
        # Test basic compound generation
        paraphrase = {
            "first_component": "राज",
            "second_component": "पुरुष",
            "relation": "genitive",
            "gender": "masculine"
        }
        result = generate_sanskrit_compound(paraphrase)
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, str))
        
    def test_compound_with_case_gender(self):
        # Test compound generation with specific case and gender
        paraphrase = {
            "first_component": "देव",
            "second_component": "दत्त",
            "relation": "tatpurusha",
            "gender": "masculine"
        }
        result = generate_sanskrit_compound(paraphrase)
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, str))

    def test_invalid_inputs(self):
        # Test handling of invalid inputs
        with self.assertRaises(KeyError):
            generate_sanskrit_compound({})
        with self.assertRaises(KeyError):
            generate_sanskrit_compound({"first_component": "test"})

if __name__ == '__main__':
    unittest.main()
