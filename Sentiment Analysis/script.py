from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import os

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Step 1: Read in the text file into an array of strings
file_path = os.path.join(os.path.dirname(__file__), 'results.txt')
with open(file_path, 'r') as file:
    reviews = file.readlines()

# Step 2: Apply sentiment analysis on each review
sia = SentimentIntensityAnalyzer()
positive_reviews = 0
total_reviews = len(reviews)

for review in reviews:
    score = sia.polarity_scores(review)['compound']
    # Step 3: Output "POSITIVE" or "NEGATIVE" based on the sentiment score
    if score > 0:
        print("POSITIVE")
        positive_reviews += 1
    else:
        print("NEGATIVE")

# Step 4: Calculate and output the overall score for the product
overall_score = (positive_reviews / total_reviews) * 100
print(f"Overall Positive Review Percentage: {overall_score:.2f}%")
