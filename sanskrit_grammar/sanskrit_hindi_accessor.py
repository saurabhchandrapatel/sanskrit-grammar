import sqlite3
import re

# Database setup (Stores Sanskrit words and Hindi glosses)
DB_NAME = "sanskrit_hindi_dict.db"

def initialize_database():
    """
    Initialize SQLite database to store Sanskrit-Hindi word mappings.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SanskritHindi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sanskrit_word TEXT UNIQUE,
            hindi_gloss TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_word(sanskrit_word, hindi_gloss):
    """
    Add a Sanskrit word and its Hindi gloss to the database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO SanskritHindi (sanskrit_word, hindi_gloss) VALUES (?, ?)", 
                       (sanskrit_word, hindi_gloss))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"⚠️ '{sanskrit_word}' already exists in the dictionary.")
    finally:
        conn.close()

def get_hindi_meaning(sanskrit_word):
    """
    Retrieve Hindi meaning for a given Sanskrit word.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT hindi_gloss FROM SanskritHindi WHERE sanskrit_word = ?", (sanskrit_word,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "❌ अर्थ उपलब्ध नहीं है"

# --- 2️⃣ शब्द-विश्लेषणम् (Sabda-viśleṣaṇam) ---
def word_analysis(word):
    """
    Perform basic Sanskrit word analysis (split Sandhi if applicable).
    """
    # Example of simple Sandhi splitting (Advanced model can be added)
    sandhi_patterns = {
        "रामस्य": ["राम", "स्य"],
        "मित्रस्य": ["मित्र", "स्य"],
        "गच्छति": ["गम्", "ति"]
    }
    return sandhi_patterns.get(word, [word])  # Return split words or original word

# --- 3️⃣ आकांक्षा (Ākāṅkṣā - Dependency Resolution) ---
def dependency_resolution(words):
    """
    Determine word dependency based on basic syntax rules.
    """
    dependencies = {
        "रामः": "कर्ता (Subject)",
        "गच्छति": "क्रिया (Verb)",
        "फलम्": "कर्म (Object)",
        "मित्रम्": "संबंध (Relation)"
    }
    return {word: dependencies.get(word, "❓ अज्ञात भूमिका") for word in words}

# --- 4️⃣ संस्कृत वाक्य की व्याख्या हिंदी में (Sentence Breakdown) ---
def translate_sentence(sentence):
    """
    Translate a Sanskrit sentence to Hindi using word analysis.
    """
    words = re.findall(r'\b\w+\b', sentence)  # Tokenize sentence
    hindi_translation = []

    for word in words:
        split_words = word_analysis(word)
        for sw in split_words:
            hindi_translation.append(f"{sw} ({get_hindi_meaning(sw)})")
    
    return " | ".join(hindi_translation)
