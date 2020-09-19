import spacy
import textacy.extract

nlp = spacy.load('en_core_web_lg')

text = """London is the capital and most populous city of England and 
the United Kingdom.  Standing on the River Thames in the south east 
of the island of Great Britain, London has been a major settlement 
for two millennia. It was founded by the Romans, who named it Londinium.
"""

doc = nlp(text)

for entity in doc.ents:
    print(f"{entity.text} ({entity.label_})")

statements = textacy.extract.semistructured_statements(doc, "London")

print("Facts about London:")

for statement in statements:
    subject, verb, fact = statement
    print(f" - {fact}")