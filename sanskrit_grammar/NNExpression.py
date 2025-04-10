import re
import matplotlib.pyplot as plt
import networkx as nx

# Basic segments in a Navya Nyaya expression
segments = ['धर्म', 'अर्थ', 'काम', 'मोक्ष', 'सिद्धान्त', 'विवेचन', 'किञ्च', 'न']

# Function to segment the Navya Nyaya expression
def segment_nn_expression(expression):
    expression = expression.strip()
    segments_found = []

    for segment in segments:
        if segment in expression:
            segments_found.append(segment)
            expression = expression.replace(segment, f"[{segment}]")

    return expression, segments_found

# Function to parse the Navya Nyaya expression
def parse_nn_expression(expression):
    expression = expression.strip()
    parsed_structure = {}

    quantifiers = ['किञ्च', 'न']
    for q in quantifiers:
        if q in expression:
            parsed_structure['quantifier'] = q
            expression = expression.replace(q, '')

    terms = ['धर्म', 'अर्थ', 'काम', 'मोक्ष', 'सिद्धान्त', 'विवेचन']
    parsed_terms = []
    for term in terms:
        if term in expression:
            parsed_terms.append(term)
            expression = expression.replace(term, '')

    parsed_structure['terms'] = parsed_terms
    parsed_structure['remaining_expression'] = expression.strip()

    return parsed_structure

# Function to render a graphical representation of the parsed expression
def render_graph(parsed_expression):
    """
    Render the graphical representation of the parsed expression.
    Uses NetworkX to create a directed graph and Matplotlib for visualization.
    """
    G = nx.DiGraph()

    G.add_node('Expression')
    for term in parsed_expression['terms']:
        G.add_node(term)
        G.add_edge('Expression', term)

    if 'quantifier' in parsed_expression:
        quantifier = parsed_expression['quantifier']
        G.add_node(quantifier)
        G.add_edge('Expression', quantifier)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=12, font_weight="bold", arrows=True)
    plt.show()
