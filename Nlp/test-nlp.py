from gensim import corpora, models, similarities

import nltk
# '''Comment after first run'''
# sentences=["latest categories","my events",
#            "get all my tags","all my feeds","new groups"]
# tokenized=[]
# for sentence in sentences:
#     tokenized.append(nltk.word_tokenize(sentence))
#
# print(tokenized)
# """Create corpus and dictionary"""
# dictionary=corpora.Dictionary(tokenized)
# dictionary.save("custom-dict.dict")
# print(dictionary.token2id)
# corpus=[dictionary.doc2bow(text) for  text in tokenized]
# corpora.MmCorpus.serialize("meetup.mm",corpus)
# print(corpus)

'''
After first run( after creating mm and dict)
'''
dictionary=corpora.Dictionary.load("custom-dict.dict")
corpus=corpora.MmCorpus("meetup.mm")

# print(corpus)

lsi=models.LsiModel(corpus,id2word=dictionary,num_topics=7)

user_query="latest categories"
vec_bow=dictionary.doc2bow(user_query.lower().split())
vec_lsi=lsi[vec_bow]
# print(vec_lsi)

#user_query="latest categories"
#new_vec=dictionary.doc2bow(user_query.lower().split())
# print(new_vec)

# index = similarities.MatrixSimilarity(lsi[corpus])
# index.save('meetup.index')
index=similarities.MatrixSimilarity.load("meetup.index")
sims = index[vec_lsi]

# sims=index[vec_lsi]
# print(list(enumerate(sims)))
# sims = sorted(enumerate(sims), key=lambda item: -item[1])
print(list(enumerate(sims)))
