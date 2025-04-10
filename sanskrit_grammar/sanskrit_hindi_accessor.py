import sqlite3
import re
import json
import logging
from typing import List, Dict, Optional, Union, Any

# Enhanced logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Database setup (Stores Sanskrit words and Hindi glosses)
DB_NAME = "sanskrit_hindi_dict.db"
DICTIONARY_FILE = "comprehensive_sanskrit_dictionary.json"

def initialize_database():
    """
    Initialize SQLite database with enhanced schema for Sanskrit-Hindi word mappings.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Enhanced table schema
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS SanskritHindi (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sanskrit_word TEXT UNIQUE,
                hindi_gloss TEXT,
                word_type TEXT,
                grammatical_gender TEXT,
                etymology TEXT,
                usage_context TEXT
            )
        ''')
        
        # Create index for faster lookups
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_sanskrit_word ON SanskritHindi(sanskrit_word)')
        
        conn.commit()
        logger.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logger.error(f"Database initialization error: {e}")
    finally:
        conn.close()

def load_comprehensive_dictionary():
    """
    Load a comprehensive Sanskrit-Hindi dictionary from a JSON file.
    """
    try:
        with open(DICTIONARY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning(f"Dictionary file {DICTIONARY_FILE} not found. Creating empty dictionary.")
        return {}
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in {DICTIONARY_FILE}")
        return {}

# Comprehensive Sandhi Splitting Rules
SANDHI_RULES = {
    # Consonant Sandhi
    "final_consonant_changes": {
        "त्": ["द्", "ध्"],
        "क्": ["ग्", "घ्"],
        "प्": ["ब्", "भ्"]
    },
    
    # Vowel Sandhi
    "vowel_merging": {
        "अ + इ": "ए",
        "अ + उ": "ओ",
        "ए + अ": "ऐ",
        "ओ + अ": "औ"
    },
    
    # Complex Sandhi Patterns
    "complex_patterns": {
        "रामस्य": ["राम", "स्य"],
        "गच्छति": ["गम्", "ति"],
        "पठति": ["पठ", "ति"],
        "करोति": ["कृ", "ति"]
    }
}

def advanced_word_analysis(word: str) -> Dict[str, Union[List[str], str]]:
    """
    Advanced Sanskrit word analysis with comprehensive Sandhi splitting.
    
    Args:
        word (str): Sanskrit word to analyze
    
    Returns:
        Dict containing analysis results
    """
    analysis = {
        "original_word": word,
        "split_words": [],
        "sandhi_type": "unknown",
        "root_word": word
    }
    
    # Check complex patterns first
    if word in SANDHI_RULES['complex_patterns']:
        analysis.update({
            "split_words": SANDHI_RULES['complex_patterns'][word],
            "sandhi_type": "complex"
        })
        return analysis
    
    # Consonant Sandhi Analysis
    for final, replacements in SANDHI_RULES['final_consonant_changes'].items():
        if word.endswith(final):
            for replacement in replacements:
                potential_root = word[:-len(final)] + replacement
                analysis.update({
                    "split_words": [potential_root, final],
                    "sandhi_type": "consonant",
                    "root_word": potential_root
                })
                break
    
    # Vowel Sandhi Analysis
    for pattern, result in SANDHI_RULES['vowel_merging'].items():
        if result in word:
            analysis.update({
                "split_words": pattern.split(" + "),
                "sandhi_type": "vowel",
                "merged_result": result
            })
    
    return analysis

def enhanced_dependency_resolution(words: List[str]) -> Dict[str, Dict[str, str]]:
    """
    Advanced dependency resolution with grammatical role detection.
    
    Args:
        words (List[str]): List of Sanskrit words
    
    Returns:
        Dict of word-level grammatical analysis
    """
    # Enhanced grammatical role mapping
    GRAMMATICAL_ROLES = {
        "कर्ता": ["ः", "म्"],  # Nominative markers
        "कर्म": ["म्"],        # Accusative markers
        "करण": ["एण"],        # Instrumental markers
        "सम्प्रदान": ["आय"],   # Dative markers
        "अपादान": ["आत्"],     # Ablative markers
        "सम्बन्ध": ["स्य"]     # Genitive markers
    }
    
    word_analysis = {}
    
    for word in words:
        analysis = {
            "word": word,
            "grammatical_roles": [],
            "potential_root": word
        }
        
        # Detect grammatical roles based on word endings
        for role, markers in GRAMMATICAL_ROLES.items():
            if any(word.endswith(marker) for marker in markers):
                analysis["grammatical_roles"].append(role)
        
        # Attempt root word extraction
        for marker in sum(GRAMMATICAL_ROLES.values(), []):
            if word.endswith(marker):
                analysis["potential_root"] = word[:-len(marker)]
                break
        
        word_analysis[word] = analysis
    
    return word_analysis

def translate_sentence_advanced(sentence: str) -> Dict[str, Any]:
    """
    Advanced Sanskrit sentence translation and analysis.
    
    Args:
        sentence (str): Sanskrit sentence to translate
    
    Returns:
        Comprehensive translation and linguistic analysis
    """
    # Tokenize sentence
    words = re.findall(r'\b\w+\b', sentence)
    
    # Comprehensive analysis
    translation_result = {
        "original_sentence": sentence,
        "word_analysis": {},
        "dependency_graph": {},
        "translation_candidates": []
    }
    
    dictionary = load_comprehensive_dictionary()
    
    for word in words:
        # Advanced word analysis
        word_details = advanced_word_analysis(word)
        
        # Dictionary lookup
        hindi_meanings = dictionary.get(word, ["❌ अर्थ उपलब्ध नहीं है"])
        
        translation_result["word_analysis"][word] = {
            "sandhi_analysis": word_details,
            "hindi_meanings": hindi_meanings
        }
    
    # Dependency resolution
    translation_result["dependency_graph"] = enhanced_dependency_resolution(words)
    
    return translation_result

def add_word_to_dictionary(
    sanskrit_word: str, 
    hindi_gloss: str, 
    word_type: Optional[str] = None, 
    grammatical_gender: Optional[str] = None,
    etymology: Optional[str] = None,
    usage_context: Optional[str] = None
):
    """
    Enhanced word addition with comprehensive metadata.
    
    Args:
        sanskrit_word (str): Sanskrit word to add
        hindi_gloss (str): Hindi meaning
        word_type (Optional[str]): Type of word (noun, verb, etc.)
        grammatical_gender (Optional[str]): Grammatical gender
        etymology (Optional[str]): Word origin
        usage_context (Optional[str]): Contextual usage
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT OR REPLACE INTO SanskritHindi 
            (sanskrit_word, hindi_gloss, word_type, grammatical_gender, etymology, usage_context) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            sanskrit_word, 
            hindi_gloss, 
            word_type, 
            grammatical_gender, 
            etymology, 
            usage_context
        ))
        conn.commit()
        logger.info(f"Added/Updated word: {sanskrit_word}")
    except sqlite3.Error as e:
        logger.error(f"Error adding word {sanskrit_word}: {e}")
    finally:
        conn.close()
