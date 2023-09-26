import nltk
import random
import string
import warnings

from NLP.findID import findId
from NLP.prepro import pre_pro
from NLP.stemming import stemming

warnings.filterwarnings('ignore')

Maxie_INPUTS = [["hello", "hi",
                 "greetings", "hey",
                 "how are you",
                 "Is anyone there?",
                 "Hello",
                 "Good day"
                 ],

                ["Which items do you have?",
                 "What kinds of items are there?",
                 "What do you sell?", "items",
                 "kinds of items",
                 "sell",
                 "product",
                 "products"],

                ["credit card", "Mastercard",
                 "can I pay with Paypal",
                 "Are you cash only?",
                 "payment",
                 "pay", "paypal",
                 "phonepe", "paytm"],

                ["delivery",
                 "shipping",
                 "deliver",
                 "long",
                 ],

                ["brands",
                 "company",
                 "companies"],

                ["laptop","pc","games",
                 "gaming"],

                ["mobile","smartphone","iphone","realme",
                 "samsung","redmi"],

                ["dslr","nikon","lumix",
                 "canon","lens","drones"],

                ["customer-care",
                 "contact",
                 "support",
                 "customer-service",
                 "service"],

                ["idiots",
                 "bad",
                 "sad",
                 "not good"],

                ["funny",
                 "joke","laugh","smile"]
                ]

Maxie_RESPONSES = [["hi", "hey", "nods", "hi there", "Hello, thanks for visiting",
                    "Hi there, what can I do for you?",
                    "Hi there, how can I help?",
                    "Happy to help!",
                    "Any time!",
                    "My pleasure", "hey there",
                    "let's go", "hey dude",
                    "goodmorning",
                    "goodevening",
                    "good afternoon"
                    ],

                   ["Laptops, smartphones, cameras,graphic cards,processors,smartphone gadgets "
                    "and all other electronic products",
                    "We sell all kind of electronic gadgets",
                    "We have all kind of electric articles from different brands"
                    ],

                   ["We accept VISA, Mastercard and Paypal",
                    "We accept most major credit cards, and Paypal",
                    "we also take payment through upi"],

                   ["Delivery takes 2-4 days",
                    "Shipping takes 2-4 days"],

                   ["apple, samsung, asus,lenovo, hp, dell, msi,nvidia, canon, nikon, lumix"],

                   [" we have allkind of gaming laptops","we have ps5 and xbox one ",
                    " we have latest graphic cards like rtx 3060 ,rtx 4090 "],

                   [" we have all the latest models of android and iphones,"
                    "we sell all the models you want at the best price ",
                    "we have both 4gb ram models and 6gb ram models"],

                   ["we have all kind of dslr and mirror-less cameras along with "
                    "the lens at the best price available in the market"],

                   ["contact our mail ihub@gmail.com",
                    "contact our customer care at 133-444-1945"],

                   ["sorry", "sorry for this condition","we are really sorry for you please contact our customer care",
                    "sorry for the inconvenience please mail at ihub@gmail.com "],

                   [ "Why did the hipster burn his mouth? He drank the coffee before it was cool.",
                     "What did the buffalo say when his son left for college? Bison."]
                   ]


def Maxie(sentence):
    Fial_Words = pre_pro(sentence)
    for i in range(0, len(Fial_Words)):
        for j in range(0, len(Maxie_INPUTS)):
            if Fial_Words[i].lower() in Maxie_INPUTS[j]:
                return random.choice(Maxie_RESPONSES[j])




def MAX():
    flag = True
    print("Hello, I'm max ,welcome to ihub. i am there to answer all of your queries , If you want to exit, type Bye!")
    while flag == True:
        user_response = input()
        user_response = user_response.lower()
        if user_response != 'bye':
            if user_response == 'thanks' or user_response == 'thank you':
                flag = False
                print("max: You're welcome!")
            else:
                if Maxie(user_response) != None:
                    print("max:" + Maxie(user_response))

        else:
            flag = False
            print("max: Bye! Have a great day!")


MAX();

# print(pre_pro("which products do you have ?"))
# print(pre_pro("which products do you have ?"))