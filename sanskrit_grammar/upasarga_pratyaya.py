import re
from typing import List, Dict, Optional, Union, Tuple

# Comprehensive Upasarga (Prefix) Dictionary with Enhanced Linguistic Metadata
UPASARGA_DICT: Dict[str, Dict[str, Union[List[str], str, Dict[str, str]]]] = {
    "प्र": {
        "meanings": ["forward", "forth", "in front"],
        "linguistic_category": "directional",
        "grammatical_impact": {
            "verb_modification": "intensification",
            "semantic_shift": "proactive or initiatory sense"
        },
        "examples": ["प्रगच्छति (goes forward)", "प्रकाश (light, illumination)"]
    },
    "अभि": {
        "meanings": ["towards", "near", "in front of", "against"],
        "linguistic_category": "directional/confrontational",
        "grammatical_impact": {
            "verb_modification": "movement towards or confrontation",
            "semantic_shift": "intensive or confrontational sense"
        },
        "examples": ["अभिगच्छति (approaches)", "अभिमान (pride)"]
    },
    "अनु": {
        "meanings": ["after", "along", "following", "in accordance with"],
        "linguistic_category": "sequential/conformative",
        "grammatical_impact": {
            "verb_modification": "following or conforming",
            "semantic_shift": "sequential or compliant sense"
        },
        "examples": ["अनुगच्छति (follows)", "अनुष्ठान (performance)"]
    },
    "सम्": {
        "meanings": ["together", "completely", "with", "well"],
        "linguistic_category": "completive/collective",
        "grammatical_impact": {
            "verb_modification": "completeness or totality",
            "semantic_shift": "comprehensive or unified sense"
        },
        "examples": ["संकल्प (resolution)", "संग्राम (battle)"]
    },
    "वि": {
        "meanings": ["apart", "away", "without", "distinctly"],
        "linguistic_category": "separative/negative",
        "grammatical_impact": {
            "verb_modification": "separation or negation",
            "semantic_shift": "dispersive or contradictory sense"
        },
        "examples": ["विजय (victory)", "विभाग (division)"]
    },
    "उप": {
        "meanings": ["near", "towards", "secondary", "subordinate"],
        "linguistic_category": "proximity/subordination",
        "grammatical_impact": {
            "verb_modification": "nearness or subordination",
            "semantic_shift": "auxiliary or supportive sense"
        },
        "examples": ["उपाध्याय (sub-teacher)", "उपवास (fasting)"]
    },
    "नि": {
        "meanings": ["down", "into", "within", "certainly"],
        "linguistic_category": "directional/intensive",
        "grammatical_impact": {
            "verb_modification": "downward movement or internalization",
            "semantic_shift": "definitive or internal sense"
        },
        "examples": ["निवेश (settlement)", "निश्चय (certainty)"]
    },
    "परा": {
        "meanings": ["away", "backwards", "completely", "beyond"],
        "linguistic_category": "transformative/transcendent",
        "grammatical_impact": {
            "verb_modification": "complete transformation or transcendence",
            "semantic_shift": "ultimate or beyond current state"
        },
        "examples": ["पराजय (defeat)", "परामर्श (consultation)"]
    }
}

# Comprehensive Pratyaya (Suffix) Dictionary with Enhanced Linguistic Metadata
PRATYAYA_DICT: Dict[str, Dict[str, Dict[str, Union[str, List[str], Dict[str, str]]]]] = {
    "कृत्": {
        "अ": {
            "meaning": "noun/verbal noun",
            "grammatical_function": "nominalization",
            "semantic_impact": "converting verb to noun",
            "examples": ["गम्य (going)", "कार्य (work)"]
        },
        "त": {
            "meaning": "past participle",
            "grammatical_function": "verbal adjective",
            "semantic_impact": "completed action",
            "examples": ["गत (gone)", "कृत (done)"]
        },
        "तृ": {
            "meaning": "agent noun",
            "grammatical_function": "noun of agency",
            "semantic_impact": "doer of action",
            "examples": ["गन्ता (goer)", "कर्ता (doer)"]
        }
    },
    "तद्धित": {
        "इक": {
            "meaning": "relating to",
            "grammatical_function": "adjectival derivative",
            "semantic_impact": "characteristic or belonging",
            "examples": ["वैदिक (related to Veda)", "राजनीतिक (political)"]
        },
        "अक": {
            "meaning": "tendency or state",
            "grammatical_function": "nominal derivative",
            "semantic_impact": "quality or propensity",
            "examples": ["बालक (child-like)", "चतुराक (clever)"]
        },
        "य": {
            "meaning": "belonging to",
            "grammatical_function": "possessive derivative",
            "semantic_impact": "ownership or origin",
            "examples": ["ग्राम्य (village-related)", "देवत्य (divine)"]
        }
    }
}

class SandhiTransformer:
    """
    Advanced Sandhi transformation engine for Sanskrit linguistic processing.
    Implements comprehensive phonetic and morphological transformation rules.
    """
    
    # Comprehensive Consonant Classification
    CONSONANT_GROUPS = {
        "sparsha": {
            "ka_varga": ["क", "ख", "ग", "घ", "ङ"],
            "ca_varga": ["च", "छ", "ज", "झ", "ञ"],
            "ta_varga": ["ट", "ठ", "ड", "ढ", "ण"],
            "pa_varga": ["प", "फ", "ब", "भ", "म"]
        },
        "antastha": ["य", "र", "ल", "व"],
        "ushman": ["श", "ष", "स"],
        "jihvamuliya": ["ह"]
    }

    # Advanced Sandhi Transformation Rules
    SANDHI_RULES = {
        # Vowel Sandhi (Vowel Combination Rules)
        "vowel_sandhi": {
            "अ + इ": "ए",
            "अ + उ": "ओ",
            "इ + अ": "या",
            "उ + अ": "वा"
        },
        
        # Consonant Sandhi Rules
        "consonant_sandhi": {
            # Nasalization Rules
            "nasalization": {
                "म्": {
                    "before_ka_varga": "ङ",
                    "before_ca_varga": "ञ",
                    "before_ta_varga": "ण",
                    "before_pa_varga": "म"
                },
                "न्": {
                    "before_ka_varga": "ङ",
                    "before_ca_varga": "ञ",
                    "before_ta_varga": "ण",
                    "before_pa_varga": "म"
                }
            },
            
            # Visarga Sandhi Rules
            "visarga_sandhi": {
                "ः + क": "क्",
                "ः + प": "प्",
                "ः + च": "च्"
            },
            
            # Assimilation Rules
            "assimilation": {
                "dental_to_cerebral": {
                    "न् + ट": "ण्",
                    "न् + ठ": "ण्",
                    "न् + ड": "ण्"
                },
                "sibilant_transformation": {
                    "स् + क": "ष्",
                    "स् + प": "ष्"
                }
            }
        }
    }

    # Comprehensive Vowel Mapping
    VOWELS = {
        "short": ["अ", "इ", "उ"],
        "long": ["आ", "ई", "ऊ"],
        "diphthong": ["ए", "ऐ", "ओ", "औ"]
    }

    @classmethod
    def apply_vowel_sandhi(cls, first_vowel: str, second_vowel: str) -> Optional[str]:
        """
        Apply vowel combination rules.
        
        Args:
            first_vowel (str): First vowel in combination
            second_vowel (str): Second vowel in combination
        
        Returns:
            Optional[str]: Transformed vowel combination or None
        """
        vowel_key = f"{first_vowel} + {second_vowel}"
        return cls.SANDHI_RULES["vowel_sandhi"].get(vowel_key, second_vowel)

    @classmethod
    def apply_consonant_sandhi(cls, prefix: str, word: str) -> str:
        """
        Apply advanced consonant Sandhi transformation rules.
        
        Args:
            prefix (str): Prefix to be added
            word (str): Original word
        
        Returns:
            str: Modified word after applying Sandhi rules
        """
        # Detailed Sandhi transformation logic
        if prefix.endswith("म्"):
            # Nasalization rules
            for varga, consonants in cls.CONSONANT_GROUPS["sparsha"].items():
                if word[0] in consonants:
                    nasalization_map = {
                        "ka_varga": "सङ्",
                        "ca_varga": "सञ्",
                        "ta_varga": "सण्",
                        "pa_varga": "संप्"
                    }
                    prefix = nasalization_map.get(varga, "सम्")
                    break
        
        # Visarga and other complex transformations
        if prefix.endswith("ः"):
            # Preserve visarga in the output
            pass
        
        return prefix + word

    @classmethod
    def analyze_word_structure(cls, word: str) -> Dict[str, Union[str, List[str]]]:
        """
        Perform comprehensive linguistic analysis of a word.
        
        Args:
            word (str): Word to analyze
        
        Returns:
            Dict containing linguistic breakdown
        """
        analysis = {
            "original_word": word,
            "vowels": [],
            "consonants": [],
            "potential_roots": []
        }
        
        # Comprehensive vowel identification
        VOWELS = ["अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ", "औ"]
        
        # Find the first long or short vowel in the word
        for char in word:
            if char in VOWELS:
                analysis["vowels"] = [char]
                break
        
        # If no vowel found, default to अ
        if not analysis["vowels"]:
            analysis["vowels"] = ["अ"]
        
        # Comprehensive consonant identification
        all_consonants = []
        for group in cls.CONSONANT_GROUPS.values():
            if isinstance(group, dict):
                all_consonants.extend([c for sublist in group.values() for c in sublist])
            else:
                all_consonants.extend(group)
        
        for char in word:
            if char in all_consonants:
                if char not in analysis["consonants"]:
                    analysis["consonants"].append(char)
        
        return analysis

def apply_sandhi_rules(prefix: str, word: str) -> str:
    """
    Wrapper function for advanced Sandhi transformation.
    
    Args:
        prefix (str): Prefix to be added
        word (str): Original word
    
    Returns:
        str: Modified word after applying Sandhi rules
    """
    # Apply consonant Sandhi first
    modified_word = SandhiTransformer.apply_consonant_sandhi(prefix, word)
    
    return modified_word

def add_upasarga(word: str, upasarga: str) -> str:
    """
    Adds an upasarga (prefix) to a root word with Sandhi rules.
    
    Args:
        word (str): The root word to modify
        upasarga (str): The prefix to add
    
    Returns:
        str: Modified word with prefix
    
    Raises:
        ValueError: If the upasarga is not recognized
    """
    # Validate upasarga
    if upasarga not in UPASARGA_DICT:
        raise ValueError(f"Unrecognized upasarga: {upasarga}")
    
    # Apply Sandhi rules and add prefix
    modified_word = apply_sandhi_rules(upasarga, word)
    
    return modified_word

def add_pratyaya(word: str, pratyaya: str, pratyaya_type: str = "कृत्") -> str:
    """
    Adds a pratyaya (suffix) to a root word with appropriate rules.
    
    Args:
        word (str): The root word to modify
        pratyaya (str): The suffix to add
        pratyaya_type (str, optional): Type of pratyaya. Defaults to "कृत्".
    
    Returns:
        str: Modified word with suffix
    
    Raises:
        ValueError: If the pratyaya or pratyaya type is not recognized
    """
    # Validate pratyaya type and pratyaya
    if pratyaya_type not in PRATYAYA_DICT:
        raise ValueError(f"Unrecognized pratyaya type: {pratyaya_type}")
    
    if pratyaya not in PRATYAYA_DICT[pratyaya_type]:
        raise ValueError(f"Unrecognized pratyaya: {pratyaya}")
    
    # Remove trailing virama (्) if present
    if word.endswith('्'):
        word = word[:-1]
    
    # Apply specific Sandhi rules for suffix addition
    if word[-1] in "अइउ":
        # Vowel ending rules: replace last vowel
        modified_word = word[:-1] + pratyaya
    else:
        # Consonant ending rules: simply append
        modified_word = word + pratyaya
    
    return modified_word

def get_upasarga_meaning(upasarga: str) -> List[str]:
    """
    Retrieves the meanings of a given upasarga.
    
    Args:
        upasarga (str): The prefix to look up
    
    Returns:
        List[str]: List of meanings for the upasarga
    """
    return UPASARGA_DICT.get(upasarga, {}).get("meanings", [])
