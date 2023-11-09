import spacy

# Load the 'en_core_web_md' model
nlp = spacy.load('en_core_web_md')

# Create spaCy Doc objects for the words 'cat,' 'monkey,' and 'banana'
cat = nlp('cat')
monkey = nlp('monkey')
banana = nlp('banana')

# Calculate and print the similarity scores between these words
print("Similarity between 'cat' and 'monkey':", cat.similarity(monkey))
print("Similarity between 'banana' and 'monkey':", banana.similarity(monkey))
print("Similarity between 'banana' and 'cat':", banana.similarity(cat))

# Tokenize the input text 'cat apple monkey banana'
input_text = 'cat apple monkey banana'
input_doc = nlp(input_text)

# Iterate through the tokens and calculate the similarity between all token pairs
print("Similarity scores between all token pairs in the input text:")
for token1 in input_doc:
    for token2 in input_doc:
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

# Tokenize the model sentence
model_sentence_doc = nlp(model_sentence)

# Iterate through the list of sentences to compare and calculate similarity
print("Similarity between the model sentence and each sentence in the list:")
for sentence in sentences_to_compare:
    sentence_doc = nlp(sentence)
    similarity_score = model_sentence_doc.similarity(sentence_doc)
    print(f"{model_sentence} - {sentence}: {similarity_score}")
