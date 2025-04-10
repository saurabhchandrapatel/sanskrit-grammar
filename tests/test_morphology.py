from sanskrit_grammar.morphology import generate_noun_forms, generate_verb_forms

def test_noun_declension():
    """Test the noun declension system with different genders and endings."""
    print("\n=== Sanskrit Noun Declension Tests ===")

    # Test a-ending masculine noun (अकारान्त पुंल्लिङ्ग)
    print("\nराम (Masculine):")
    rama_forms = generate_noun_forms("राम", "m")
    for case, numbers in rama_forms.items():
        print(f"\n{case}:")
        for number, form in numbers.items():
            print(f"  {number}: {form}")

    # Test ā-ending feminine noun (आकारान्त स्त्रीलिङ्ग)
    print("\nलता (Feminine):")
    lata_forms = generate_noun_forms("लत", "f")
    for case, numbers in lata_forms.items():
        print(f"\n{case}:")
        for number, form in numbers.items():
            print(f"  {number}: {form}")

    # Test a-ending neuter noun (अकारान्त नपुंसकलिङ्ग)
    print("\nज्ञान (Neuter):")
    jnana_forms = generate_noun_forms("ज्ञान", "n")
    for case, numbers in jnana_forms.items():
        print(f"\n{case}:")
        for number, form in numbers.items():
            print(f"  {number}: {form}")

def test_verb_conjugation():
    """Test the verb conjugation system with different roots and moods."""
    print("\n=== Sanskrit Verb Conjugation Tests ===")

    # Test root with vowel ending
    print("\nभू (Present Tense, परस्मैपद):")
    bhu_forms = generate_verb_forms("भू", "p", "lat")
    for person, numbers in bhu_forms.items():
        print(f"\n{person}:")
        for number, form in numbers.items():
            print(f"  {number}: {form}")

    # Test root with consonant ending
    print("\nपठ् (Present Tense, परस्मैपद):")
    path_forms = generate_verb_forms("पठ", "p", "lat")
    for person, numbers in path_forms.items():
        print(f"\n{person}:")
        for number, form in numbers.items():
            print(f"  {number}: {form}")

    # Test ātmanepada verb
    print("\nसेव् (Present Tense, आत्मनेपद):")
    sev_forms = generate_verb_forms("सेव", "a", "lat")
    for person, numbers in sev_forms.items():
        print(f"\n{person}:")
        for number, form in numbers.items():
            print(f"  {number}: {form}")

    # Test imperative mood
    print("\nनी (Imperative, परस्मैपद):")
    ni_forms = generate_verb_forms("नी", "p", "lot")
    for person, numbers in ni_forms.items():
        print(f"\n{person}:")
        for number, form in numbers.items():
            print(f"  {number}: {form}")

if __name__ == "__main__":
    test_noun_declension()
    test_verb_conjugation()
