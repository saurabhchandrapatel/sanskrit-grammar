
# Example Usage
root_word = "धार (dhāra)"  # Example root meaning 'to hold'
upasarga = "प्र"  # Prefix meaning 'forward' or 'intensification'
pratyaya = "-त्र"  # Suffix meaning 'instrument or agent'

# Generate word using upasarga and pratyaya
generated_word = generate_word_with_upasarga_and_pratyaya(root_word, upasarga, pratyaya)
print("Generated Word:", generated_word)


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

# Example usage
image_path = 'path_to_image_with_text.png'  # Replace with the actual image path
reaction = ocr_text_reaction(image_path)
print(reaction)


# ✅ Example Usage
print(generate_sanskrit_word("गच्छ", "लट्", "प्रथम", "एकवचन", "परस्मैपद"))  # गच्छति
print(generate_sanskrit_word("पठ", "लङ्", "मध्यम", "बहुवचन", "परस्मैपद"))  # पठत
print(generate_sanskrit_word("गम्", "लृट्", "उत्तम", "एकवचन", "आत्मनेपद"))  # गच्छे

# ✅ Example Usage
root = "गच्छ"  # √गम् root verb
pada_type = "परस्मैपद"  # Active voice

full_conjugations = conjugate_verb_all_lakaras(root, pada_type)
for lakara, conjugation in full_conjugations.items():
    print(f"\n*** {lakara} लकारः ***")
    for person, forms in conjugation.items():
        print(f"{person}: {forms}")

# ✅ Example Usage
root = "गच्छ"  # √गम् root verb
tense = "लट्"  # Present tense
pada_type = "परस्मैपद"  # Active voice

conjugation = conjugate_verb(root, tense, pada_type)
for person, forms in conjugation.items():
    print(f"{person}: {forms}")

"""
प्रथमपुरुषः (Third Person): ['गच्छति', 'गच्छतः', 'गच्छन्ति']
मध्यमपुरुषः (Second Person): ['गच्छसि', 'गच्छथः', 'गच्छथ']
उत्तमपुरुषः (First Person): ['गच्छामि', 'गच्छावः', 'गच्छामः']

"""

# ✅ Example Test Cases
words = ["गच्छति", "गच्छते", "अगच्छत्", "अगच्छन्ते", "गमिष्यति", "गमिष्यते",
         "गच्छतु", "गच्छताम्", "गच्छेत्", "गच्छेते", "भूयात्", "भूयाथ", 
         "अगच्छम्", "अगच्छे", "लभते", "लभति", "निन्दति", "निन्दते", "याचते"]

for word in words:
    print(detect_tense_and_pada(word))

# ✅ Example Test Cases
words = ["पठति", "अगच्छत्", "गमिष्यति", "अकरोत्", "करिष्यामि", "गच्छतु", "पठेत्", "भूयात्", "अगच्छम्"]

for word in words:
    print(detect_tense(word))



# ✅ Example with धातु "पठ्" (read/study)
dhatu = "पठ"  # Root verb
conjugated_forms = conjugate_dhatu(dhatu)

# ✅ Display Results
for person, forms in conjugated_forms.items():
    print(f"{person}: {forms}")

# ✅ **Examples**
#print("🔹 Pratyahara Example:")
#print(get_pratyahara("अ", "ण्"))  # अ इ उ

print("\n🔹 Sandhi Examples:")
#print(apply_sandhi("राम", "इति"))  # रामेति
print(apply_sandhi("गुरु", "उपदेशः"))  # गुरूपदेशः

print("\n🔹 Sandhi Viched Examples:")
#print(sandhi_viched("रामेति"))  # ('राम', 'इ')
print(sandhi_viched("गुरूपदेशः"))  # ('गुरु', 'उ')

