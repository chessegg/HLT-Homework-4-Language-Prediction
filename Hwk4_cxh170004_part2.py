# Craig Hilby (cxh170004)

import nltk
import pickle
from nltk.util import ngrams

def compute_prob(text, uni_dict, bi_dict, v): # v = total vocabulary size
    u_test = nltk.word_tokenize(text)
    b_test = list(ngrams(u_test, 2))
    p_laplace = 1

    for bigram in b_test:
        b = bi_dict[bigram] if bigram in bi_dict else 0
        u = uni_dict[bigram[0]] if bigram[0] in uni_dict else 0
        p_laplace = p_laplace * ((b + 1) / (u + v))

    return p_laplace

if __name__ == '__main__':

    # read the pickle files
    uni_eng_dict = pickle.load(open('uni_english.p', 'rb'))
    bi_eng_dict = pickle.load(open('bi_english.p', 'rb'))

    uni_french_dict = pickle.load(open('uni_french.p', 'rb'))
    bi_french_dict = pickle.load(open('bi_french.p', 'rb'))

    uni_italian_dict = pickle.load(open('uni_italian.p', 'rb'))
    bi_italian_dict = pickle.load(open('bi_italian.p', 'rb'))

    # getting total length of vocabulary size, summing together the dict lengths of all 3 languages
    v = len(uni_eng_dict) + len(uni_french_dict) + len(uni_italian_dict)

    test_file = open('data/LangId.test', 'r')
    output_file = open('output.txt', 'w')
    line = test_file.readline()
    count = 0

    while line: # while line is not empty (line being empty signifies EOF reached)
        count += 1
        # calling compute_prob functions for laplace probability calculations on all three languages
        eng_prob = compute_prob(line, uni_eng_dict, bi_eng_dict, v)
        french_prob = compute_prob(line, uni_french_dict, bi_french_dict, v)
        italian_prob = compute_prob(line, uni_italian_dict, bi_italian_dict, v)

        #setting language to the most probable language
        if eng_prob > italian_prob and eng_prob > french_prob:
            language = 'English'
        elif italian_prob > eng_prob and italian_prob > french_prob:
            language = 'Italian'
        else:
            language = 'French'

        output_file.write(str(count) + ' ' + language + '\n')  #ie 1 Italian for the first line
        
        line = test_file.readline() #read in the next line of the file

    test_file.close()
    output_file.close()

    #Now, compare my output with the correct classifications
    output_file = open('output.txt', 'r')
    correct_langs = open('data/LangId.sol', 'r')
    output_line = output_file.readline()
    correct_line = correct_langs.readline()
    correct = 0
    total = 0
    incorrect = []

    while output_line and correct_line: #while both my output.txt file and the LangId.sol file have lines (not EOF)
        total += 1
        if output_line == correct_line:
            correct += 1
        else:
            incorrect.append(str(total) + ' ')
        output_line = output_file.readline()
        correct_line = correct_langs.readline()
        
    output_file.close()
    correct_langs.close()
    accuracy = "{:.2f}".format(correct / total)

    print('correct: ' + str(correct))
    print('total items: ' + str(total))
    print('accuracy: ' + accuracy)
    print('incorrect items: ' + ''.join(incorrect))
    


