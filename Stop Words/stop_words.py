import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

input = " The term domestic dog refers to any of several hundred breeds of dog in the world today. While these animals vary drastically in appearance, every dog from the Chihuahua to the Great Dane—is a member of the same species, Canis familiaris. This separates domestic dogs from wild canines, such as coyotes, foxes, and wolves."

print(input)

print(stopwords.words('english'))

tokens = input.split()

# Remove stopwords and handle case sensitivity
clean_tokens = [token.lower() for token in tokens if token.lower() not in stopwords.words('english')]

freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))
    
freq.plot(20, cumulative=False)
plt.show()  # Ensure the plot is displayed

# Simple text summary with the most frequent word
most_common_word = freq.max()
print(f"The text is about: {most_common_word}")

