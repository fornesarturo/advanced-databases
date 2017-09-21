import pandas as pd
import numpy as np
import json

def fromJson(filename="words.json"):
    dic = {}
    with open(filename, 'r') as f:
        dic = json.loads(f.read())
    return dic

def toJson(dictionary, filename="words.json"):
    with open(filename, 'w') as f:
        f.write(json.dumps(dictionary))

def create_hist(filename, dictionary):
    hist = {}
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                if word in dictionary:
                    if dictionary[word] in hist.keys():
                        hist[dictionary[word]] += 1
                    else:
                        hist[dictionary[word]] = 1
                else:
                    if word in hist:
                        hist[word] += 1
                    else:
                        hist[word] = 1

    keyValue = zip(hist.keys(), hist.values())
    return dict(sorted(keyValue, key = lambda x: x[1], reverse=True))

dictionary = fromJson()

filename = "file.txt"# input("¿Dónde está el archivo?: ")
hist = create_hist(filename, dictionary)

print(hist)
