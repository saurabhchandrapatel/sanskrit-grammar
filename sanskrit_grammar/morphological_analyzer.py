import re

# Sample dictionary of Sanskrit roots (धातु) with possible suffixes
SANSKRIT_DHATUS = {
    "गम्": ["ति", "तः", "न्ति", "सि", "थः", "थ", "मि", "वः", "मः"],  # Example conjugations for "गम्" (to go)
    "भू": ["ति", "तः", "न्ति"],  # Example conjugations for "भू" (to be)
    "कृ": ["ति", "तः", "न्ति"],  # Example conjugations for "कृ" (to do)
}

UPASARGA_LIST = [
    "प्र", "पर", "अप", "सम्", "अति", "अधि", "नि", "निर्", "दुर्", "दुस्",
    "अभि", "उद्", "उप", "अनु", "अव", "वि", "परि", "प्रति", "सु", "सुस्",
    "कु", "अङ्"
]

"""
कृत् प्रत्ययाः (Primary verbal suffixes) – Used for deriving nouns and adjectives from roots.

तद्धित प्रत्ययाः (Secondary suffixes) – Used to derive new words from existing nouns/adjectives.

सर्वनाम प्रत्ययाः (Pronominal suffixes) – Used for pronoun declension.

विभक्ति प्रत्ययाः (Case suffixes) – Used for noun inflection (like nominative, accusative, etc.).

संधि प्रत्ययाः (Joining suffixes) – Used in compound word formation.

धातु प्रत्ययाः (Verb inflections) – Used in tense and mood-based conjugation.

"""
# PRATYAYA_LIST = ["क", "क्त", "त", "त्व", "ता", "स्य", "अय"]  # Sample suffixes (प्रत्यय)
# KRIT_PRATYAYA_LIST
KRIT_PRATYAYA_LIST = [
    "क", "क्त", "क्त्वा", "अ", "अन", "अल", "ता", "त्व", "इ", "त्र", "इन",
    "अय", "न", "ली", "ल्य", "मन", "म", "श", "य", "व", "तृ", "इत्र", "इष्णु",
    "मात्र", "स्य", "मल", "न्य", "त्र", "शतृ", "शानच", "अव्यय", "इन्", "अस"
]

TADDHITA_PRATYAYA_LIST = [
    "इय", "क", "का", "त", "त्र", "त्व", "इ", "त्व", "य", "वत्", "मय", "शील",
    "धर्म", "ल", "ज", "जनि", "यन", "अच", "अण", "अय", "मातृ", "स", "इष्ठ",
    "अर्थ", "इष्णु", "इत्र", "सार", "लु"
]

SARVANAMA_PRATYAYA_LIST = [
    "अस्म", "त्व", "युष्म", "एत", "अत", "इदम्", "किम्", "य", "त", "स्म",
    "क", "द", "एष", "न"
]
VIBHAKTI_PRATYAYA_LIST = [
    "सुप्", "अम्", "आ", "अय", "स्म", "अस्", "स्य", "ओ", "ई", "इन", "त्र",
    "म", "इन्", "अस्म", "नि", "ति"
]
SANDHI_PRATYAYA_LIST = [
    "अ", "इ", "उ", "ऋ", "ए", "ओ", "औ", "अः", "म्", "न्", "स्"
]
DHATU_PRATYAYA_LIST = [
    "ति", "तः", "न्ति", "सि", "थः", "थ", "मि", "वः", "मः",  # Present (लट्)
    "ताम्", "ताताम्", "अन"  # Imperative (लोट्)
    "स्यति", "स्यतः", "स्यन्ति", "स्स्यसि", "स्यथः", "स्यथ",  # Future (लृट्)
    "अम्", "आः", "अत", "आम", "आताम्", "अन्",  # Past (लङ्, लिट्, लुट्)
]
PRATYAYA_LIST = KRIT_PRATYAYA_LIST + TADDHITA_PRATYAYA_LIST + SARVANAMA_PRATYAYA_LIST + VIBHAKTI_PRATYAYA_LIST + SANDHI_PRATYAYA_LIST + DHATU_PRATYAYA_LIST


def identify_pratyaya(word):
    """
    Identify the suffix (Pratyaya) in a given Sanskrit word.
    """
    for pratyaya in PRATYAYA_LIST:
        if word.endswith(pratyaya):
            return pratyaya
    return None

def analyze_sanskrit_word(word):
    """
    Sanskrit Morphological Analyzer: Identifies root, suffix, prefix
    and grammatical features of a given Sanskrit word.
    """
    root = None
    suffix = None
    prefix = None

    # Checking for Upasarga (Prefix)
    for upasarga in UPASARGA_LIST:
        if word.startswith(upasarga):
            prefix = upasarga
            word = word[len(upasarga):]  # Remove the prefix
            break  # Assuming single prefix

    # Checking for Dhatu (Root)
    for dhatu, suffixes in SANSKRIT_DHATUS.items():
        for suf in suffixes:
            if word.endswith(suf):
                root = dhatu
                suffix = suf
                break
        if root:
            break

    # Checking for Pratyaya (Suffix)
    additional_suffix = None
    for pratyaya in PRATYAYA_LIST:
        if word.endswith(pratyaya) and pratyaya != suffix:
            additional_suffix = pratyaya
            break

    return {
        "word": word,
        "root": root,
        "suffix": suffix,
        "prefix": prefix,
        "additional_suffix": additional_suffix
    }

