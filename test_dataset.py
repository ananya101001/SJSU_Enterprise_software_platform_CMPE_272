import pandas as pd
from sentiment_analysis import analyze_sentiment

# Absolute path to your CSV file
dataset_file = 'sentiment_analysis.csv'

encodings = ['utf-8', 'latin1', 'iso-8859-1', 'utf-16']

for encoding in encodings:
    try:
        data = pd.read_csv(dataset_file, encoding=encoding)
        print(f"Successfully read the file with encoding: {encoding}")
        dataset_path = 'sentiment_analysis.csv' 
        df = pd.read_csv(dataset_file, encoding=encoding)

        if 'text' not in df.columns:
            print("The dataset does not contain a 'text' column.")
            break
        df['text'] = df['text'].astype(str)

        df['NEW_Sentiment'] = df['text'].apply(analyze_sentiment)
        print(df.head())  
        df.to_csv('sentiment_analysis_results.csv', index=False)
        print(data.head())  # Print the first few rows to verify
        break
    except UnicodeDecodeError:
        print(f"Encoding {encoding} failed.")
    except Exception as e:
        print(f"An error occurred: {e}")


    


   