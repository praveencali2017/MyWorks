from nltk.corpus import wordnet as wn


# for synset in wn.synsets('printer'):
#      print("\tLemma: {}".format(synset.name()))
#      print("\tDefinition: {}".format(synset.definition()))
#      print("\tExample: {}".format(synset.examples()))
# # print(check)
def checkwordSimilarity(word1,word2):
    word_sim = 0
    try:
        for item in word1:
            for item2 in word2:
                sim = item.path_similarity(item2)
                if sim > word_sim:
                    word_sim = sim
    except:
        print("error")
    return word_sim
word1=wn.synsets('school')
word2 =wn.synsets('schools')
print(word1)
print(word2)
print(checkwordSimilarity(word1,word2))

