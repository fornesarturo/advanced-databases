def connections(iter):
    hist = {}
    for node in iter:
        if node in hist.keys():
            hist[node] += 1
        else:
            hist[node] = 1
    return hist

def getOrder(dictionary):
    return sorted(dictionary, key = lambda x: dictionary.get(x), reverse = False)

def getOrderAsDict(dictionary):
    keyValue = zip(dictionary.keys(), dictionary.values())
    return sorted(keyValue, key = lambda x: x[1], reverse =True)

def gaussFilter(x, mean, sigma):
    """
    gaussFilter

    Receives:
        x - the value of which to calculate the probability.
        mean - the mean of the distribution.
        sigma - the standard deviation of the distribution.

    Returns:
        float - The probability of x in the given distribution
    """
    return 1 / (math.sqrt(2 * math.pi) * sigma) * math.exp(-((mean - x) ** 2) / (2 * sigma ** 2))

def filter(dictionary, iter, centerAround=None, outlierValue=4, debug=False):
    """
    filter

    Receives:
        dictionary - The dictionary containing an ID and the value asociated to it.
        centerAround - A custom input of the mean of the distribution.
        iter - The values of the distribution.
        debug - Debug mode.

    Returns:
        Implicitly modifies the given dictionary by taking out the outliers.
        list - The entries in the data that were removed by the filter, the outliers.
    """
    if not centerAround:
        m = stat.mean(iter)
    else:
        m = centerAround
    sigma = stat.stdev(iter)
    outlierLimit = gaussFilter(outlierValue, m, sigma)
    if debug:
        print("Mean: " + str(m) + " StdDev: " + str(sigma))
        print("Outlier limit: " + str(outlierLimit))
    outliers = []
    for key in dictionary.keys():
        if(gaussFilter(dictionary[key], m, sigma) < outlierLimit):
            outliers.append(key)
    for outlier in outliers:
        del dictionary[outlier]
    return outliers

nodes = pd.read_csv("rooster_teeth_Nodes.csv")
csvNames = pd.read_csv("depth_2_the_national_Nodes.csv")
nationalDictionary = connections(csv.Target)

originalSize = len(nationalDictionary)

outliers = filter(dictionary=nationalDictionary, centerAround=31, iter=nationalDictionary.values(), debug=True)
print("Deleted " + str(len(outliers)) + " items from the data.\nOriginal data contained " + str(originalSize) + " items.")
print("Dictionary is now of length: " + str(len(nationalDictionary)))
orderedDictionary = getOrderAsDict(nationalDictionary)

influentialNodes = []
for i in orderedDictionary:
    influentialNodes.append((csvNames.query('id == {}'.format(i[0])).label.values[0], i[1]))
