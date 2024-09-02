from sentiment_analysis import analyze_sentiment

def run_tests():
    assert analyze_sentiment("I love this product! It's amazing.") == "Positive"
    assert analyze_sentiment("I hate this product. It's terrible.") == "Negative"
    assert analyze_sentiment("This product is okay.") == "Neutral"
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
