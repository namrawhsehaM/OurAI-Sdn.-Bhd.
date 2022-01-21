
import json
import random
import json
import os

import torch
from model import *
from nltk_utils import bag_of_words, tokenize
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

from utility import openn
from utility import searching
from utility import setusername


def answer(tag, query):
    if tag == "open":
        result = openn(query)
        return result
    elif tag == "SetUserName":
        setusername()
    elif tag == "Search":
        print("searching")
        result = searching(query)
        # print(result)
        return result
    else:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{random.choice(intent['responses'])}")
                return (f"{random.choice(intent['responses'])}")
