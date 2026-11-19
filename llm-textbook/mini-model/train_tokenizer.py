"""Train our teaching tokenizer. Standard library only. Does not train an LLM."""
from collections import Counter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
samples = ROOT.joinpath('corpus.txt').read_text().splitlines()
assert len(' '.join(samples).split()) == 50
vocab = {i: bytes([i]) for i in range(256)}
sequences = [list(text.encode()) for text in samples]
merges = []

def counts():
    return Counter((a,b) for seq in sequences for a,b in zip(seq,seq[1:]))

def replace(seq, a, b, new):
    result=[]; i=0
    while i<len(seq):
        if i+1<len(seq) and seq[i]==a and seq[i+1]==b:
            result.append(new); i+=2
        else:
            result.append(seq[i]); i+=1
    return result

def snapshot():
    return dict(sequences=sequences, pieces=[[vocab[i].decode() for i in seq] for seq in sequences],
                tokenCount=sum(map(len,sequences)), vocabularySize=len(vocab),
                candidates=[dict(left=vocab[a].decode(),right=vocab[b].decode(),count=n)
                            for (a,b),n in counts().most_common(5)],
                learned=[dict(id=i,text=vocab[i].decode()) for i in range(256,len(vocab))])

stages=[snapshot()]
for _ in range(16):
    if not counts(): break
    (a,b),frequency=counts().most_common(1)[0]
    new=len(vocab); vocab[new]=vocab[a]+vocab[b]
    merges.append(dict(left=a,right=b,id=new,frequency=frequency))
    sequences=[replace(seq,a,b,new) for seq in sequences]
    for text,seq in zip(samples,sequences):
        assert b''.join(vocab[i] for i in seq).decode()==text
    stages.append(snapshot())

# A saved tokenizer must reproduce the training encoding using the ordered rules.
for text,expected in zip(samples,sequences):
    encoded=list(text.encode())
    for m in merges: encoded=replace(encoded,m['left'],m['right'],m['id'])
    assert encoded==expected

data=dict(samples=samples,wordCount=50,uniqueWords=len(set(' '.join(samples).split())),stages=stages)
ROOT.joinpath('training-stages.json').write_text(json.dumps(data,indent=2)+'\n')
ROOT.joinpath('tokenizer.json').write_text(json.dumps(dict(base='byte IDs 0 through 255',merges=merges,addedVocabulary={i:list(vocab[i]) for i in range(256,len(vocab))}),indent=2)+'\n')
print(json.dumps(dict(words=data['wordCount'],uniqueWords=data['uniqueWords'],sentences=len(samples),initialTokens=stages[0]['tokenCount'],finalTokens=stages[-1]['tokenCount'],vocabulary=len(vocab),firstMerge=stages[1]['learned'][0],checks='all stages decode exactly; saved rules reproduce final encodings')))
