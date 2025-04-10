Sandhi Module
============

Overview
--------

The Sandhi module implements the rules of Sanskrit sandhi (संधि), which are phonological rules governing sound changes that occur at word boundaries. This module provides functionality to apply various types of sandhi rules when combining Sanskrit words.

Types of Sandhi
-------------

1. Vowel Sandhi (स्वर संधि)
   - Combining vowels at word boundaries
   - Example: राम + इति = रामेति

2. Consonant Sandhi (व्यञ्जन संधि)
   - Rules for combining consonants
   - Example: वाक् + देवी = वाग्देवी

3. Visarga Sandhi (विसर्ग संधि)
   - Rules for handling visarga (ः)
   - Example: रामः + गच्छति = रामो गच्छति

Usage Examples
-------------

Basic Sandhi Operations
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from sanskrit_grammar.sandhi import sandhi_handler

    # Basic vowel sandhi
    result = sandhi_handler('राम', 'इति')
    print(result)  # Output: रामेति

    # Consonant sandhi
    result = sandhi_handler('वाक्', 'देवी')
    print(result)  # Output: वाग्देवी

Advanced Usage
~~~~~~~~~~~~

.. code-block:: python

    from sanskrit_grammar.sandhi import apply_vowel_sandhi, apply_consonant_sandhi

    # Specific vowel sandhi
    result = apply_vowel_sandhi('देव', 'आलय')
    print(result)  # Output: देवालय

    # Specific consonant sandhi
    result = apply_consonant_sandhi('तत्', 'कार')
    print(result)  # Output: तत्कार
