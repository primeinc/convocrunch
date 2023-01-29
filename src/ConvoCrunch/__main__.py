import argparse
from .chat_processor import process_chat_data

def main():
    parser = argparse.ArgumentParser(description='Process chat data.')
    parser.add_argument('csv_file', type=str, help='The path to the CSV file containing the chat data.')
    args = parser.parse_args()

    process_chat_data(args.csv_file)
