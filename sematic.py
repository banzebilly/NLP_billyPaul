import spacy

# Load the 'en_core_web_md' model
nlp_md = spacy.load('en_core_web_md')

# Load the 'en_core_web_sm' model
nlp_sm = spacy.load('en_core_web_sm')

# Create spaCy Doc objects for the words 'cat,' 'monkey,' and 'banana'
cat = nlp_md('cat')
monkey = nlp_md('monkey')
banana = nlp_md('banana')

# Calculate and print the similarity scores between these words using the medium model
print("Similarity between 'cat' and 'monkey' (md):", cat.similarity(monkey))
print("Similarity between 'banana' and 'monkey' (md):", banana.similarity(monkey))
print("Similarity between 'banana' and 'cat' (md):", banana.similarity(cat))

# Calculate and print the similarity scores between these words using the small model
cat_sm = nlp_sm('cat')
monkey_sm = nlp_sm('monkey')
banana_sm = nlp_sm('banana')
print("\nSimilarity between 'cat' and 'monkey' (sm):", cat_sm.similarity(monkey_sm))
print("Similarity between 'banana' and 'monkey' (sm):", banana_sm.similarity(monkey_sm))
print("Similarity between 'banana' and 'cat' (sm):", banana_sm.similarity(cat_sm))

# Tokenize the input text 'cat apple monkey banana' using the medium model
input_text_md = 'cat apple monkey banana'
input_doc_md = nlp_md(input_text_md)

# Tokenize the input text 'cat apple monkey banana' using the small model
input_text_sm = 'cat apple monkey banana'
input_doc_sm = nlp_sm(input_text_sm)

# Iterate through the tokens and calculate the similarity between all token pairs using the medium model
print("\nSimilarity scores between all token pairs in the input text (md):")
for token1 in input_doc_md:
    for token2 in input_doc_md:
        if token1 != token2:
            similarity_score = token1.similarity(token2)
            print(f"{token1.text} - {token2.text}: {similarity_score}")

# Iterate through the tokens and calculate the similarity between all token pairs using the small model
print("\nSimilarity scores between all token pairs in the input text (sm):")
for token1 in input_doc_sm:
    for token2 in input_doc_sm:
        if token1 != token2:
            similarity_score = token1.similarity(token2)
            print(f"{token1.text} - {token2.text}: {similarity_score}")

# Define the model sentence to compare
model_sentence = "Why is my cat on the car."

# Create a list of sentences to compare with
sentences_to_compare = [
    "My cat is sleeping on the couch.",
    "I don't have a cat, but I have a dog.",
    "Banana and monkey are in the tree."
]

# Tokenize the model sentence using the medium model
model_sentence_doc_md = nlp_md(model_sentence)

# Tokenize the model sentence using the small model
model_sentence_doc_sm = nlp_sm(model_sentence)

# Iterate through the list of sentences to compare and calculate similarity using the medium model
print("\nSimilarity between the model sentence and each sentence in the list (md):")
for sentence in sentences_to_compare:
    sentence_doc = nlp_md(sentence)
    similarity_score = model_sentence_doc_md.similarity(sentence_doc)
    print(f"{model_sentence} - {sentence}: {similarity_score}")

# Iterate through the list of sentences to compare and calculate similarity using the small model
print("\nSimilarity between the model sentence and each sentence in the list (sm):")
for sentence in sentences_to_compare:
    sentence_doc = nlp_sm(sentence)
    similarity_score = model_sentence_doc_sm.similarity(sentence_doc)
    print(f"{model_sentence} - {sentence}: {similarity_score}")

# Observations:
# - Similarity scores may vary between the medium and small models.
# - Larger models generally capture more nuanced relationships between words.
# - In some cases, the small model may provide reasonable similarity scores.
# - The choice of model depends on the specific use case and available resources.

