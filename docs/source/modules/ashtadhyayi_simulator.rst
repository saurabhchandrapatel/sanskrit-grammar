Ashtadhyayi Simulator
===================

Overview
--------

The Ashtadhyayi Simulator module implements a computational model of Panini's grammar rules. It provides a class-based approach to applying various Sanskrit grammar transformations based on Paninian rules.

Features
--------

1. Rule Application
   - Application of specific Paninian sutras
   - Vowel transformation rules
   - Consonant transformation rules
   - Declension handling

2. Supported Rules
   - Nakara Svara (नकार स्वर) transformations
   - Vowel-to-vowel transformations
   - Basic declension rules

Usage Examples
-------------

Basic Rule Application
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from sanskrit_grammar.ashtadhyayi_simulator import PaniniSutras

    # Create an instance of PaniniSutras
    panini = PaniniSutras()

    # Apply nakara svara rule
    result = panini.apply_sutra('nakara_svara', 'नकार')
    print(result)  # Output: नकारं

Vowel Transformations
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Apply vowel transformation rule
    result = panini.apply_sutra('vowel_to_vowel_rule', 'राजा')
    print(result)  # Output: राजी

Declension Application
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Apply declension rules
    result = panini.apply_declension('देवा')
    print(result)  # Output: देवां

Advanced Usage
~~~~~~~~~~~~

.. code-block:: python

    # Chain multiple transformations
    word = 'राजा'
    word = panini.apply_sutra('vowel_to_vowel_rule', word)
    word = panini.apply_declension(word)
    print(word)
