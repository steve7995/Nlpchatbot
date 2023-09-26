import nltk
# nltk.download()



from nltk.stem import WordNetLemmatizer
from NLP.stemming import stemming
from NLP.stopwords import remove_stop_words
from NLP.tokenize import tokenize
lemmatizer = WordNetLemmatizer()

def bot_working(sentence):
    tokens_array = tokenize(sentence)
    print("step:1")
    print(tokens_array)
    print("tokenization and removal of punctuation marks done ")
    print("---------------------------------------------------")
    print("step:2")
    new_tokens = remove_stop_words(tokens_array)
    print(new_tokens)
    print("removal of stop words done ")
    print("---------------------------------------------------")
    steve = []
    for i in new_tokens:
        steve.append(lemmatizer.lemmatize(i))
    print(steve)
    print("lemmatization done")
    print("---------------------------------------------------")
    print("step:3")
    new_tokens2 = stemming(new_tokens)
    print("stemming done")
    for j in range(0,len(steve)):
        new_tokens2.append(steve[j])
    print(new_tokens2)

    print("---------------------------------------------------")





# print(bot_working(" what mobiles are there in your store ?"))
# print(bot_working(" Do you have gaming laptops ?"))

print(bot_working("Do you have gaming laptops ?"))


