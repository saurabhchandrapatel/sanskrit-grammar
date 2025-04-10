Morphological Analyzer
====================

Overview
--------

The Morphological Analyzer module provides tools for analyzing Sanskrit words and breaking them down into their constituent parts. It can identify roots (धातु), prefixes (उपसर्ग), suffixes (प्रत्यय), and other morphological components.

Features
--------

1. Word Analysis
   - Identification of root words (धातु)
   - Detection of prefixes (उपसर्ग)
   - Recognition of suffixes (प्रत्यय)

2. Grammatical Analysis
   - Case identification (विभक्ति)
   - Gender recognition (लिंग)
   - Number determination (वचन)

Usage Examples
-------------

Basic Word Analysis
~~~~~~~~~~~~~~~~

.. code-block:: python

    from sanskrit_grammar.morphological_analyzer import analyze_sanskrit_word

    # Analyze a verb form
    result = analyze_sanskrit_word('गच्छति')
    print(result)
    # Output: {
    #     'धातु': 'गम्',
    #     'प्रत्यय': 'ति',
    #     'type': 'verb'
    # }

Pratyaya (Suffix) Identification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from sanskrit_grammar.morphological_analyzer import identify_pratyaya

    # Identify suffixes in a word
    result = identify_pratyaya('करोति')
    print(result)
    # Output: {
    #     'प्रत्यय': 'ओति',
    #     'type': 'verb_suffix'
    # }

Advanced Analysis
~~~~~~~~~~~~~~

.. code-block:: python

    # Analyze a word with prefix (उपसर्ग)
    result = analyze_sanskrit_word('प्रगच्छति')
    print(result)
    # Output: {
    #     'उपसर्ग': 'प्र',
    #     'धातु': 'गम्',
    #     'प्रत्यय': 'ति',
    #     'type': 'verb'
    # }
