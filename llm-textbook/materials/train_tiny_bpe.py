"""A tiny byte-level BPE training example; IDs are ours, not cl100k_base IDs."""
from collections import Counter
import json
from pathlib import Path

samples = ['cat', 'cat', 'car']
vocabulary = {i: bytes([i]) for i in range(256)}
sequences = [list(s.encode('utf-8')) for s in samples]
stages = []

def snapshot(added=None):
    pairs = Counter((a,b) for seq in sequences for a,b in zip(seq,seq[1:]))
    return {'sequences': [list(s) for s in sequences], 'pieces': [[vocabulary[i].decode() for i in s] for s in sequences],
            'vocabularySize': len(vocabulary), 'added': added,
            'pairs': [{'left': vocabulary[a].decode(), 'right': vocabulary[b].decode(), 'count': n} for (a,b),n in pairs.most_common()],
            'entries': [{'id': i, 'piece': vocabulary[i].decode()} for i in [97,99,114,116]+list(range(256,len(vocabulary)))]}
stages.append(snapshot())
for _ in range(2):
    counts = Counter((a,b) for seq in sequences for a,b in zip(seq,seq[1:]))
    (a,b), count = counts.most_common(1)[0]
    new_id = len(vocabulary)
    vocabulary[new_id] = vocabulary[a] + vocabulary[b]
    updated = []
    for seq in sequences:
        out=[]; i=0
        while i<len(seq):
            if i+1<len(seq) and seq[i]==a and seq[i+1]==b:
                out.append(new_id); i+=2
            else:
                out.append(seq[i]); i+=1
        updated.append(out)
    sequences=updated
    stages.append(snapshot({'left':vocabulary[a].decode(),'right':vocabulary[b].decode(),'id':new_id,'piece':vocabulary[new_id].decode(),'count':count}))
assert sequences==[[257],[257],[256,114]]
assert [b''.join(vocabulary[i] for i in seq).decode() for seq in sequences]==samples
result={'samples':samples,'stages':stages}
Path(__file__).with_name('tiny-bpe-training.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
