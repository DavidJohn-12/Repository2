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

    word_count={}

    for word in edited_words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1

for i in range(10):
    max_word = None
    max_count = 0

    for word in word_count:
        if word_count[word] > max_count:
            max_word = word
            max_count = word_count[word] # find the word with the highest count

    # stop if dictionary becomes empty
    if max_word is None:
            break

    print(max_word, "->", max_count)

    del word_count[max_word]# remove the word so it won't be chosen again in the 10 range






