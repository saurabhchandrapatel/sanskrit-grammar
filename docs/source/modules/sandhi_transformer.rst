Sandhi Transformer
=================

Overview
--------

The Sandhi Transformer is an advanced linguistic processing engine designed for comprehensive Sanskrit word analysis. It provides sophisticated methods for understanding word structure, consonant groups, and linguistic transformations.

Key Features
------------

1. Word Structure Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``analyze_word_structure`` method performs a comprehensive linguistic breakdown of Sanskrit words:

- Identifies the original word
- Extracts primary vowels
- Classifies consonants
- Detects potential roots

Example
^^^^^^^

.. code-block:: python

    from sanskrit_grammar.upasarga_pratyaya import SandhiTransformer

    # Analyze word structure
    result = SandhiTransformer.analyze_word_structure("राम")
    print(result)
    # Output: {
    #   'original_word': 'राम',
    #   'vowels': ['आ'],
    #   'consonants': ['र', 'म'],
    #   'potential_roots': []
    # }

2. Consonant Classification
~~~~~~~~~~~~~~~~~~~~~~~~~~

The transformer includes a comprehensive consonant group classification:

- Sparsha (Stops): ka_varga, ca_varga, ta_varga, pa_varga
- Antastha (Semivowels): य, र, ल, व
- Ushman (Sibilants): श, ष, स
- Jihvamuliya: ह

Detailed Consonant Groups
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    print(SandhiTransformer.CONSONANT_GROUPS)
    # Detailed nested dictionary of consonant classifications

API Reference
-------------

.. py:class:: SandhiTransformer

   .. py:classmethod:: analyze_word_structure(word: str) -> Dict[str, Union[str, List[str]]]

      Perform comprehensive linguistic analysis of a Sanskrit word.

      :param word: Sanskrit word to analyze
      :type word: str
      :returns: Dictionary with linguistic breakdown
      :rtype: Dict[str, Union[str, List[str]]]

   .. py:attribute:: CONSONANT_GROUPS

      A comprehensive classification of Sanskrit consonants into linguistic groups.
