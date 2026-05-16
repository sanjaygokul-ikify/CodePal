import os
import json
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from src.core import CodeAnalyzer

def main():
    # Load configuration
    with open('config.json') as f:
        config = json.load(f)

    # Initialize the AI engine
    model = AutoModelForSequenceClassification.from_pretrained(config['model_name'])
    tokenizer = AutoTokenizer.from_pretrained(config['tokenizer_name'])

    # Create a CodeAnalyzer instance
    analyzer = CodeAnalyzer(model, tokenizer)

    # Analyze code and provide feedback
    code = input('Enter your code: ')
    feedback = analyzer.analyze_code(code)
    print(feedback)

if __name__ == '__main__':
    main()
