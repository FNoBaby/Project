
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download necessary NLTK data
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')

# Text to process
text = "I am going on mountains. I will climb till I can’t no more."

# Tokenise the text
tokens = word_tokenize(text)

# Normalise the cases
tokens = [token.lower() for token in tokens]

# Remove stop words
stop_words = set(stopwords.words('english'))
tokens = [token for token in tokens if token not in stop_words]

# Tag each token with its appropriate parts of speech tag
pos_tags = nltk.pos_tag(tokens)
print("POS Tags:", pos_tags)

# Stemming using Porter Stemmer
porter = PorterStemmer()
print("\nStemming:")
for token in tokens:
    stemmed_token = porter.stem(token)
    print(token + " -> " + stemmed_token)

# Function to map POS tags to WordNet format
def get_part_of_speech_tags(token):
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    tag = nltk.pos_tag([token])[0][1][0].upper()
    return tag_dict.get(tag, wordnet.NOUN)

# Lemmatisation using WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()
print("\nLemmatisation:")
for token in tokens:
    lemmatised_token = lemmatizer.lemmatize(token, get_part_of_speech_tags(token))
    print(token + " -> " + lemmatised_token)
