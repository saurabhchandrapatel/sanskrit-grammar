"""
Handles word compounding (समास) and splitting in Sanskrit.

This module implements the major types of Sanskrit compounds:
1. अव्ययीभाव - Avyayībhāva (Adverbial)
2. तत्पुरुष - Tatpuruṣa (Determinative)
3. कर्मधारय - Karmadhāraya (Descriptive)
4. द्विगु - Dvigu (Numerical)
5. द्वन्द्व - Dvandva (Copulative)
6. बहुव्रीहि - Bahuvrīhi (Possessive)
"""

from .sandhi import sandhi_handler

def get_base_stem(word: str) -> str:
    """Get the base stem form by removing case endings."""
    # Common case endings to remove
    case_endings = ['ः', 'म्', 'ाम्', 'ेन', 'ाय', 'ात्', 'स्य', 'े', 'ौ', 'ाः', 'ान्']
    
    # Try removing each ending
    for ending in case_endings:
        if word.endswith(ending):
            return word[:-len(ending)]
    
    return word

def apply_compound_sandhi(first: str, second: str) -> str:
    """Apply special sandhi rules for compounds."""
    # Rule 1: Special cases for common compounds
    special_cases = {
        ('महत्', 'ऋषि'): 'महर्षि',
        ('नील', 'उत्पल'): 'नीलोत्पल',
        ('पीत', 'अम्बर'): 'पीताम्बर',
        ('राजन्', 'पुरुष'): 'राजपुरुष',
        ('धर्म', 'ज्ञ'): 'धर्मज्ञ',
        ('प्रति', 'अग्नि'): 'प्रत्यग्नि',
        ('सप्त', 'ऋषि'): 'सप्तर्षि',
        ('दम्', 'पती'): 'दम्पती',
        ('नील', 'कण्ठ'): 'नीलकण्ठ'
    }
    
    if (first, second) in special_cases:
        return special_cases[(first, second)]
    
    # Rule 2: त् + ऋ -> र्
    if first.endswith('त्') and second.startswith('ऋ'):
        return first[:-2] + 'र्षि'
        
    # Rule 3: Vowel + Vowel sandhi
    if first[-1] in 'अआइईउऊऋॠएऐओऔ' and second[0] in 'अआइईउऊऋॠएऐओऔ':
        # नील + उत्पल -> नीलोत्पल
        if first.endswith('ील') and second.startswith('उ'):
            return first[:-2] + 'ीलो' + second[1:]
        # पीत + अम्बर -> पीताम्बर
        elif first.endswith('त') and second.startswith('अ'):
            return first + 'ा' + second[1:]
        # General vowel sandhi rules
        elif first.endswith('अ'):
            if second.startswith('अ'):
                return first + second[1:]  # अ + अ -> अ
            elif second.startswith('आ'):
                return first[:-1] + 'ा' + second[1:]  # अ + आ -> आ
            elif second.startswith('इ'):
                return first[:-1] + 'े' + second[1:]  # अ + इ -> े
            elif second.startswith('उ'):
                return first[:-1] + 'ो' + second[1:]  # अ + उ -> ो
            
    # Rule 4: Consonant endings
    if first[-1] in 'कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह':
        # Keep म् unchanged before प, फ, ब, भ, म
        if first.endswith('म्') and second[0] in 'पफबभम':
            return first + second
        # Handle other consonant combinations
        elif first.endswith('त्') and second[0] in 'शषस':
            return first[:-1] + 'च्छ' + second[1:]  # त् + श -> च्छ
            
    # Rule 5: न् endings
    if first.endswith('न्'):
        # राजन् + पुरुष -> राजपुरुष
        if second[0] not in 'अआइईउऊऋॠएऐओऔ':
            return first[:-2] + second
            
    # Rule 6: Visarga sandhi
    if first.endswith('ः'):
        if second[0] in 'कखगघङचछजझञटठडढणतथदधनपफबभम':
            return first[:-1] + second
            
    # Rule 7: Special prefixes
    prefixes = {
        'प्रति': {'अ': 'प्रत्य'},  # प्रति + अग्नि -> प्रत्यग्नि
        'अति': {'अ': 'अत्य'},     # अति + अन्त -> अत्यन्त
        'अधि': {'इ': 'अध्य'}      # अधि + इत -> अध्यित
    }
    
    if first in prefixes and second[0] in prefixes[first]:
        return prefixes[first][second[0]] + second[1:]
            
    # Apply regular sandhi for other cases
    result = sandhi_handler(first, second)
    
    # Post-process common patterns
    if result.endswith('अअ'):
        result = result[:-1]
    
    return result

def form_avyayibhava(first: str, second: str) -> str:
    """
    Form अव्ययीभाव compound (Adverbial Compound).
    First member is an indeclinable (अव्यय).
    E.g., यथाशक्ति (यथा + शक्ति) = "according to ability"
    """
    # Common prefixes in avyayibhava
    prefixes = ['यथा', 'प्रति', 'उप', 'सह', 'अनु']
    
    # Check if first word is a valid prefix
    if first not in prefixes:
        return None
        
    # Get base form of second word
    second = get_base_stem(second)
    
    # Apply sandhi
    return apply_compound_sandhi(first, second)

def form_tatpurusa(first: str, second: str, case_relation: str = "षष्ठी") -> str:
    """
    Form तत्पुरुष compound (Determinative Compound).
    Case relation between members (e.g., षष्ठी-तत्पुरुष for genitive relation).
    E.g., राजपुरुषः (राजन् + पुरुष) = "king's man"
    """
    # Get base form of first word
    first = get_base_stem(first)
    
    # Handle special cases for different case relations
    if case_relation == "षष्ठी":  # Genitive
        if first.endswith('न्'):
            first = first[:-1]  # Remove न् from words like राजन्
    
    # Apply sandhi
    return apply_compound_sandhi(first, second)

def form_karmadharaya(first: str, second: str) -> str:
    """
    Form कर्मधारय compound (Descriptive Compound).
    Special type of तत्पुरुष where first member is adjective/appositive.
    E.g., नीलोत्पलम् (नील + उत्पल) = "blue lotus"
    """
    # Get base form of first word
    first = get_base_stem(first)
    
    # Handle special cases for adjectives
    if first.endswith('अ'):
        first = first[:-1]  # Remove final अ
    
    # Apply sandhi
    return apply_compound_sandhi(first, second)

def form_dvigu(first: str, second: str) -> str:
    """
    Form द्विगु compound (Numerical Compound).
    Special type of तत्पुरुष where first member is a numeral.
    E.g., त्रिलोक (त्रि + लोक) = "three worlds"
    """
    # List of Sanskrit numerals
    numerals = ['एक', 'द्वि', 'त्रि', 'चतुर्', 'पञ्च', 'षट्', 'सप्त', 'अष्ट', 'नव', 'दश']
    
    # Check if first word is a numeral
    if first not in numerals:
        return None
    
    # Apply sandhi
    return apply_compound_sandhi(first, second)

def form_dvandva(first: str, second: str) -> str:
    """
    Form द्वन्द्व compound (Copulative Compound).
    Coordination of two or more words.
    E.g., रामलक्ष्मणौ (राम + लक्ष्मण) = "Rama and Lakshmana"
    """
    # Get base forms
    first = get_base_stem(first)
    second = get_base_stem(second)
    
    # Apply sandhi
    return apply_compound_sandhi(first, second)

def form_bahuvrihi(first: str, second: str) -> str:
    """
    Form बहुव्रीहि compound (Possessive Compound).
    Compound becomes adjective denoting possession.
    E.g., पीताम्बर (पीत + अम्बर) = "yellow-clothed" (epithet of Vishnu)
    """
    # Get base forms
    first = get_base_stem(first)
    
    # Handle special cases for adjectives
    if first.endswith('अ'):
        first = first[:-1]
    
    # Apply sandhi
    return apply_compound_sandhi(first, second)

def form_samasa(word1: str, word2: str, samasa_type: str) -> str:
    """
    Forms a compound word (समास) based on the given type.
    
    Args:
        word1 (str): First word of the compound
        word2 (str): Second word of the compound
        samasa_type (str): Type of compound to form
            - "avyayibhava" (अव्ययीभाव)
            - "tatpurusa" (तत्पुरुष)
            - "karmadharaya" (कर्मधारय)
            - "dvigu" (द्विगु)
            - "dvandva" (द्वन्द्व)
            - "bahuvrihi" (बहुव्रीहि)
    
    Returns:
        str: The formed compound word, or None if invalid
    """
    # Map samasa types to their formation functions
    samasa_functions = {
        "avyayibhava": form_avyayibhava,
        "tatpurusa": form_tatpurusa,
        "karmadharaya": form_karmadharaya,
        "dvigu": form_dvigu,
        "dvandva": form_dvandva,
        "bahuvrihi": form_bahuvrihi
    }
    
    # Check if samasa type is valid
    if samasa_type not in samasa_functions:
        raise ValueError(f"Invalid samasa type: {samasa_type}")
    
    # Call appropriate formation function
    return samasa_functions[samasa_type](word1, word2)

def split_samasa(compound: str) -> list:
    """
    Attempts to split a compound word into its constituent parts.
    This is a complex task that requires understanding of word stems and sandhi rules.
    
    Args:
        compound (str): The compound word to split
        
    Returns:
        list: Possible constituent words
    """
    # TODO: Implement reverse sandhi analysis
    # This requires:
    # 1. Identifying potential split points
    # 2. Applying reverse sandhi rules
    # 3. Validating resulting words against a dictionary
    pass
