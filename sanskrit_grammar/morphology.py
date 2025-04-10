from .sandhi import sandhi_handler

def apply_guna(vowel: str) -> str:
    """Apply guna strengthening to vowels."""
    guna_map = {
        'इ': 'ए', 'ई': 'ए',
        'उ': 'ओ', 'ऊ': 'ओ',
        'ऋ': 'अर्', 'ॠ': 'अर्',
        'ृ': 'र', 'ॄ': 'र'
    }
    return guna_map.get(vowel, vowel)

def apply_vrddhi(vowel: str) -> str:
    """Apply vrddhi strengthening to vowels."""
    vrddhi_map = {
        'अ': 'आ',
        'इ': 'ऐ', 'ई': 'ऐ',
        'उ': 'औ', 'ऊ': 'औ',
        'ऋ': 'आर्', 'ॠ': 'आर्',
        'ृ': 'ार्', 'ॄ': 'ार्'
    }
    return vrddhi_map.get(vowel, vowel)

def apply_stem_sandhi(stem: str, suffix: str) -> str:
    """
    Apply sandhi rules between stem and suffix.
    """
    if not suffix:
        return stem
        
    # Special handling for verb endings starting with vowels
    if suffix and suffix[0] in 'अआइईउऊऋॠएऐओऔ':
        if stem.endswith('व्'):
            return stem[:-2] + 'व' + suffix
        elif stem.endswith('य्'):
            return stem[:-2] + 'य' + suffix
            
    return sandhi_handler(stem, suffix)

def generate_noun_forms(noun: str, gender: str):
    """
    Generate all declensions of a noun based on its gender.
    
    Args:
        noun (str): The base noun form (प्रातिपदिक)
        gender (str): Gender of the noun ('m' for masculine, 'f' for feminine, 'n' for neuter)
    
    Returns:
        dict: A dictionary containing all declension forms organized by case and number
    """
    # Sanskrit cases (विभक्ति)
    cases = {
        1: "प्रथमा",  # Nominative
        2: "द्वितीया",  # Accusative
        3: "तृतीया",  # Instrumental
        4: "चतुर्थी",  # Dative
        5: "पञ्चमी",  # Ablative
        6: "षष्ठी",  # Genitive
        7: "सप्तमी",  # Locative
        8: "सम्बोधन"  # Vocative
    }
    
    # Numbers (वचन)
    numbers = ["एकवचन", "द्विवचन", "बहुवचन"]
    
    # Suffix mappings based on gender and case
    suffixes = {
        'm': {  # Masculine endings (अकारान्त पुंल्लिङ्ग)
            1: ['ः', 'ौ', 'ाः'],
            2: ['म्', 'ौ', 'ान्'],
            3: ['ेन', 'ाभ्याम्', 'ैः'],
            4: ['ाय', 'ाभ्याम्', 'ेभ्यः'],
            5: ['ात्', 'ाभ्याम्', 'ेभ्यः'],
            6: ['स्य', 'योः', 'ानाम्'],
            7: ['े', 'योः', 'ेषु'],
            8: ['', 'ौ', 'ाः']
        },
        'f': {  # Feminine endings (आकारान्त स्त्रीलिङ्ग)
            1: ['ा', 'े', 'ाः'],
            2: ['ाम्', 'े', 'ाः'],
            3: ['या', 'ाभ्याम्', 'ाभिः'],
            4: ['ायै', 'ाभ्याम्', 'ाभ्यः'],
            5: ['ायाः', 'ाभ्याम्', 'ाभ्यः'],
            6: ['ायाः', 'योः', 'ानाम्'],
            7: ['ायाम्', 'योः', 'ासु'],
            8: ['े', 'े', 'ाः']
        },
        'n': {  # Neuter endings (अकारान्त नपुंसकलिङ्ग)
            1: ['म्', 'े', 'ानि'],
            2: ['म्', 'े', 'ानि'],
            3: ['ेन', 'ाभ्याम्', 'ैः'],
            4: ['ाय', 'ाभ्याम्', 'ेभ्यः'],
            5: ['ात्', 'ाभ्याम्', 'ेभ्यः'],
            6: ['स्य', 'योः', 'ानाम्'],
            7: ['े', 'योः', 'ेषु'],
            8: ['', 'े', 'ानि']
        }
    }
    
    # Initialize result dictionary
    declensions = {}
    
    # Generate forms for each case and number
    for case in cases:
        declensions[cases[case]] = {}
        for i, number in enumerate(numbers):
            # Handle stem modifications based on gender and case
            stem = noun
            if gender in suffixes and case in suffixes[gender]:
                suffix = suffixes[gender][case][i]
                # Apply sandhi rules between stem and suffix
                declensions[cases[case]][number] = apply_stem_sandhi(stem, suffix)
    
    return declensions

def modify_verb_stem(dhatu: str, lakara: str) -> str:
    """
    Apply verb stem modifications based on tense/mood.
    """
    # Basic verb stem modifications
    if lakara == 'lat':  # Present tense
        # For roots ending in vowels, apply guna
        if dhatu[-1] in 'िीुऊृॄ':
            if dhatu[-1] in 'िी':
                return dhatu[:-1] + 'य्'  # Add 'य्' after guna for i/ī
            elif dhatu[-1] in 'ुऊ':
                return dhatu[:-1] + 'व्'  # Add 'व्' after guna for u/ū
            else:
                return dhatu[:-1] + apply_guna(dhatu[-1])
    return dhatu

def generate_verb_forms(dhatu: str, pada: str, lakara: str):
    """
    Generate all conjugated forms of a verb root (धातु) for given लकार.
    
    Args:
        dhatu (str): The verb root (धातु)
        pada (str): Voice of the verb ('p' for परस्मैपद, 'a' for आत्मनेपद)
        lakara (str): Tense/Mood ('lat' for लट्, 'lot' for लोट्, etc.)
    
    Returns:
        dict: A dictionary containing all conjugated forms organized by person and number
    """
    # Persons (पुरुष)
    persons = {
        1: "प्रथम",  # Third person
        2: "मध्यम",  # Second person
        3: "उत्तम"   # First person
    }
    
    # Numbers (वचन)
    numbers = ["एकवचन", "द्विवचन", "बहुवचन"]
    
    # Verb endings based on pada and lakara
    endings = {
        'p': {  # परस्मैपद endings
            'lat': {  # Present tense
                1: ['ति', 'तः', 'न्ति'],
                2: ['सि', 'थः', 'थ'],
                3: ['मि', 'वः', 'मः']
            },
            'lot': {  # Imperative
                1: ['तु', 'ताम्', 'न्तु'],
                2: ['हि', 'तम्', 'त'],
                3: ['आनि', 'आव', 'आम']
            }
        },
        'a': {  # आत्मनेपद endings
            'lat': {
                1: ['ते', 'ेते', 'न्ते'],
                2: ['से', 'ेथे', 'ध्वे'],
                3: ['े', 'वहे', 'महे']
            },
            'lot': {
                1: ['ताम्', 'ेताम्', 'न्ताम्'],
                2: ['स्व', 'एथाम्', 'ध्वम्'],
                3: ['ै', 'आवहै', 'आमहै']
            }
        }
    }
    
    # Initialize result dictionary
    conjugations = {}
    
    # Generate forms for each person and number
    for person in persons:
        conjugations[persons[person]] = {}
        for i, number in enumerate(numbers):
            # Get the appropriate ending
            if pada in endings and lakara in endings[pada] and person in endings[pada][lakara]:
                ending = endings[pada][lakara][person][i]
                # Apply verb stem modifications based on tense and other rules
                stem = modify_verb_stem(dhatu, lakara)
                # Apply sandhi rules between stem and ending
                conjugations[persons[person]][number] = apply_stem_sandhi(stem, ending)
    
    return conjugations
