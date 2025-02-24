from nltk.tokenize import word_tokenize, sent_tokenize, regexp_tokenize

# Sample text
text = "Hello, world! This is a test."

# Word Tokenization
word_tokens = word_tokenize(text)
print("Word Tokenization:", word_tokens)

# Sentence Tokenization
sent_tokens = sent_tokenize(text)
print("Sentence Tokenization:", sent_tokens)

# Whitespace Tokenization
whitespace_tokens = text.split()
print("Whitespace Tokenization:", whitespace_tokens)

# Regular Expression Tokenization
regexp_tokens = regexp_tokenize(text, pattern=r'\w+')
print("Regular Expression Tokenization:", regexp_tokens)