"""Real, reproducible tokenization. No model API call; no input text is uploaded."""
import json
import os
import sys
from pathlib import Path
import tiktoken

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault('TIKTOKEN_CACHE_DIR', str(ROOT / '.tokenizer-cache'))
enc = tiktoken.get_encoding('cl100k_base')
texts = sys.argv[1:] or ['hello world', 'Hello world', 'hello  world', 'I am replaying the video.']
results = []
for text in texts:
    ids = enc.encode(text)
    token_bytes = [enc.decode_single_token_bytes(i) for i in ids]
    assert b''.join(token_bytes).decode('utf-8') == text
    results.append({'text': text, 'ids': ids,
                    'pieces': [b.decode('utf-8', errors='backslashreplace') for b in token_bytes],
                    'bytes': [list(b) for b in token_bytes],
                    'decoded': enc.decode(ids)})
output = {'encoding': enc.name, 'library': 'tiktoken', 'version': tiktoken.__version__, 'examples': results}
print(json.dumps(output, ensure_ascii=False, indent=2))
if len(sys.argv) == 1:
    Path(__file__).with_name('tokenization-examples.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
