class PaniniSutras:
    def __init__(self):
        """
        Initialize the PaniniSutras class with predefined sets of rules.
        For simplicity, we'll demonstrate a few Sutras for noun declensions.
        """
        self.sutras = {
            "nakara_svara": self.nakara_svara,  # Example of nakara (नकार) rule for transformation
            "vowel_to_vowel_rule": self.vowel_to_vowel_rule,  # Example of vowel change rule
        }

    def apply_sutra(self, rule: str, word: str):
        """
        Apply a specific Paninian sutra on the given word.
        :param rule: The rule identifier (such as 'nakara_svara')
        :param word: The word on which the rule should be applied
        :return: The transformed word after applying the rule
        """
        if rule in self.sutras:
            return self.sutras[rule](word)
        else:
            print(f"Error: Rule '{rule}' not found.")
            return word

    def nakara_svara(self, word):
        """
        This rule deals with the transformation of certain consonants like 'n' into their appropriate vowel sounds.
        For demonstration purposes, let's apply a simple transformation.
        Example: "न" to "नं" (like "नकार" becoming "नं").
        """
        if word.endswith("न"):
            return word[:-1] + "ं"
        return word

    def vowel_to_vowel_rule(self, word):
        """
        This rule demonstrates a simple vowel transformation (like an 'a' changing to 'i' in some cases).
        Example: "राज" becomes "राजी" in the nominative singular.
        """
        if word.endswith("ा"):
            return word[:-1] + "ी"
        return word

    def apply_declension(self, word):
        """
        Simulate the application of declensions to a word.
        Example: The word might change based on gender, number, or case.
        """
        # Apply some basic rules based on gender or number
        if word.endswith("ा"):
            return word + "ं"  # Example of singular to plural transformation
        elif word.endswith("ी"):
            return word + "ं"
        return word

