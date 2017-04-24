from gensim import models
from gensim.models import Doc2Vec
from gensim.models.doc2vec import LabeledSentence
from collections import namedtuple
import gensim.models.doc2vec
doc1=["latest categories","my events",
           "get all my tags","all my feeds","new groups"]
LabeledSentence()
# Load data

# doc1 = ["This is a sentence", "This is another sentence"]

# Transform data (you can add more data preprocessing steps)

docs = []
analyzedDocument = namedtuple('AnalyzedDocument', 'words tags')
for i, text in enumerate(doc1):
    words = text.lower().split()
    tags = [i]
    docs.append(analyzedDocument(words, tags))

# Train model (set min_count = 1, if you want the model to work with the provided example data set)

model = Doc2Vec(docs, size = 100, window = 300, min_count = 1, workers = 4)

# Get the vectors
print(model.docvecs[0])
print(model.docvecs[1])
