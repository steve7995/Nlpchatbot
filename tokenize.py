from NLP.stemming import stemming


# we are doing both tokenization and removal of punctuation


def tokenize(str):
    tokenization_arr = str.split()
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in range(0, len(tokenization_arr)):
        if tokenization_arr[i] in punc:
            tokenization_arr[i] = " "
            tokenization_arr.remove(tokenization_arr[i])

    return tokenization_arr


# print(tokenize(" hi i am abhi"))
