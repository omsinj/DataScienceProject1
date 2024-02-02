""" Before running the code below, we need to install spacey using the command: pip install spacy

Once pip spacy is installed, we download the English model, using the command: python -m spacy download en_core_web_sm

Follow the code below

"""


# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Task 1- Initial selection

gardenpathSentences = [
    "The old man the boats.",
    "The complex houses married and single soldiers and their families."
]


# Task 2 - Full List of garden path sentences
gardenpathSentences = [
    "The old man the boats.",
    "The complex houses married and single soldiers and their families.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    " The cotton clothing is made of grows in Missippi.
]

# Task 3 Process each sentence, examine spaCy's categorisation and perform named entity recognition.

# Process each sentence using spaCy
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    
    # Print spaCy's categorisation
    print(f"Original Sentence: {sentence}")
    print("Categorisation:")
    for token in doc:
        print(f"{token.text}: {token.pos_}")
    
    # Perform Named Entity Recognition (NER)
    print("Named Entity Recognition (NER):")
    for ent in doc.ents:
        print(f"{ent.text}: {ent.label_}")
    
    print("\n" + "="*50 + "\n")

    
""" Additional Notes:

AT the bottome of your file, write a comment about two entities that you looked up. For each entity answer the following questions:

    
1. 'LAW' Entity:
- What was the entity and its explanation that you looked up?
The entity 'LAW' represents legal document titles or law-specific terms.

- Why is it relevant?
This entity is relevant when spaCy identifies mentions related to laws, legal documents, or specific legal terminology.

2. 'NORP' Entity:
- What was the entity and its explanation that you looked up?
The entity 'NORP' stands for "Nationalities or religious or political groups."

- Why is it relevant?
This entity is relevant when spaCy identifies mentions of nationalities, religious affiliations, or political groups in the text.

"""
