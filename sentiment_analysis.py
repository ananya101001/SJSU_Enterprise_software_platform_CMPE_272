from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"
    

texts = [
        "I Like Enterprise Software Course",
        "I hate this fall. It's too sunny today",
        "It's okay, we all can complete assignments by deadline !",
    ]

for text in texts:
        print(f"Text: {text}")
        print(f"Sentiment: --  {analyze_sentiment(text)}")
        print('------------')    

if __name__ == "__main__":
    text = input("Enter a text string for sentiment analysis: ")
    sentiment = analyze_sentiment(text)
    print(f"The sentiment of the text is: {sentiment}")
