Welcome to Sanskrit Grammar's documentation!
=======================================

Sanskrit Grammar is a Python library for processing and analyzing Sanskrit text. It provides tools for sandhi operations, morphological analysis, and compound word generation.

Features
--------

* Sandhi (संधि) - Rules for combining characters and words
* Morphological Analysis - Analyzing word structure and components
* Compound Word Generation - Creating and analyzing Sanskrit compounds
* Stem Generation - Generating various word forms

Installation
-----------

You can install the package using pip:

.. code-block:: bash

   pip install sanskrit-grammar

Quick Start
----------

Here's a simple example of using the sandhi module:

.. code-block:: python

   from sanskrit_grammar.sandhi import sandhi_handler
   
   # Combine two words using sandhi rules
   result = sandhi_handler('राम', 'इति')
   print(result)  # Output: रामेति

Contents
--------

.. toctree::
   :maxdepth: 2
   
   modules/sandhi
   modules/morphological_analyzer
   modules/stem_generator
   modules/ashtadhyayi_simulator

API Reference
------------

.. toctree::
   :maxdepth: 2
   
   api/sandhi
   api/morphological_analyzer
   api/stem_generator
   api/ashtadhyayi_simulator

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
