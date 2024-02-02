Find at least 2 garden path sentences. 
Store the sentences in a list called gardenpathSentences.
gardenpathSentences = [
    "The old man the boats.",
    "The complex houses married and single soldiers and their families."
]

Add the following sentences to the list
Mary gave the child a Band-Aid
That Jill is never here hurts
The cotton clothing is made of grows in Mississippi

gardenpathSentences = [
    "The old man the boats.",
    "The complex houses married and single soldiers and their families.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts."
]

Tokenise each sentence in the list, and perform named entity recognition.

pip install spacy
python -m spacy download en_core_web_sm
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

# Tokenize and perform named entity recognition for each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    
    # Tokenization
    tokens = [token.text for token in doc]
    print(f"Tokens: {tokens}")

    # Named Entity Recognition
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print(f"Named Entities: {entities}\n")


Examine how spaCy has categorised each sentence. Then use spacy.explain to look up and print the meaning of entities that you dont understand. For example: print(space.explain("FAC"))
# Process each sentence and examine spaCy's categorisation

# Process each sentence using spaCy
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    
    # Print spaCy's categorization
    print(f"Original Sentence: {sentence}")
    print("Categorization:")
    for token in doc:
        print(f"{token.text}: {token.pos_} ({spacy.explain(token.pos_)})")
    
    # Perform Named Entity Recognition (NER)
    print("\nNamed Entity Recognition (NER):")
    for ent in doc.ents:
        print(f"{ent.text}: {ent.label_} ({spacy.explain(ent.label_)})")
    
    print("\n" + "="*50 + "\n")

    
""" Additional Notes:

AT the bottome of your file, write a comment about two entities that you looked up. For each entity answer the following questions:

    
1. 'LAW' Entity:
What was the entity and its explanation that you looked up?
The entity 'LAW' represents legal document titles or law-specific terms.

- Why is it relevant?
This entity is relevant when spaCy identifies mentions related to laws, legal documents, or specific legal terminology.

2. 'NORP' Entity:
- What was the entity and its explanation that you looked up?
The entity 'NORP' stands for "Nationalities or religious or political groups."

- Why is it relevant?
This entity is relevant when spaCy identifies mentions of nationalities, religious affiliations, or political groups in the text.

"""
