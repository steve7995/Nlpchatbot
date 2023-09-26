from NLP.stemming import stemming
from NLP.stopwords import remove_stop_words
from NLP.tokenize import tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# we are doing tokenization
# we are doing removal of punctuation marks
# we are doing stemming and lemmatization
def pre_pro(str):
    # the array we get after tokenization
    t_arr = tokenize(str)
    t_arr = remove_stop_words(t_arr)
    steve = []
    for i in t_arr:
        steve.append(lemmatizer.lemmatize(i))
    t_arr = stemming(t_arr)

    for j in steve:
        t_arr.append(j)
    return t_arr




print(pre_pro("what products do you have ?"))