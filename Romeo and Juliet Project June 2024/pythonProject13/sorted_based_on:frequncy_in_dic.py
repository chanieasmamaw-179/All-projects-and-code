from string import punctuation
from operator import itemgetter

txt = "what if the values, are equal? If the values are equal, is there a way to sort them in respect to their length instead?"

N = 100
words = {}

words_gen = (words	.strip(punctuation).lower()
for line in txt:
for word in txt.split()

for word in words_gen:
    words[word] = words.get(word, 0) + 1

top_words = sorted(words.items(), key=itemgetter(1), reverse=True)[:N]

for word, frequency in top_words:
    print ("%s %d" % (word, frequency))