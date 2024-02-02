# Process a document
document = nlp("Intelligence suggests that a meeting between leaders is scheduled in Washington next week.")

# Extract and print named entities
entities = [(ent.text, ent.label_) for ent in document.ents]
print("Named Entities:", entities)

import spacy
# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

gardenpathSentences = [
    "The old man the boats.",
    "The complex houses married and single soldiers and their families."
]


gardenpathSentences = [
    "The old man the boats.",
    "The complex houses married and single soldiers and their families.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Tokenize and perform named entity recognition for each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    
    # Tokenize and display each token
    tokens = [token.text for token in doc]
    print(f"Tokens for '{sentence}': {tokens}")
    
    # Perform named entity recognition and display entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print(f"Named Entities for '{sentence}': {entities}")
    
    print("\n----------------------\n")
	


""" OUTPUT

Tokens for 'The old man the boats.': ['The', 'old', 'man', 'the', 'boats', '.']
Named Entities for 'The old man the boats.': []

----------------------

Tokens for 'The complex houses married and single soldiers and their families.': ['The', 'complex', 'houses', 'married', 'and', 'single', 'soldiers', 'and', 'their', 'families', '.']
Named Entities for 'The complex houses married and single soldiers and their families.': []

----------------------

Tokens for 'Mary gave the child a Band-Aid.': ['Mary', 'gave', 'the', 'child', 'a', 'Band', '-', 'Aid', '.']
Named Entities for 'Mary gave the child a Band-Aid.': [('Mary', 'PERSON')]

----------------------

Tokens for 'That Jill is never here hurts.': ['That', 'Jill', 'is', 'never', 'here', 'hurts', '.']
Named Entities for 'That Jill is never here hurts.': [('Jill', 'PERSON')]

----------------------

Tokens for 'The cotton clothing is made of grows in Mississippi.': ['The', 'cotton', 'clothing', 'is', 'made', 'of', 'grows', 'in', 'Mississippi', '.']
Named Entities for 'The cotton clothing is made of grows in Mississippi.': [('Mississippi', 'GPE')]

----------------------

"""

# Lets go one better and rewrite the code to include comments
# Tokenise and perform named entity recognition for each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    
    # Tokenize and display each token
    tokens = [token.text for token in doc]
    print(f"Tokens for '{sentence}': {tokens}")
    
    # Perform named entity recognition and display entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print(f"Named Entities for '{sentence}': {entities}")
    
    # Explain the meaning of each entity
    for ent, label in entities:
        explanation = spacy.explain(label)
        print(f"Explanation for '{ent}' (Entity Type: {label}): {explanation}")
    
    print("\n----------------------\n")
	
	
""" OUTPUT 

Tokens for 'The old man the boats.': ['The', 'old', 'man', 'the', 'boats', '.']
Named Entities for 'The old man the boats.': []

----------------------

Tokens for 'The complex houses married and single soldiers and their families.': ['The', 'complex', 'houses', 'married', 'and', 'single', 'soldiers', 'and', 'their', 'families', '.']
Named Entities for 'The complex houses married and single soldiers and their families.': []

----------------------

Tokens for 'Mary gave the child a Band-Aid.': ['Mary', 'gave', 'the', 'child', 'a', 'Band', '-', 'Aid', '.']
Named Entities for 'Mary gave the child a Band-Aid.': [('Mary', 'PERSON')]
Explanation for 'Mary' (Entity Type: PERSON): People, including fictional

----------------------

Tokens for 'That Jill is never here hurts.': ['That', 'Jill', 'is', 'never', 'here', 'hurts', '.']
Named Entities for 'That Jill is never here hurts.': [('Jill', 'PERSON')]
Explanation for 'Jill' (Entity Type: PERSON): People, including fictional

----------------------

Tokens for 'The cotton clothing is made of grows in Mississippi.': ['The', 'cotton', 'clothing', 'is', 'made', 'of', 'grows', 'in', 'Mississippi', '.']
Named Entities for 'The cotton clothing is made of grows in Mississippi.': [('Mississippi', 'GPE')]
Explanation for 'Mississippi' (Entity Type: GPE): Countries, cities, states

----------------------

"""

"""

The old man the boats."

Named Entities: None Explanation: There are no named entities in this sentence. "The complex houses married and single soldiers and their families."

Named Entities: None Explanation: There are no named entities in this sentence. "Mary gave the child a Band-Aid."

Named Entities: [('Mary', 'PERSON')] Explanation: "PERSON" refers to a real or fictional person. In this case, "Mary" is recognized as a person. "That Jill is never here hurts."

Named Entities: [('Jill', 'PERSON')] Explanation: "PERSON" refers to a real or fictional person. In this case, "Jill" is recognized as a person. "The cotton clothing is made of grows in Mississippi."

Named Entities: [('Mississippi', 'GPE')] Explanation: "GPE" stands for geopolitical entity. In this case, "Mississippi" is recognized as a geopolitical entity.

"""


	