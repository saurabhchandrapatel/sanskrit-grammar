Ashtadhyayi Simulator API Reference
=====================================

This page contains the detailed API reference for the Ashtadhyayi Simulator module.

.. module:: sanskrit_grammar.ashtadhyayi_simulator

Classes
-------

.. autoclass:: PaniniSutras
   :members:
   :undoc-members:
   :show-inheritance:

Methods
-------

.. automethod:: PaniniSutras.apply_sutra

.. automethod:: PaniniSutras.nakara_svara

.. automethod:: PaniniSutras.vowel_to_vowel_rule

.. automethod:: PaniniSutras.apply_declension

Example Usage
--------------

.. code-block:: python

    # Create an instance of PaniniSutras
    panini = PaniniSutras()

    # Apply a specific sutra
    result = panini.apply_sutra('nakara_svara', 'नकार')
    print(result)  # Output: नकारं

    # Apply vowel transformation
    result = panini.apply_sutra('vowel_to_vowel_rule', 'राजा')
    print(result)  # Output: राजी

    # Apply declension
    result = panini.apply_declension('देवा')
    print(result)  # Output: देवां
