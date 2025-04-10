Upasarga and Pratyaya Module
==========================

Overview
--------

The Upasarga and Pratyaya module provides advanced tools for handling Sanskrit word prefixes (Upasarga) and suffixes (Pratyaya). This module is crucial for understanding and generating complex Sanskrit word formations.

Key Functions
-------------

1. Add Pratyaya
~~~~~~~~~~~~~~~

The ``add_pratyaya`` function allows adding suffixes to root words with appropriate linguistic rules:

.. code-block:: python

    from sanskrit_grammar.upasarga_pratyaya import add_pratyaya

    # Add a कृत् (Krit) pratyaya
    modified_word = add_pratyaya("गम्", "अ")
    print(modified_word)  # Output: गमा

2. Pratyaya Types
~~~~~~~~~~~~~~~~

Supported Pratyaya Types:
- कृत् (Krit): Verbal derivative suffixes
- तद्धित: Nominal derivative suffixes

Example Usage
-------------

.. code-block:: python

    # Adding different types of pratyayas
    verb_form = add_pratyaya("पठ्", "अ", pratyaya_type="कृत्")
    noun_form = add_pratyaya("राज", "इक", pratyaya_type="तद्धित")

Error Handling
--------------

The function raises ``ValueError`` for:
- Unrecognized pratyaya types
- Invalid pratyaya for a given type

API Reference
-------------

.. py:function:: add_pratyaya(word: str, pratyaya: str, pratyaya_type: str = "कृत्")

   Add a pratyaya (suffix) to a root word with appropriate rules.

   :param word: The root word to modify
   :type word: str
   :param pratyaya: The suffix to add
   :type pratyaya: str
   :param pratyaya_type: Type of pratyaya, defaults to "कृत्"
   :type pratyaya_type: str, optional
   :returns: Modified word with suffix
   :rtype: str
   :raises ValueError: If pratyaya or pratyaya type is not recognized
