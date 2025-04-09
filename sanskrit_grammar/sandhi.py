import re

# Sandhi patterns for vowel and consonant combinations
VOWEL_SANDHI = {
    'अ': {'अ': 'आ', 'इ': 'ई', 'उ': 'ऊ', 'ए': 'ऐ', 'ओ': 'औ', 'अं': 'ं'},
    'आ': {'अ': 'आ', 'इ': 'ई', 'उ': 'ऊ', 'ए': 'ऐ', 'ओ': 'औ', 'अं': 'ं'},
    'इ': {'अ': 'ई', 'इ': 'ई', 'उ': 'ऊ', 'ए': 'ऐ', 'ओ': 'औ', 'अं': 'ं'},
    'ई': {'अ': 'ई', 'इ': 'ई', 'उ': 'ऊ', 'ए': 'ऐ', 'ओ': 'औ', 'अं': 'ं'},
    'उ': {'अ': 'ऊ', 'इ': 'ई', 'उ': 'ऊ', 'ए': 'ऐ', 'ओ': 'औ', 'अं': 'ं'},
    'ऊ': {'अ': 'ऊ', 'इ': 'ई', 'उ': 'ऊ', 'ए': 'ऐ', 'ओ': 'औ', 'अं': 'ं'},
    'ए': {'अ': 'ऐ', 'इ': 'ई', 'उ': 'ऊ', 'ए': 'ऐ', 'ओ': 'औ', 'अं': 'ं'},
    'ऐ': {'अ': 'ऐ', 'इ': 'ई', 'उ': 'ऊ', 'ए': 'ऐ', 'ओ': 'औ', 'अं': 'ं'},
    'ओ': {'अ': 'औ', 'इ': 'ई', 'उ': 'ऊ', 'ए': 'ऐ', 'ओ': 'औ', 'अं': 'ं'},
    'औ': {'अ': 'औ', 'इ': 'ई', 'उ': 'ऊ', 'ए': 'ऐ', 'ओ': 'औ', 'अं': 'ं'}
}

# Sandhi pattern for consonants (simplified)
CONSONANT_SANDHI = {
    'क': {'क': 'क', 'ग': 'ग', 'घ': 'घ'},
    'ग': {'क': 'ग', 'ग': 'ग', 'घ': 'घ'},
    'च': {'च': 'च', 'ज': 'ज', 'झ': 'झ'},
    'ज': {'च': 'ज', 'ज': 'ज', 'झ': 'झ'},
    'ट': {'ट': 'ट', 'ठ': 'ठ', 'ड': 'ड'},
    'ड': {'ट': 'ड', 'ड': 'ड', 'ढ': 'ढ'}
}

# Function to handle Sandhi based on vowel combinations
def apply_vowel_sandhi(word1, word2):
    """
    Apply vowel Sandhi rules for combining two words.
    """
    if word1[-1] in VOWEL_SANDHI and word2[0] in VOWEL_SANDHI[word1[-1]]:
        return word1[:-1] + VOWEL_SANDHI[word1[-1]].get(word2[0], word2[0]) + word2[1:]
    return word1 + word2

# Function to handle consonant Sandhi
def apply_consonant_sandhi(word1, word2):
    """
    Apply consonant Sandhi rules for combining two words.
    """
    if word1[-1] in CONSONANT_SANDHI and word2[0] in CONSONANT_SANDHI[word1[-1]]:
        return word1[:-1] + CONSONANT_SANDHI[word1[-1]].get(word2[0], word2[0]) + word2[1:]
    return word1 + word2

# Example Sandhi Handling
def sandhi_handler(word1, word2):
    """
    Handle Sandhi for given words.
    """
    # Check if the Sandhi is between two vowels or consonants
    if word1[-1] in VOWEL_SANDHI and word2[0] in VOWEL_SANDHI[word1[-1]]:
        return apply_vowel_sandhi(word1, word2)
    elif word1[-1] in CONSONANT_SANDHI and word2[0] in CONSONANT_SANDHI[word1[-1]]:
        return apply_consonant_sandhi(word1, word2)
    else:
        return word1 + word2

# Test cases for Sandhi
word1 = 'राम'
word2 = 'इति'
result = sandhi_handler(word1, word2)
print(f"Sandhi of {word1} + {word2}: {result}")

word3 = 'गच्छ'
word4 = 'सि'
result2 = sandhi_handler(word3, word4)
print(f"Sandhi of {word3} + {word4}: {result2}")
