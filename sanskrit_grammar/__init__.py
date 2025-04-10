import re
import pytesseract
from PIL import Image

"""
Sanskrit grammar, or **Vyākaraṇa** (व्याकरण), is one of the six traditional Vedanga disciplines in Hinduism. It provides the rules for constructing words, sentences, and understanding their meanings. Here are some of the key concepts in Sanskrit grammar:

### 1. **Dhātu (धातु) – Root**
   - **Dhātu** refers to the root of a verb. These are the basic building blocks for word formation.
   - Sanskrit verbs are derived from Dhātus, and different forms of a verb can be created by adding suffixes and affixes.
   - For example: The root verb "gam" (गम्) means "to go."

### 2. **Samāsas (समास) – Compound Words**
   - **Samāsa** refers to the combination of two or more words to form a new compound word.
   - There are different types of compounds:
     - **Dvandva** (द्वंद्व) – Coordinative compounds, e.g., "rāma-krishna" (रामकृष्ण) meaning "Rama and Krishna."
     - **Tatpurusha** (तत्पुरुष) – Possessive compounds, e.g., "rājapuruṣa" (राजपुरुष) meaning "king's man."
     - **Karmadhāraya** (कर्मधारय) – Descriptive compounds, e.g., "satyāśraya" (सत्याश्रय) meaning "one who relies on truth."
     - **Bahuvrīhi** (बहुव्रीहि) – Explanatory compounds, e.g., "caturbhuj" (चतुर्भुज) meaning "one with four arms."

### 3. **Sandhi (संधि) – Euphonic Combination**
   - **Sandhi** refers to the rules for combining sounds at word boundaries.
   - **Vowel Sandhi**: When vowels meet at word boundaries, they combine into a new form. For example, "sūrya" (सूर्य) + "astu" (अस्तु) becomes "sūryastu" (सूर्यस्तु).
   - **Consonant Sandhi**: Changes that occur when consonants meet at word boundaries, such as "yog" (योग) + "kṣema" (क्षेम) becoming "yogakṣema" (योगक्षेम).

### 4. **Declension (Declension of Nouns)**
   - **Vibhakti** (विभक्ति) refers to the grammatical cases, or declension, that show the function of a noun in a sentence. There are **8 cases** in Sanskrit:
     1. **Nominative** (Prathama) – Subject
     2. **Accusative** (Dvitīya) – Object
     3. **Instrumental** (Tṛtīya) – Means or instrument
     4. **Dative** (Chaturthī) – Recipient or beneficiary
     5. **Ablative** (Pañcamī) – Separation or source
     6. **Genitive** (Sasṭhī) – Possession
     7. **Locative** (Saptamī) – Location or place
     8. **Vocative** (Sambodhana) – Address or calling

### 5. **Conjugation (Verbs)**
   - **Lākāra** (लकार) refers to the tense and mood of a verb. Sanskrit verbs have 10 primary tenses, and each verb is conjugated based on the tense, mood, person, and number.
     - **Present Tense**: Action happening now.
     - **Past Tense**: Action completed in the past.
     - **Future Tense**: Action that will happen.
     - Other moods like **Imperative** (command), **Optative** (wish), and **Conditional** (if-then scenarios).
   - Verbs are conjugated based on the **person** (first, second, third), **number** (singular, dual, plural), and **gender** (masculine, feminine, neuter).

### 6. **Upasargas (उपसर्ग) – Prefixes**
   - **Upasargas** are prefixes that modify the meaning of a verb. They can change the verb’s action to something more intense, reverse, or different.
   - Examples: "pra" (प्र) as in **pratiṣṭhā** (प्रतिष्ठा) meaning "to establish" or "ud" (उद्) as in **utthāpayati** (उत्थापयति) meaning "to lift."

### 7. **Pratyaya (प्रत्यय) – Suffixes**
   - **Pratyayas** are suffixes used to form various grammatical forms. These can change the root word into nouns, adjectives, or verbs.
   - For example:
     - **-i** (इ) is added to make adjectives, e.g., "sūrya" (सूर्य) becomes "sūryi" (सूर्यि) meaning "solar."
     - **-tva** (त्व) is used to form abstract nouns, e.g., "yoga" (योग) becomes "yogatva" (योगत्व) meaning "the state of being united."

### 8. **Karma (कर्म) – Object**
   - In Sanskrit grammar, the object of a verb (Karma) is identified by the case ending. For instance, if a verb takes an **accusative object**, the object will be in the accusative case.

### 9. **Taddhita (तद्धित) – Derivatives**
   - **Taddhita** is a class of words derived from nouns by the addition of specific suffixes. They can describe qualities, actions, or relationships. For example, from "rāja" (राजा) meaning "king," we can create "rājaputra" (राजपुत्र), meaning "prince."

### 10. **Samskrita Syntax (Word Order)**
   - Sanskrit word order is generally **Subject-Object-Verb (SOV)**. However, the word order can be flexible due to the inflection of nouns and verbs.
   - For example: "Rāmaḥ vanam gacchati" (रामः वनं गच्छति) meaning "Rama goes to the forest" can be rearranged as "Gacchati vanam Rāmaḥ" (गच्छति वनं रामः) without changing the meaning.

### 11. **Nekīnāṁ and Vākya**
   - **Vākya** (वाक्य) refers to the sentence. A sentence consists of at least one **verb** and a **subject**. Complex sentences can be formed using multiple clauses connected by conjunctions.

### 12. **Prakṛti and Vikṛti**
   - **Prakṛti** refers to the base form of a word, and **Vikṛti** refers to the modified forms of a word (e.g., in conjugation or declension).

### 13. **Samasas (Compounds)**
   - **Samasas** are compound words formed by combining multiple words, and understanding the various rules of combining these is crucial for fluency in Sanskrit grammar.

### 14. **Vibhakti (Case Declension)**
   - **Vibhakti** represents the cases of nouns, pronouns, and adjectives in Sanskrit, which define their syntactic roles in a sentence. For example:
     - **Prathama Vibhakti** (Nominative) – Subject
     - **Dvitīya Vibhakti** (Accusative) – Object
     - And so on for the 8 cases mentioned earlier.

### Conclusion:
Sanskrit grammar is systematic and precise, with a rich structure of roots, prefixes, suffixes, verb conjugation, case declension, and word formation. Understanding these rules is essential for reading, speaking, and analyzing Sanskrit texts correctly. Each rule helps in building accurate and meaningful sentences, and this depth of grammar makes Sanskrit an extraordinarily precise and flexible language.
"""
# ✅ Correct Maheshwara Sutras
maheshwara_sutras = [
    "अ इ उ ण्", "ऋ ऌ क्", "ए ओ ङ्", "ऐ औ च्",
    "ह य व र ट्", "ल ण्", "ञ म ङ ण न म्", "झ भ ञ्",
    "घ ढ ध ष्", "ज ब ग ड द श्", "ख फ छ ठ थ च ट त व्",
    "क प य्", "श ष स र्", "ह ल्"
]

# List of common Upasargāḥ (Prefixes)
upasargas = {
    "आ": "indicates approach or emphasis",
    "नि": "denotes negation or downward movement",
    "प्र": "indicates forward movement or intensification",
    "अधि": "denotes superiority or excess",
    "सम": "indicates together or completeness",
    "वि": "indicates separation or distinction",
    "उद": "indicates elevation or rising",
    "अप": "denotes away or opposition"
}

# List of common Pratyayāḥ (Suffixes)
pratyayas = {
    "-क": "forms adjectives indicating 'having'",
    "-त्व": "denotes the state or quality",
    "-इक": "indicates something related to or having the characteristic of",
    "-त्र": "denotes instruments or agent",
    "-त्वा": "denotes a state or quality",
    "-न": "denotes negation or absence"
}

def get_pratyahara(start, end):
    """
    Extracts the pratyahara (phonetic subset) from Maheshwara Sutras.
    
    :param start: The starting character.
    :param end: The ending marker character (must be a final consonant in a sutra).
    :return: The extracted phonetic subset.
    """
    pratyahara = ""
    found_start = False
    
    for sutra in maheshwara_sutras:
        for char in sutra.split():
            if char == start:
                found_start = True
            if found_start:
                pratyahara += char
            if char == end:
                return pratyahara
    return None  # If not found

def apply_sandhi(word1, word2):

    """
    Joins two words based on basic vowel Sandhi rules.
    
    """
    # ✅ Basic Sandhi Rules (Vowel-based)
    sandhi_rules = {
        ("अ", "अ"): "आ",
        ("अ", "इ"): "ए",
        ("अ", "उ"): "ओ",
        ("इ", "इ"): "ई",
        ("उ", "उ"): "ऊ",
        ("अ", "ए"): "ए",
        ("अ", "ओ"): "ओ",
        ("अ", "ऋ"): "अर",
    }

    if word1[-1] in "अइउ" and word2[0] in "अइउएओऋ":
        pair = (word1[-1], word2[0])
        if pair in sandhi_rules:
            return word1[:-1] + sandhi_rules[pair] + word2[1:]
    return word1 + word2

def sandhi_viched(word):
    """
    Attempts to split a given word into two words by reversing Sandhi.
    """
    # ✅ Basic Sandhi Rules (Vowel-based)
    sandhi_rules = {
        ("अ", "अ"): "आ",
        ("अ", "इ"): "ए",
        ("अ", "उ"): "ओ",
        ("इ", "इ"): "ई",
        ("उ", "उ"): "ऊ",
        ("अ", "ए"): "ए",
        ("अ", "ओ"): "ओ",
        ("अ", "ऋ"): "अर",
    }
    for (a, b), result in sandhi_rules.items():
        pattern = re.compile(f"({result})")
        match = pattern.search(word)
        if match:
            idx = match.start()
            return word[:idx] + a, b + word[idx + len(result):]
    return word, ""

# ✅ Basic Verb Conjugation for लट् लकार (Present Tense)

def conjugate_dhatu(dhatu):
    """
    Conjugates a given Sanskrit dhatu in present tense (लट् लकार).
    :param dhatu: Root verb (धातु)
    :return: Dictionary of conjugated forms
    """
    # Dhatu Endings for Parasmaipada verbs in लट् लकार
    parasmaipada_endings = {
        "प्रथम पुरुष" : ["ति", "तः", "न्ति"],  # 3rd Person: Singular, Dual, Plural
        "मध्यम पुरुष" : ["सि", "थः", "थ"],    # 2nd Person: Singular, Dual, Plural
        "उत्तम पुरुष" : ["मि", "वः", "मः"]   # 1st Person: Singular, Dual, Plural
    }

    forms = {}
    for person, endings in parasmaipada_endings.items():
        forms[person] = [dhatu + ending for ending in endings]
    return forms

def detect_tense(word):
    """
    Detects the tense (लकारः) of a Sanskrit verb based on its ending.
    
    :param word: Input verb form (e.g., पठति, अगच्छत्)
    :return: Tense name in Sanskrit
    """
    # Extended Tense patterns
    tense_patterns = {
        "लट् (Present Tense)": ["ति", "सि", "मि"],  # पठति, गच्छसि, करोमि
        "लङ् (Past Tense)": ["त्", "ः", "म्"],     # अगच्छत्, अपठः, अकरोत्
        "लृट् (Future Tense)": ["ष्यति", "ष्यसि", "ष्यामि"],  # गमिष्यति, पठिष्यसि, करिष्यामि
        "लोट् (Imperative)": ["तु", "ताम्", "न्तु"],  # पठतु, गच्छतु
        "विधिलिङ् (Potential)": ["एत्", "याम", "युः"],  # पठेत्, गच्छेत्
        "आशीर्लिङ् (Benediction)": ["यात्", "यु:"],  # भूयात्, जीवेत्
        "लुङ् (Aorist/Past Perfect)": ["अम्", "अः", "अरम्"],  # अगच्छम्, अभूव
    }

    for tense, endings in tense_patterns.items():
        if any(word.endswith(ending) for ending in endings):
            return f"The word '{word}' is in {tense}."
    
    return "Tense not identified."

def detect_tense_and_pada_v0(word):
    """
    Atmanepada & Parasmaipada Basics
    लकारः (Tense)	Parasmaipada (परस्मैपद)	Atmanepada (आत्मनेपद)
    लट् (Present)	गच्छति (He goes)	गच्छते (He goes - reflexive)
    लङ् (Past)	अगच्छत् (He went)	अगच्छत (He went - reflexive)
    लृट् (Future)	गमिष्यति (He will go)	गमिष्यते (He will go - reflexive)
    लोट् (Imperative)	गच्छतु (Let him go)	गच्छताम् (Let them go - reflexive)
    विधिलिङ् (Optative)	गच्छेत् (He should go)	गच्छेत (He should go - reflexive)
    लुङ् (Aorist/Past Perf.)	अगच्छम् (I went)	अगच्छे (I went - reflexive)
    💡 Atmanepada verbs generally end in:

    Present (लट्): ते, एते, अन्ते

    Past (लङ्): त, एते, अन्त

    Future (लृट्): ष्यते, ष्येते, ष्यन्ते

    Detects the tense (लकारः) and whether the verb is Parasmaipada (परस्मैपद) or Atmanepada (आत्मनेपद).
    
    :param word: Input verb form (e.g., गच्छति, गच्छते, अगच्छत्)
    :return: Tense name in Sanskrit and Pada type

    Ubhayapada verbs (उभयपदी धातवः) can be conjugated in both Parasmaipada (परस्मैपद) and Atmanepada (आत्मनेपद), depending on context and meaning.

    Examples of Ubhayapada Verbs
    Root (धातु)	Parasmaipada Usage	Atmanepada Usage
    निन्द् (to blame)	निन्दति (He blames)	निन्दते (He blames himself)
    याच् (to beg)	याचति (He asks)	याचते (He asks for himself)
    लभ् (to get)	लभति (He gets)	लभते (He receives for himself)
    स्पर्ध् (to compete)	स्पर्धते (He competes)	स्पर्धते (Reflexive: He competes for himself)

    """
    # Define tense patterns
    tense_patterns = {
        "लट् (Present Tense)": {
            "Parasmaipada": ["ति", "सि", "मि"],   # गच्छति, पठसि, करोमि
            "Atmanepada": ["ते", "एते", "अन्ते"]  # गच्छते, गच्छेते, गच्छन्ते
        },
        "लङ् (Past Tense)": {
            "Parasmaipada": ["त्", "ः", "म्"],    # अगच्छत्, अकरोत्, अपठम्
            "Atmanepada": ["त", "एते", "अन्त"]   # अगच्छत, अगच्छेते, अगच्छन्त
        },
        "लृट् (Future Tense)": {
            "Parasmaipada": ["ष्यति", "ष्यसि", "ष्यामि"],  # गमिष्यति, पठिष्यसि
            "Atmanepada": ["ष्यते", "ष्येते", "ष्यन्ते"]  # गमिष्यते, गमिष्येते, गमिष्यन्ते
        },
        "लोट् (Imperative)": {
            "Parasmaipada": ["तु", "ताम्", "न्तु"],  # पठतु, गच्छतु
            "Atmanepada": ["ताम्", "एताम्", "अन्ताम्"]  # गच्छताम्, गच्छेताम्, गच्छन्ताम्
        },
        "विधिलिङ् (Potential/Optative)": {
            "Parasmaipada": ["एत्", "याम", "युः"],  # पठेत्, गच्छेत्
            "Atmanepada": ["एत", "एते", "येरन्"]   # गच्छेत, गच्छेते, गच्छेरन्
        },
        "आशीर्लिङ् (Benediction)": {
            "Parasmaipada": ["यात्", "यु:"],  # भूयात्, जीवेत्
            "Atmanepada": ["याथ", "येयुः"]  # भूयाथ, जीवेयुः
        },
        "लुङ् (Aorist/Past Perfect)": {
            "Parasmaipada": ["अम्", "अः", "अरम्"],  # अगच्छम्, अभूव
            "Atmanepada": ["ए", "एते", "अन्त"]  # अगच्छे, अगच्छेते, अगच्छन्त
        }
    }

    for tense, pada_data in tense_patterns.items():
        for pada, endings in pada_data.items():
            if any(word.endswith(ending) for ending in endings):
                return f"The word '{word}' is in {tense} and follows {pada} (पद)."
    
    return "Tense and Pada not identified."

def detect_tense_and_pada(word):
    """
    Detects the tense (लकारः) and whether the verb is 
    Parasmaipada (परस्मैपद), Atmanepada (आत्मनेपद), or Ubhayapada (उभयपद).
    
    :param word: Input verb form (e.g., गच्छति, गच्छते, लभते)
    :return: Tense name in Sanskrit and Pada type
    """

    # List of known Ubhayapada roots
    ubhayapada_roots = ["निन्द्", "याच्", "लभ्", "स्पर्ध्", "मृष्"]

    # Define tense patterns
    tense_patterns = {
        "लट् (Present Tense)": {
            "Parasmaipada": ["ति", "सि", "मि"],   
            "Atmanepada": ["ते", "एते", "अन्ते"]  
        },
        "लङ् (Past Tense)": {
            "Parasmaipada": ["त्", "ः", "म्"],    
            "Atmanepada": ["त", "एते", "अन्त"]   
        },
        "लृट् (Future Tense)": {
            "Parasmaipada": ["ष्यति", "ष्यसि", "ष्यामि"],  
            "Atmanepada": ["ष्यते", "ष्येते", "ष्यन्ते"]  
        },
        "लोट् (Imperative)": {
            "Parasmaipada": ["तु", "ताम्", "न्तु"],  
            "Atmanepada": ["ताम्", "एताम्", "अन्ताम्"]  
        },
        "विधिलिङ् (Potential/Optative)": {
            "Parasmaipada": ["एत्", "याम", "युः"],  
            "Atmanepada": ["एत", "एते", "येरन्"]   
        },
        "आशीर्लिङ् (Benediction)": {
            "Parasmaipada": ["यात्", "यु:"],  
            "Atmanepada": ["याथ", "येयुः"]  
        },
        "लुङ् (Aorist/Past Perfect)": {
            "Parasmaipada": ["अम्", "अः", "अरम्"],  
            "Atmanepada": ["ए", "एते", "अन्त"]  
        }
    }

    pada_type = None
    tense_detected = None

    for tense, pada_data in tense_patterns.items():
        for pada, endings in pada_data.items():
            if any(word.endswith(ending) for ending in endings):
                tense_detected = tense
                pada_type = pada
                break

    if tense_detected and pada_type:
        # Check if the root of the word belongs to Ubhayapada roots
        root = word[:3]  # Extract first 3 letters (approximate root)
        if any(root in ubh_root for ubh_root in ubhayapada_roots):
            return f"The word '{word}' is in {tense_detected} and follows Ubhayapada (उभयपद)."
        return f"The word '{word}' is in {tense_detected} and follows {pada_type} (पद)."
    
    return "Tense and Pada not identified."

# Sanskrit Verb Conjugation Generator
def conjugate_verb(dhatu, lakara, pada):
    
    """
    Sanskrit verbs conjugate based on:
    ✅ धातु (Root) – e.g., √गम् (gam) → "to go"
    ✅ लकारः (Tense/Mood) – e.g., लट् (Present), लङ् (Past), लृट् (Future)
    ✅ पद (Pada) – परस्मैपद / आत्मनेपद / उभयपद
    ✅ पुरुष (Person) – उत्तम (First), मध्यम (Second), प्रमाण (Third)
    ✅ वचन (Number) – एकवचन (Singular), द्विवचन (Dual), बहुवचन (Plural)

    Example: गच्छ (√गम्) Conjugation in Present Tense (लट् लकार)
    पुरुषः	एकवचनम्	द्विवचनम्	बहुवचनम्
    प्रथमपुरुषः (Third Person)	गच्छति	गच्छतः	गच्छन्ति
    मध्यमपुरुषः (Second Person)	गच्छसि	गच्छथः	गच्छथ
    उत्तमपुरुषः (First Person)	गच्छामि	गच्छावः	गच्छामः

    Generates full conjugation for a given Sanskrit root (धातु), tense (लकारः), and pada (पदः).

    :param dhatu: Sanskrit root verb (e.g., 'गम्')
    :param lakara: Tense (लकारः) - e.g., 'लट्' (Present), 'लङ्' (Past), 'लृट्' (Future)
    :param pada: Pada type - 'परस्मैपद' or 'आत्मनेपद'
    :return: Conjugation table
    """

    # Verb endings based on Tense and Pada
    endings = {
        "लट्": {  # Present Tense
            "परस्मैपद": ["ति", "तः", "न्ति", "सि", "थः", "थ", "मि", "वः", "मः"],
            "आत्मनेपद": ["ते", "एते", "अन्ते", "से", "एथे", "ध्वे", "ए", "वहे", "महे"]
        },
        "लङ्": {  # Past Tense (Aorist)
            "परस्मैपद": ["त्", "तः", "न्", "ः", "थः", "त", "म्", "व", "म"],
            "आत्मनेपद": ["त", "एते", "अन्त", "थाः", "एथे", "ध्वे", "ए", "वहे", "महे"]
        },
        "लृट्": {  # Future Tense
            "परस्मैपद": ["ष्यति", "ष्यतः", "ष्यन्ति", "ष्यसि", "ष्यथः", "ष्यथ", "ष्यामि", "ष्यावः", "ष्यामः"],
            "आत्मनेपद": ["ष्यते", "ष्येते", "ष्यन्ते", "ष्यसे", "ष्येथे", "ष्यध्वे", "ष्ये", "ष्यावहे", "ष्यामहे"]
        },
        "लोट्": {  # Imperative
            "परस्मैपद": ["तु", "ताम्", "न्तु", "हि", "तम्", "त", "आनि", "आव", "आम"],
            "आत्मनेपद": ["ताम्", "एताम्", "अन्ताम्", "थाम्", "एतम्", "ध्वम्", "ऐ", "आवहि", "आमहै"]
        },
    }

    # Get correct endings
    if lakara not in endings or pada not in endings[lakara]:
        return "Invalid tense (लकारः) or pada (पदः)!"

    suffixes = endings[lakara][pada]

    # Form full conjugation table
    conjugated_forms = {
        "प्रथमपुरुषः (Third Person)": [dhatu + suffixes[0], dhatu + suffixes[1], dhatu + suffixes[2]],
        "मध्यमपुरुषः (Second Person)": [dhatu + suffixes[3], dhatu + suffixes[4], dhatu + suffixes[5]],
        "उत्तमपुरुषः (First Person)": [dhatu + suffixes[6], dhatu + suffixes[7], dhatu + suffixes[8]]
    }

    return conjugated_forms

# Sanskrit Verb Conjugation Generator for 10 Lakāras

def conjugate_verb_all_lakaras(dhatu, pada):
    """
    Generates full conjugations for a given Sanskrit root (धातु) across all 10 लकाराः.

    :param dhatu: Sanskrit root verb (e.g., 'गम्')
    :param pada: Pada type - 'परस्मैपद' or 'आत्मनेपद'
    :return: Dictionary of conjugations for each लकारः

    In Sanskrit, verbs (धातु) conjugate based on लकारः (tense/mood):

    लकारः (Tense/Mood)	English Equivalent	Example
    लट् (Present)	Simple Present	गच्छति (He goes)
    लङ् (Past)	Imperfect Past	अगच्छत् (He went)
    लृट् (Future)	Simple Future	गमिष्यति (He will go)
    लुट् (Periphrastic Future)	Definite Future	गन्ता (He is sure to go)
    लृङ् (Conditional)	Hypothetical	गमिष्यत् (He would go)
    लोट् (Imperative)	Command	गच्छतु (Let him go)
    विधिलिङ् (Optative)	Potential	गच्छेत् (He may go)
    आशिर्लिङ् (Benedictive)	Blessing/Wish	गच्छेयात् (May he go)
    विद्यालिङ् (Subjunctive)	Hypothetical	गच्छेत् (He might go)
    लुङ् (Aorist)	Simple Past	अगच्छत् (He went)

    """

    # Define endings for each लकारः (tense/mood)
    lakara_endings = {
        "लट्": {  # Present Tense
            "परस्मैपद": ["ति", "तः", "न्ति", "सि", "थः", "थ", "मि", "वः", "मः"],
            "आत्मनेपद": ["ते", "एते", "अन्ते", "से", "एथे", "ध्वे", "ए", "वहे", "महे"]
        },
        "लङ्": {  # Past (Imperfect)
            "परस्मैपद": ["त्", "तः", "न्", "ः", "थः", "त", "म्", "व", "म"],
            "आत्मनेपद": ["त", "एते", "अन्त", "थाः", "एथे", "ध्वे", "ए", "वहे", "महे"]
        },
        "लृट्": {  # Future Tense
            "परस्मैपद": ["ष्यति", "ष्यतः", "ष्यन्ति", "ष्यसि", "ष्यथः", "ष्यथ", "ष्यामि", "ष्यावः", "ष्यामः"],
            "आत्मनेपद": ["ष्यते", "ष्येते", "ष्यन्ते", "ष्यसे", "ष्येथे", "ष्यध्वे", "ष्ये", "ष्यावहे", "ष्यामहे"]
        },
        "लुट्": {  # Periphrastic Future
            "परस्मैपद": ["तारः", "तारौ", "तारः", "तास्यसि", "तास्यथः", "तास्यथ", "तास्यामि", "तास्यावः", "तास्यामः"]
        },
        "लृङ्": {  # Conditional
            "परस्मैपद": ["ष्यत्", "ष्यताम्", "ष्युः", "ष्याः", "ष्यथाम्", "ष्यत", "ष्याम्", "ष्याव", "ष्याम"]
        },
        "लोट्": {  # Imperative
            "परस्मैपद": ["तु", "ताम्", "न्तु", "हि", "तम्", "त", "आनि", "आव", "आम"],
            "आत्मनेपद": ["ताम्", "एताम्", "अन्ताम्", "थाम्", "एतम्", "ध्वम्", "ऐ", "आवहि", "आमहै"]
        },
        "विधिलिङ्": {  # Optative (Potential)
            "परस्मैपद": ["यात्", "याताम्", "युः", "याः", "याथाम्", "यात", "याम्", "याव", "याम"]
        },
        "आशिर्लिङ्": {  # Benedictive
            "परस्मैपद": ["एयात्", "एयाताम्", "एयुः", "एयाः", "एयाथाम्", "एयात", "एयाम्", "एयाव", "एयाम"]
        },
        "लुङ्": {  # Aorist (Simple Past)
            "परस्मैपद": ["त्", "तः", "न्", "ः", "थः", "त", "म्", "व", "म"]
        }
    }

    # Store conjugations
    all_conjugations = {}

    # Iterate over each लकारः
    for lakara, padas in lakara_endings.items():
        if pada in padas:
            suffixes = padas[pada]
            conjugated_forms = {
                "प्रथमपुरुषः (Third Person)": [dhatu + suffixes[0], dhatu + suffixes[1], dhatu + suffixes[2]],
                "मध्यमपुरुषः (Second Person)": [dhatu + suffixes[3], dhatu + suffixes[4], dhatu + suffixes[5]],
                "उत्तमपुरुषः (First Person)": [dhatu + suffixes[6], dhatu + suffixes[7], dhatu + suffixes[8]]
            }
            all_conjugations[lakara] = conjugated_forms

    return all_conjugations

# Verb conjugation generator with all 10 लकाराः
def generate_sanskrit_word(dhatu, lakara, purusha, vachana, pada):
    """
    Generates a Sanskrit word using a root (धातु), tense/mood (लकार), person (पुरुष),
    number (वचन), and voice (परस्मैपद/आत्मनेपद).
    Includes Sandhi rules for better word formation.
    Handles All 10 Tenses: Now, the function supports imperative (लृट्), past (लङ्), present (लट्), and can be extended to handle Future, Optative, and other tenses.
    Basic Sandhi Implementation: This function applies basic vowel and consonant fusion rules to generate a more accurate word.
    Supports All Person, Number, and Voice: Handles all grammatical forms such as 1st, 2nd, 3rd person, singular, dual, plural, and both parasmaipada (active) and ātmanepada (middle) forms.
    :param dhatu: Sanskrit root verb (e.g., 'गम्', 'पठ्')
    :param lakara: Tense/mood (e.g., 'लट्', 'लङ्', 'लृट्', etc.)
    :param purusha: Person ('प्रथम' (3rd), 'मध्यम' (2nd), 'उत्तम' (1st))
    :param vachana: Number ('एकवचन', 'द्विवचन', 'बहुवचन')
    :param pada: Pada type ('परस्मैपद' or 'आत्मनेपद')
    :return: Generated Sanskrit word with sandhi applied
    """
    
    # Define suffixes for all 10 लकाराः (Tenses/Moods)
    verb_suffixes = {
        "लट्": {  # Present tense
            "परस्मैपद": {
                "प्रथम": ["ति", "तः", "न्ति"], 
                "मध्यम": ["सि", "थः", "थ"], 
                "उत्तम": ["मि", "वः", "मः"]
            },
            "आत्मनेपद": {
                "प्रथम": ["ते", "एते", "अन्ते"], 
                "मध्यम": ["से", "एथे", "ध्वे"], 
                "उत्तम": ["ए", "वहे", "महे"]
            }
        },
        "लङ्": {  # Past tense
            "परस्मैपद": {
                "प्रथम": ["त्", "तः", "न्"], 
                "मध्यम": ["ः", "थः", "त"], 
                "उत्तम": ["म्", "व", "म"]
            },
            "आत्मनेपद": {
                "प्रथम": ["त", "एते", "अन्त"], 
                "मध्यम": ["थाः", "एथे", "ध्वे"], 
                "उत्तम": ["ए", "वहे", "महे"]
            }
        },
        "लृट्": {  # Imperative tense
            "परस्मैपद": {
                "प्रथम": ["तु", "त", "न्ति"],
                "मध्यम": ["हि", "थ", "तम"],
                "उत्तम": ["तु", "व", "म"]
            },
            "आत्मनेपद": {
                "प्रथम": ["ते", "त", "न्ते"],
                "मध्यम": ["त", "थे", "व"],
                "उत्तम": ["व", "वः", "व"]
            }
        },
        # Add more tenses (e.g., Future, Conditional, Optative, etc.)
        "लट्": {
            "परस्मैपद": {
                "प्रथम": ["ति", "तः", "न्ति"], 
                "मध्यम": ["सि", "थः", "थ"], 
                "उत्तम": ["मि", "वः", "मः"]
            },
            "आत्मनेपद": {
                "प्रथम": ["ते", "एते", "अन्ते"], 
                "मध्यम": ["से", "एथे", "ध्वे"], 
                "उत्तम": ["ए", "वहे", "महे"]
            }
        }
    }

    # Ensure valid input
    if lakara not in verb_suffixes or pada not in verb_suffixes[lakara]:
        return "❌ Invalid input: Check लकार or पद type"

    if purusha not in verb_suffixes[lakara][pada]:
        return "❌ Invalid input: Check पुरुष"

    if vachana not in ["एकवचन", "द्विवचन", "बहुवचन"]:
        return "❌ Invalid input: Check वचन"

    # Mapping वचन to index in suffix lists
    vachana_index = {"एकवचन": 0, "द्विवचन": 1, "बहुवचन": 2}

    # Generate word
    suffix = verb_suffixes[lakara][pada][purusha][vachana_index[vachana]]
    generated_word = dhatu + suffix
    
    # Apply Sandhi rules
    generated_word_with_sandhi = apply_sandhi(generated_word)

    return generated_word_with_sandhi

def ocr_text_reaction(image_path):
    """
    This function performs OCR on the image and returns the text extracted from it.
    It can react to the extracted text based on specific conditions or triggers.
    # You may need to specify the path to the tesseract executable if it's not in your PATH
    # Example: 'C:/Program Files/Tesseract-OCR/tesseract.exe' for Windows
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    Parameters:
    image_path (str): Path to the image file from which text is to be extracted.

    Returns:
    str: The extracted text from the image.
    """
    try:
        # Open the image using PIL
        img = Image.open(image_path)

        # Perform OCR using Tesseract
        extracted_text = pytesseract.image_to_string(img)

        # Reacting based on extracted text
        print(f"Extracted Text: {extracted_text}")

        # Example reaction: Check if certain keywords are found in the text
        if "hello" in extracted_text.lower():
            return "Hi! How can I assist you today?"
        elif "thank you" in extracted_text.lower():
            return "You're welcome!"
        else:
            return "Text extracted successfully!"

    except Exception as e:
        return f"Error processing the image: {str(e)}"

def generate_samasa(word1, word2, samasa_type):
    """
    This function generates a samasa (compound word) based on the type of Samasa.
    
    :param word1: The first word in the compound.
    :param word2: The second word in the compound.
    :param samasa_type: The type of samasa (Dvandva, Tatpurusha, Karmadhāraya, Bahuvrīhi).
    
    :return: The compound word (samasa).
    """
    
    samasa = ""
    
    # Dvandva Samasa: The compound word represents a co-ordination between two elements.
    # Example: रामकृष्ण (Rama and Krishna)
    if samasa_type == "Dvandva":
        samasa = word1 + word2  # Simply concatenate the words
        # ड्वंद्व समास - दो शब्दों का समन्वय दर्शाने वाला समास है। उदाहरण: रामकृष्ण (राम और कृष्ण)

    # Tatpurusha Samasa: The first word generally describes or possesses the second.
    # Example: राजपुरुष (King's man)
    elif samasa_type == "Tatpurusha":
        samasa = word1 + word2  # Simply concatenate the words for simplicity
        # तत्पुरुष समास - पहला शब्द दूसरे शब्द को गुण या स्वामित्व में दर्शाता है। उदाहरण: राजपुरुष (राजा का आदमी)

    # Karmadhāraya Samasa: The first word describes the second word.
    # Example: चतुर्भुज (one with four arms)
    elif samasa_type == "Karmadhāraya":
        samasa = word1 + word2  # Simple concatenation for illustration
        # कर्मधारय समास - पहला शब्द दूसरे शब्द का गुण बताता है। उदाहरण: चतुर्भुज (जिसके चार हाथ हैं)

    # Bahuvrīhi Samasa: The compound word explains or describes a person or thing by its trait.
    # Example: चतुर्भुज (one with four arms)
    elif samasa_type == "Bahuvrīhi":
        samasa = word1 + word2  # Simple concatenation for this example
        # बहुव्रीहि समास - इस समास में शब्द का अर्थ एक गुण या विशेषता से मिलता है। उदाहरण: चतुर्भुज (जिसके चार हाथ हैं)

    else:
        raise ValueError("Invalid Samasa Type")  # If the samasa type is not recognized
    
    return samasa

def apply_upasarga(root, upasarga):
    """Function to add Upasarga (prefix) to a root word."""
    if upasarga in upasargas:
        new_word = upasarga + root
        return new_word
    else:
        return f"Invalid Upasarga: {upasarga}"

def apply_pratyaya(root, pratyaya):
    """Function to add Pratyaya (suffix) to a root word."""
    if pratyaya in pratyayas:
        new_word = root + pratyaya
        return new_word
    else:
        return f"Invalid Pratyaya: {pratyaya}"

def generate_word_with_upasarga_and_pratyaya(root, upasarga, pratyaya):
    """Generate a word by applying both Upasarga and Pratyaya."""
    word_with_upasarga = apply_upasarga(root, upasarga)
    final_word = apply_pratyaya(word_with_upasarga, pratyaya)
    return final_word
