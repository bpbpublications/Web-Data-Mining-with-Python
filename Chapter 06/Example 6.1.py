import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import sent_tokenize
txt = "I love watching movies. I and my friends love eating popcorn and snacks while watching Movie."
tokenized = sent_tokenize(txt)
print(tokenized)
