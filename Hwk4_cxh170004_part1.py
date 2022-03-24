# Craig Hilby (cxh170004)

import nltk
import pickle
from nltk.util import ngrams
from collections import Counter

def build_lang(file):
    input = open(file, 'r', encoding="latin1") # open file
    raw_input = input.readlines() # read in text
    text = ''.join(line.replace('\n', ' ') for line in raw_input) # remove newlines
    
    unigrams = nltk.word_tokenize(text) #tokenized text is the list of unigrams
    bigrams = list(ngrams(unigrams, 2))
    
    #Counter is a much faster and inbuilt Python way to count occurrances and build a dict of {item : occurance}
    unigram_dict = dict(Counter(unigrams))
    bigram_dict = dict(Counter(bigrams))

    return unigram_dict, bigram_dict


if __name__ == '__main__':
    #building and pickling English unigrams and bigrams
    uni_english, bi_english = build_lang('data/LangId.train.English')
    pickle.dump(uni_english, open('uni_english.p', 'wb'))
    pickle.dump(bi_english, open('bi_english.p', 'wb'))

    #building and pickling French unigrams and bigrams
    uni_french, bi_french = build_lang('data/LangId.train.French')
    pickle.dump(uni_french, open('uni_french.p', 'wb'))
    pickle.dump(bi_french, open('bi_french.p', 'wb'))

    #building and pickling Italian unigrams and bigrams
    uni_italian, bi_italian = build_lang('data/LangId.train.Italian')
    pickle.dump(uni_italian, open('uni_italian.p', 'wb'))
    pickle.dump(bi_italian, open('bi_italian.p', 'wb'))

