
def removesuffix(self: str, suffix: str, /) -> str:

    if suffix and self.endswith(suffix):
        return self[:-len(suffix)]
    else:
        return self[:]



def stemming(a):
    stem_words = ['ing', "y","s", "tion","ed","tions","ors","able "]
    for i in range(0, len(a)):
        for j in range(0, len(stem_words)):
            if a[i].endswith(stem_words[j]):
                new = (removesuffix(a[i], stem_words[j]))
                a[i] = new
    return a


print(stemming(["interesting" , "finally" ,"perception"]))