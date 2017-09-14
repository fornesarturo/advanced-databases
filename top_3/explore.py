import pandas as pd
import numpy as np

def histogram(iter):
    hist = {}
    for node in iter:
        if node in hist.keys():
            hist[node] += 1
        else:
            hist[node] = 1
    keyValue = zip(hist.keys(), hist.values())
    return sorted(hist, key = lambda x: hist.get(x), reverse = False)

csv = pd.read_csv("rooster_achievement.csv")
csv.plot.hist()
csvTargetHistogram = histogram(csv.Target)
csvNames = pd.read_csv("rooster_achievement_nodes.csv")
topThree = csvTargetHistogram[:3]

influentialNodes = []
for i in topThree:
    influentialNodes.append(csvNames.query('id == {}'.format(i)).label.values[0])

print(influentialNodes)
