import pandas as pd
import nltk
nltk.download('vader_lexicon')

def process_chat_data(csv_file: str):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Perform the necessary processing on the data
    conversations = df.groupby('conversation_id')

    from nltk.sentiment import SentimentIntensityAnalyzer

    sia = SentimentIntensityAnalyzer()

    for conversation_id, messages in conversations:
        sentiment = sia.polarity_scores(messages['text'].str.cat(sep=' '))
        print(f'Conversation ID: {conversation_id}, Sentiment: {sentiment}')