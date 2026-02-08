import string

infile=open('sample-file.txt','r')
texts=infile.read()
infile.close()

tokens=texts.split()# splits into tokens and stores in variable "tokens"


edited_words=[]
for token in tokens:
    token=token.lower()#makes lowercase
    token=token.strip(string.punctuation)#removes the punctuations

    count_letters=0

    for char in token:
        if char.isalpha():
            count_letters+=1 #this section counts number of alphabets in each word

    if count_letters>=2:
        edited_words.append(token)#adds to list if more than two alphabets per word

bigrams = []

for i in range(len(edited_words) - 1):
    word1 = edited_words[i]
    word2 = edited_words[i + 1]
    bigram = word1 + " " + word2
    bigrams.append(bigram)

bigram_counts = {}

for bigram in bigrams:
    if bigram in bigram_counts:
        bigram_counts[bigram] += 1
    else:
        bigram_counts[bigram] = 1

print("\nTop 5 most frequent bigrams:")

for i in range(5):
    max_bigram = None
    max_count = 0

    for bigram in bigram_counts:
        if bigram_counts[bigram] > max_count:
            max_bigram = bigram
            max_count = bigram_counts[bigram]

    if max_bigram is None:
        break

    print(max_bigram, "->", max_count)

    del bigram_counts[max_bigram]
