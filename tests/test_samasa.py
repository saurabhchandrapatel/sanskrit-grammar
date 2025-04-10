from sanskrit_grammar.samasa import form_samasa

def test_avyayibhava():
    """Test अव्ययीभाव compounds with edge cases."""
    print("\n=== Testing अव्ययीभाव Compounds ===")
    
    # Standard cases
    test_cases = [
        ("यथा", "शक्ति", "according to ability"),
        ("उप", "कृष्ण", "near Krishna"),
        ("प्रति", "अग्नि", "towards the fire"),
        
        # Edge cases
        ("सम्", "अर्थ", "with meaning"),  # Prefix with संधि
        ("अधि", "देव", "over/about god"),  # Prefix with different vowel
        ("निर्", "अर्थक", "meaningless")  # Prefix with विसर्ग
    ]
    
    for first, second, description in test_cases:
        result = form_samasa(first, second, "avyayibhava")
        print(f"{first} + {second} = {result} # {description}")

def test_tatpurusa():
    """Test तत्पुरुष compounds with edge cases."""
    print("\n=== Testing तत्पुरुष Compounds ===")
    
    test_cases = [
        # Standard cases
        ("राजन्", "पुरुष", "king's man"),
        ("धर्म", "ज्ञ", "knower of dharma"),
        ("देव", "दत्त", "given by god"),
        
        # Edge cases
        ("गो", "पाल", "cow-herder"),  # Compound with different stems
        ("अन्न", "दाता", "food giver"),  # Longer compound
        ("शत", "पथ", "hundred paths")  # Numerical prefix
    ]
    
    for first, second, description in test_cases:
        result = form_samasa(first, second, "tatpurusa")
        print(f"{first} + {second} = {result} # {description}")

def test_karmadharaya():
    """Test कर्मधारय compounds with edge cases."""
    print("\n=== Testing कर्मधारय Compounds ===")
    
    test_cases = [
        # Standard cases
        ("नील", "उत्पल", "blue lotus"),
        ("महत्", "ऋषि", "great sage"),
        ("कृष्ण", "सर्प", "black snake"),
        
        # Edge cases
        ("महा", "राज", "great king"),  # Prefix variation
        ("सु", "कृत", "well-done"),  # Prefix with different meaning
        ("नव", "यौवन", "new youth")  # Descriptive compounds
    ]
    
    for first, second, description in test_cases:
        result = form_samasa(first, second, "karmadharaya")
        print(f"{first} + {second} = {result} # {description}")

def test_dvigu():
    """Test द्विगु compounds with edge cases."""
    print("\n=== Testing द्विगु Compounds ===")
    
    test_cases = [
        # Standard cases
        ("त्रि", "लोक", "three worlds"),
        ("पञ्च", "वट", "five banyan trees"),
        ("सप्त", "ऋषि", "seven sages"),
        
        # Edge cases
        ("चतुर्", "वेद", "four Vedas"),  # Numerical prefix with संधि
        ("षड्", "अङ्ग", "six limbs"),  # Numerical prefix with complex संधि
        ("दश", "दिक्", "ten directions")  # Numerical compound
    ]
    
    for first, second, description in test_cases:
        result = form_samasa(first, second, "dvigu")
        print(f"{first} + {second} = {result} # {description}")

def test_dvandva():
    """Test द्वन्द्व compounds with edge cases."""
    print("\n=== Testing द्वन्द्व Compounds ===")
    
    test_cases = [
        # Standard cases
        ("राम", "लक्ष्मण", "Rama and Lakshmana"),
        ("शिव", "पार्वती", "Shiva and Parvati"),
        ("दम्", "पती", "husband and wife"),
        
        # Edge cases
        ("नर", "नारी", "man and woman"),  # Gender variation
        ("सूर्य", "चन्द्र", "sun and moon"),  # Cosmic entities
        ("अग्नि", "वायु", "fire and wind")  # Natural elements
    ]
    
    for first, second, description in test_cases:
        result = form_samasa(first, second, "dvandva")
        print(f"{first} + {second} = {result} # {description}")

def test_bahuvrihi():
    """Test बहुव्रीहि compounds with edge cases."""
    print("\n=== Testing बहुव्रीहि Compounds ===")
    
    test_cases = [
        # Standard cases
        ("पीत", "अम्बर", "yellow-clothed"),
        ("चक्र", "पाणि", "wheel-handed"),
        ("नील", "कण्ठ", "blue-throated"),
        
        # Edge cases
        ("दीर्घ", "बाहु", "long-armed"),  # Descriptive possession
        ("शत", "पत्र", "hundred-leafed"),  # Numerical possession
        ("सु", "लोचन", "beautiful-eyed")  # Prefix variation
    ]
    
    for first, second, description in test_cases:
        result = form_samasa(first, second, "bahuvrihi")
        print(f"{first} + {second} = {result} # {description}")

if __name__ == "__main__":
    test_avyayibhava()
    test_tatpurusa()
    test_karmadharaya()
    test_dvigu()
    test_dvandva()
    test_bahuvrihi()
