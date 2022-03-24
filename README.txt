This is Homework 4 from CS 4395 Human Language Technologies (Natural Language Processing).

The instructions for the assignment can be found in the homework_4_ngram_INSTRUCTIONS.pdf file.

The basic gist of the project is that we use NLP (specifically, NLTK) to create unigram and bigram dictionaries
for English, French, and Italian using provided training data. We then use these dictionaries to calculate
probabilities that each sentence is a certain language in the test data.

TO RUN THIS PROJECT:
Open command prompt and go to the directory with all of the files and py scripts. Then run:

python Hwk4_cxh170004_part1.py

(This will create the dictionaries. Then to calculate probabilities of the test data, run:)

python Hwk4_cxh170004_part2.py


To view results, open the output.txt file that was written during runtime. The actual sentences in the test
data can be viewed in the data/LangId.test text file.