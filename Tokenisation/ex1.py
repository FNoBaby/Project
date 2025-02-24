import nltk
import matplotlib.pyplot as plt

input = " The term domestic dog refers to any of several hundred breeds of dog in the world today. While these animals vary drastically in appearance, every dog from the Chihuahua to the Great Dane—is a member of the same species, Canis familiaris. This separates domestic dogs from wild canines, such as coyotes, foxes, and wolves."

print(input)

tokens = input.split()

freq = nltk.FreqDist(tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))
    
freq.plot(20, cumulative=False)
plt.show()  # Ensure the plot is displayed
# 20 refers to number of gridlines along the x axis
