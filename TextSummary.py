import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.kl import KLSummarizer
import itertools
from googlesearch import search

text = "deep.srt"

#to convet from srt to text format
def txt(srt_file):
    file = open( "deep.srt", "r")
    lines = file.readlines()
    file.close()

    text = ''
    for line in lines:
        if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
            text += ' ' + line.rstrip('\n')
        text = text.lstrip()
    #print(text)
    return text

text = txt(text)

#Loading the english stop words (a, the, and, like etc etc)
stopwords = list(STOP_WORDS)

#This is the model for tokenizing words, i haven't dug deep in this
#but at looking at the outputs I found it is just tokenizing the words
#It is a comprehensive model for tokenizing into words as well as sentences

nlp = spacy.load('en_core_web_sm')

doc = nlp(text)

tokens = [token.text for token in doc]
#print(tokens)

#by looking at the punctuations i found new line wasn't added as punctuation so i added
punctuation = punctuation + '\n'
#print(punctuation)

#Just counting the word freq from the article
#Ignoring punctuations and stopwords
#And storing them in dictionary
word_freq = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1


sort_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

query = ''
for i in sort_freq[:3]:
    query += i[0]
    query += ' '
print("The top 3 most frequent words are : ")
print(query)


# to return relevant content available online
query2 = query + "notes"
query3 = query + "formulas and equation"
query4 = query + "examples and questions"

print("Top Results for the Topic : ")
for j in search(query, tld="co.in", num=2, stop=2, pause=2):
    print(j)
print("Top Results for the Notes related to Topic : ")
for j in search(query2, tld="co.in", num=2, stop=2, pause=2):
    print(j)
print("Top Results for the Equations or Formulae for the Topic : ")
for j in search(query3, tld="co.in", num=2, stop=2, pause=2):
    print(j)
print("Top Results for the Examples relevant to the Topic : ")
for j in search(query4, tld="co.in", num=2, stop=2, pause=2):
    print(j)



def summarize_using_KL(text_file, n_sentences = 20, language="english"):

    parser = PlaintextParser.from_string(
        text_file, Tokenizer(language))
    stemmer = Stemmer(language)
    summarizer = KLSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)
    summary = summarizer(parser.document, n_sentences)
    return summary

summary =  summarize_using_KL(text)
out = list(itertools.chain(summary))
#print(type(summary_2))
final_summary = []
for elem in out:
        final_summary.append(elem)
        #print(elem)

print("Summary (list) using KLSummarizer : ")
print(final_summary)