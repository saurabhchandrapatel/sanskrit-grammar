Stem Generator
============

Overview
--------

The Stem Generator module provides functionality for generating various forms of Sanskrit words, including compound words (समास) and their different grammatical forms. It implements rules for creating different types of compounds and handling their case endings.

Features
--------

1. Compound Word Generation
   - Tatpurusha (तत्पुरुष)
   - Dvandva (द्वन्द्व)
   - Bahuvrihi (बहुव्रीहि)
   - Avyayibhava (अव्ययीभाव)

2. Case and Gender Handling
   - Nominative case endings
   - Gender-specific forms
   - Number variations

Examples
--------

Basic Usage
~~~~~~~~~~

.. code-block:: python

    from sanskrit_grammar.stem_generator import generate_sanskrit_compound

    # Generate a basic compound
    paraphrase = {
        "first_component": "राज",
        "second_component": "पुरुष",
        "relation": "genitive",
        "gender": "masculine"
    }
    result = generate_sanskrit_compound(paraphrase)
    print(result)

Advanced Usage
~~~~~~~~~~~~

.. code-block:: python

    # Generate a compound with specific case and gender
    paraphrase = {
        "first_component": "देव",
        "second_component": "दत्त",
        "relation": "tatpurusha",
        "gender": "masculine"
    }
    result = generate_sanskrit_compound(paraphrase)
    print(result)

Operations
~~~~~~~~~

.. code-block:: python

    # Using individual component operations
    from sanskrit_grammar.stem_generator import (
        alaukikavigraha,
        samasa_anta,
        upasarjana_operations
    )

    # Apply specific operations
    result = alaukikavigraha("राज", "पुरुष")
    result = samasa_anta(result)
    result = upasarjana_operations(result, "before")
