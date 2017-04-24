import difflib

sentences=["latest categories","my events",
           "get all my tags","all my feeds","new groups"]
user_query="what are my category?"
prob=[]
for sentence in sentences:
    seq = difflib.SequenceMatcher(a=user_query.lower(), b=sentence.lower())
    prob.append(seq.ratio())

print(prob)