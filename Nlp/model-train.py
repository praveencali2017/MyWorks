from gensim import models
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from collections import namedtuple
import gensim.models.doc2vec
sources = ("latest categories","my events",
           "get all my tags","all my feeds","new groups")
documents = gensim.models.doc2vec.TaggedLineDocument(sources)
model = gensim.models.doc2vec.Doc2Vec(dm=0, # DBOW
				size=400,
				window=8,
				min_count=5,
				dbow_words = 1) # DBOW, simultaneously train word vectors with doc vectors

# build model
model.build_vocab(documents)
# train model
model.train(documents)
# save
model.save('model-custom-corpus-en')

model = gensim.models.doc2vec.Doc2Vec.load('model-law-corpus-en')

st = 'group'

new_doc_vec = model.infer_vector(st)

print(model.docvecs.most_similar([new_doc_vec]))