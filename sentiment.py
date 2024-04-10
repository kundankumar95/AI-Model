from textblob import TextBlob
with open('Backend\\Features\\sentiment.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
print(text)
sentiment = blob.sentiment.polarity  # -1 to 1
print(sentiment)