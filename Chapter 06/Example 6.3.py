import nltk 

from nltk.tokenize import word_tokenize, sent_tokenize 
txt = "I love watching movies. Me and my friends love eating popcorn and snacks while watching the movie."
    
tokenized = sent_tokenize(txt) 
for i in tokenized: 
  wordsList = nltk.word_tokenize(i)
  tagged = nltk.pos_tag(wordsList) 
  print(tagged)
