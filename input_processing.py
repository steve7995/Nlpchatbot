from NLP.prepro import pre_pro
from NLP.tokenize import tokenize
l= ["hello", "hi", "greetings", "hey", "how are you", "good-day"]
new_l=[]
for w in l:
    tokenize(w)
    new_l.extend(w)
print(new_l)

# def maxie_input_pro(list):
#     pass



