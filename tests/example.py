from sanskrit_grammar import generate_word_with_upasarga_and_pratyaya

# Example Usage
root_word = "धार (dhāra)"  # Example root meaning 'to hold'
upasarga = "प्र"  # Prefix meaning 'forward' or 'intensification'
pratyaya = "-त्र"  # Suffix meaning 'instrument or agent'

# Generate word using upasarga and pratyaya
generated_word = generate_word_with_upasarga_and_pratyaya(root_word, upasarga, pratyaya)
print("Generated Word:", generated_word)


from sanskrit_grammar import generate_samasa

# Examples of using the function
print(generate_samasa("rāma", "kṛṣhṇa", "Dvandva"))  # Example for Dvandva
# हिंदी में: इस उदाहरण में 'राम' और 'कृष्ण' शब्दों का समास होगा जो एक ड्वंद्व समास है।
print(generate_samasa("rāja", "puruṣa", "Tatpurusha"))  # Example for Tatpurusha
# हिंदी में: इस उदाहरण में 'राजा' और '

# Examples of using the function
print(generate_samasa("rāma", "kṛṣhṇa", "Dvandva"))  # Example for Dvandva
print(generate_samasa("rāja", "puruṣa", "Tatpurusha"))  # Example for Tatpurusha
print(generate_samasa("catur", "bhuj", "Karmadhāraya"))  # Example for Karmadhāraya
print(generate_samasa("catur", "bhuj", "Bahuvrīhi"))  # Example for Bahuvrīhi


from sanskrit_grammar import ocr_text_reaction

# Example usage
image_path = 'path_to_image_with_text.png'  # Replace with the actual image path
reaction = ocr_text_reaction(image_path)
print(reaction)


from sanskrit_grammar import generate_sanskrit_word

# Example Usage
print(generate_sanskrit_word("गच्छ", "लट्", "प्रथम", "एकवचन", "परस्मैपद"))  # गच्छति
print(generate_sanskrit_word("पठ", "लङ्", "मध्यम", "बहुवचन", "परस्मैपद"))  # पठत
print(generate_sanskrit_word("गम्", "लृट्", "उत्तम", "एकवचन", "आत्मनेपद"))  # गच्छे

from sanskrit_grammar import conjugate_verb_all_lakaras

# Example Usage
root = "गच्छ"  # √गम् root verb
pada_type = "परस्मैपद"  # Active voice

full_conjugations = conjugate_verb_all_lakaras(root, pada_type)
for lakara, conjugation in full_conjugations.items():
    print(f"\n*** {lakara} लकारः ***")
    for person, forms in conjugation.items():
        print(f"{person}: {forms}")


from sanskrit_grammar import conjugate_verb

# Example Usage
root = "गच्छ"  # √गम् root verb
tense = "लट्"  # Present tense
pada_type = "परस्मैपद"  # Active voice

conjugation = conjugate_verb(root, tense, pada_type)
for person, forms in conjugation.items():
    print(f"{person}: {forms}")



from sanskrit_grammar import detect_tense_and_pada
from sanskrit_grammar import detect_tense


"""
प्रथमपुरुषः (Third Person): ['गच्छति', 'गच्छतः', 'गच्छन्ति']
मध्यमपुरुषः (Second Person): ['गच्छसि', 'गच्छथः', 'गच्छथ']
उत्तमपुरुषः (First Person): ['गच्छामि', 'गच्छावः', 'गच्छामः']

"""


# Example Test Cases
words = ["गच्छति", "गच्छते", "अगच्छत्", "अगच्छन्ते", "गमिष्यति", "गमिष्यते",
         "गच्छतु", "गच्छताम्", "गच्छेत्", "गच्छेते", "भूयात्", "भूयाथ", 
         "अगच्छम्", "अगच्छे", "लभते", "लभति", "निन्दति", "निन्दते", "याचते"]

for word in words:
    print(detect_tense_and_pada(word))

# Example Test Cases
words = ["पठति", "अगच्छत्", "गमिष्यति", "अकरोत्", "करिष्यामि", "गच्छतु", "पठेत्", "भूयात्", "अगच्छम्"]

for word in words:
    print(detect_tense(word))


from sanskrit_grammar import conjugate_dhatu

# Example with धातु "पठ्" (read/study)
dhatu = "पठ"  # Root verb
conjugated_forms = conjugate_dhatu(dhatu)

# Display Results
for person, forms in conjugated_forms.items():
    print(f"{person}: {forms}")

from sanskrit_grammar import apply_sandhi
from sanskrit_grammar import sandhi_viched


# Examples
#print(" Pratyahara Example:")
#print(get_pratyahara("अ", "ण्"))  # अ इ उ

print("\n Sandhi Examples:")
#print(apply_sandhi("राम", "इति"))  # रामेति
print(apply_sandhi("गुरु", "उपदेशः"))  # गुरूपदेशः

print("\n Sandhi Viched Examples:")
#print(sandhi_viched("रामेति"))  # ('राम', 'इ')
print(sandhi_viched("गुरूपदेशः"))  # ('गुरु', 'उ')




from sanskrit_grammar.ashtadhyayi_simulator import PaniniSutras


"""
Example Functionality
Noun Declension (शब्दरूप): Generates declensions for all cases & numbers.

Verb Conjugation (धातुरूप): Conjugates verbs for all लकाराः (tenses/moods).

"""

# Example usage
panini = PaniniSutras()

# Applying sutra 'nakara_svara'
word = "राजन"  # Example word
new_word = panini.apply_sutra("nakara_svara", word)
print(f"After applying nakara_svara: {new_word}")

# Applying sutra 'vowel_to_vowel_rule'
word = "राज"  # Example word
new_word = panini.apply_sutra("vowel_to_vowel_rule", word)
print(f"After applying vowel_to_vowel_rule: {new_word}")

# Applying declension transformation
word = "राज"  # Example word
new_word = panini.apply_declension(word)
print(f"After applying declension: {new_word}")





from sanskrit_grammar.morphological_analyzer import analyze_sanskrit_word

"""
 Kr̥t Pratyayas (Primary suffixes) → Noun/Adjective formation

 Taddhita Pratyayas (Secondary suffixes) → Derived words from nouns

 Sarvanama Pratyayas (Pronouns) → Used in pronoun declension

 Vibhakti Pratyayas (Case suffixes) → Noun inflection

 Sandhi Pratyayas (Joining suffixes) → Used in compound formation

 Dhatu Pratyayas (Verb inflections) → Used in tense/mood conjugation
"""
# Example Usage
sanskrit_word = "प्रगच्छति"
sanskrit_word = "saurabh"
analysis_result = analyze_sanskrit_word(sanskrit_word)

print("Sanskrit Morphological Analysis:")
print(analysis_result)

from sanskrit_grammar.morphological_analyzer import identify_pratyaya

# Test Cases
print(identify_pratyaya("गमनीय"))  # Expected: "नीय"
print(identify_pratyaya("वक्तव्य"))  # Expected: "व्य"
print(identify_pratyaya("पुरुषत्व"))  # Expected: "त्व"



from sanskrit_grammar.NNExpression import segment_nn_expression
from sanskrit_grammar.NNExpression import parse_nn_expression


# Example usage
expression = "धर्मकर्मसिद्धान्ते किञ्च न"
segmented_expression, segments_found = segment_nn_expression(expression)
parsed_expression = parse_nn_expression(segmented_expression)
render_graph(parsed_expression)



from sanskrit_grammar import sandhi_handler

# Test cases for Sandhi
word1 = 'राम'
word2 = 'इति'
result = sandhi_handler(word1, word2)
print(f"Sandhi of {word1} + {word2}: {result}")

word3 = 'गच्छ'
word4 = 'सि'
result2 = sandhi_handler(word3, word4)
print(f"Sandhi of {word3} + {word4}: {result2}")


from sanskrit_grammar.sanskrit_hindi_accessor import add_word, initialize_database ,translate_sentence,dependency_resolution
 
initialize_database()

# Adding sample words to dictionary
add_word("रामः", "राम (एक व्यक्ति)")
add_word("गच्छति", "जाता है")
add_word("फलम्", "फल")
add_word("मित्रम्", "मित्र")

# Sample Sanskrit sentence analysis
sentence = "रामः गच्छति फलम्"
print(f" संस्कृत वाक्य: {sentence}")

# Word-by-word translation
print(f" हिंदी अनुवाद: {translate_sentence(sentence)}")

# Analyzing words and dependencies
words = sentence.split()
analysis_result = dependency_resolution(words)
for word, role in analysis_result.items():
    print(f" {word} → {role}")


from sanskrit_grammar.stem_generator import  generate_sanskrit_compound

# Example usage

# Define some sample data for the generator
# Analytical paraphrase format
sample_paraphrase = {
    "first_component": "राजन्",  # king
    "second_component": "पत्नी",  # queen
}
compound = generate_sanskrit_compound(sample_paraphrase)
print("Generated Sanskrit Compound:", compound)


# Test noun declension
from sanskrit_grammar.morphology import generate_noun_forms

print("\n=== Sanskrit Morphology Examples ===")

# Test noun declension
print("\n1. Noun Declension Examples:")

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

# Test verb conjugation
from sanskrit_grammar.morphology import generate_verb_forms

print("\n2. Verb Conjugation Examples:")

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

# Test verb conjugation system
print("\n2. Verb Conjugation Examples:")
from sanskrit_grammar.morphology import generate_verb_forms

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
