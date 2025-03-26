
This Python module provides functions to handle and manipulate various aspects of Sanskrit grammar, including **word generation**, **prefixes (Upasarga)**, **suffixes (Pratyaya)**, **verb conjugation**, **noun declension**, **Sandhi** (joining words), **Sandhi Vechheda** (splitting words), and **tense identification**. The module is designed to be a foundational tool for working with Sanskrit words and sentences in Python, supporting multiple grammatical operations, and it can be extended further as per specific needs.

---

### Key Functions:

1. **Upasarga (Prefix) and Pratyaya (Suffix) Functions**:
   - These functions allow the application of **Upasargas** (prefixes) and **Pratyayas** (suffixes) to a root word. 
   - The module contains predefined lists of common prefixes and suffixes used in Sanskrit grammar, which can be added to root words to generate valid forms.

2. **Sandhi (Joining Words)**:
   - The **sandhi** function applies the rules of Sandhi, which deal with the joining of words in Sanskrit.
   - It simplifies joining two words based on common Sandhi rules (e.g., dropping the last vowel of the first word if it's a vowel and appending the second word).

3. **Sandhi Vechheda (Splitting Words)**:
   - The **sandhi_vechheda** function splits joined words based on common Sandhi rules and returns their components.
   
4. **Verb Conjugation**:
   - The module supports **simplified verb conjugation** in the **present** and **past** tenses for **first** and **third-person singular/plural** forms.
   - This function uses basic rules of conjugation for Sanskrit verbs and can be extended for more complex verb forms (e.g., future, conditional, etc.).

5. **Noun Declension**:
   - The **declense_noun** function provides simplified declension for a noun based on the **nominative case** and **singular/plural** forms.
   - It can be expanded to handle more cases (genitive, accusative, etc.) and genders (masculine, feminine, neuter).

6. **Tense Identification**:
   - The **identify_tense** function helps identify the tense of a verb based on common suffixes associated with different tenses.
   - It currently recognizes verbs in the present and past tenses.

7. **Word Generation**:
   - The **generate_sanskrit_word** function demonstrates how to generate a valid Sanskrit word by applying both a prefix (Upasarga) and suffix (Pratyaya) to a given root word.

---

### Example Usage:

The following are a few examples demonstrating how to use the module:

```python
import sanskrit_grammar

# Apply Upasarga (prefix) to a root word
print(sanskrit_grammar.apply_upasarga("धार", "प्र"))  
# Output: प्रधार

# Apply Pratyaya (suffix) to a root word
print(sanskrit_grammar.apply_pratyaya("धार", "-त्र"))
# Output: धारत्र

# Conjugate verb in present tense, 3rd person, plural
print(sanskrit_grammar.conjugate_verb("गच्छ", "present", "3rd", "plural"))
# Output: गच्छन्ति

# Generate a word by applying Upasarga and Pratyaya to a root word
print(sanskrit_grammar.generate_sanskrit_word("धार", "प्र", "-त्र"))
# Output: प्रधारत्र
```

---

### Features:
- **Modularity**: Each function in the module is independent, allowing users to pick and use only the functions they need.
- **Extendability**: The module is designed to be extended. You can add more complex conjugation rules, declension types, or Sandhi handling as necessary.
- **Sanskrit Grammar Rules**: Includes a simplified version of the complex rules for **Sandhi**, **verb conjugation**, and **noun declension**.

---

### Use Cases:
- **Sanskrit NLP Projects**: This module can be used in projects that involve processing Sanskrit text, such as building an NLP pipeline or generating words using grammatical rules.
- **Learning Aid**: A useful tool for Sanskrit learners to understand and generate conjugated verbs, declined nouns, and apply grammatical rules to words.
- **Sanskrit-based Applications**: It can serve as a backend for Sanskrit-related applications like text processing, grammar checking, and automated word generation.

---

### Potential Improvements:
- **Extended Conjugation**: Handle more verb tenses, moods, and persons (future tense, conditional mood, etc.).
- **Complete Declension**: Implement full noun declension for all cases and genders.
- **Advanced Sandhi**: Improve Sandhi and Sandhi Vechheda to handle more complex forms, including exceptions and advanced rules.
- **Integrating with NLP tools**: The module can be integrated with other NLP libraries for tokenization, morphological analysis, etc.

---

This module provides a solid foundation for working with Sanskrit grammar, allowing users to perform various grammatical operations programmatically. It is ideal for anyone working with Sanskrit text or developing applications that require grammatical analysis and word generation.
