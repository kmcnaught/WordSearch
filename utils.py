from sympound import sympound
from jellyfish import levenshtein_distance

# A python package for performing word lookups in a dictionary


class DictionaryLookup(object):
    def __init__(self, dictionary_pkl):

        distancefun = levenshtein_distance
        self.ssc = sympound(distancefun=distancefun,
                            maxDictionaryEditDistance=100)
        self.ssc.load_pickle(dictionary_pkl)

    def lookup(self, word, max_distance=4):
        for s in self.ssc.lookup(word, 2, edit_distance_max=max_distance):
            print(s)

        return None
