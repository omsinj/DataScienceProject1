import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# List of garden path sentences
gardenpathSentences = [
    "The old man the boats.",
    "The complex houses married and single soldiers and their families.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts."
]

# Process each sentence and examine spaCy's categorization
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    
    # Tokenization
    tokens = [token.text for token in doc]
    print(f"Tokens: {tokens}")

    # Named Entity Recognition
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print(f"Named Entities: {entities}")

    # Print explanations for entities
    for ent_text, ent_label in entities:
        explanation = spacy.explain(ent_label)
        if explanation is not None:
            print(f"Explanation for '{ent_label}': {explanation}")
        else:
            print(f"No explanation found for '{ent_label}'\n")
    
    print("\n")

# Explanation for entities looked up:
# 1. "GPE": Geopolitical Entity
#    Explanation: Countries, cities, and states.
#    Comment: The entity "GPE" makes sense in the context of geopolitical entities, and it correctly identifies locations such as countries, cities, and states.

# 2. "FAC": Facility
#    Explanation: Buildings, airports, highways, bridges, etc.
#    Comment: The entity "FAC" makes sense when applied to buildings, airports, highways, and other facilities. It accurately categorizes elements related to physical structures and facilities.
