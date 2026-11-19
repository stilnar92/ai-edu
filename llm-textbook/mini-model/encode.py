"""Use the saved tokenizer without training or changing its vocabulary."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def encode(text):
    saved = json.loads((ROOT / 'tokenizer.json').read_text())
    vocab = {i: bytes([i]) for i in range(256)}
    vocab.update({int(i): bytes(b) for i, b in saved['addedVocabulary'].items()})
    sequence = list(text.encode('utf-8'))
    steps = []
    for rule in saved['merges']:
        result = []
        i = 0
        while i < len(sequence):
            if i + 1 < len(sequence) and sequence[i:i+2] == [rule['left'], rule['right']]:
                result.append(rule['id'])
                i += 2
            else:
                result.append(sequence[i])
                i += 1
        if result != sequence:
            steps.append({'merged': vocab[rule['id']].decode('utf-8', errors='backslashreplace'), 'id': rule['id']})
        sequence = result
    recovered = b''.join(vocab[i] for i in sequence).decode('utf-8')
    assert recovered == text
    return {'text': text, 'ids': sequence,
            'pieces': [vocab[i].decode('utf-8', errors='backslashreplace') for i in sequence],
            'appliedMerges': steps, 'decoded': recovered, 'vocabularySize': len(vocab)}

if __name__ == '__main__':
    text = sys.argv[1] if len(sys.argv)>1 else 'the small dog eats fish'
    print(json.dumps(encode(text), ensure_ascii=False, indent=2))
