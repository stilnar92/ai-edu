# Encoding a new sentence

Input: `the small dog eats fish`

This uses saved merge rules, without adding entries or training the language model. Space is shown as ␣.

| Piece | ID |
|---|---:|
| `the␣` | 259 |
| `s` | 115 |
| `m` | 109 |
| `a` | 97 |
| `l` | 108 |
| `l` | 108 |
| `␣d` | 263 |
| `o` | 111 |
| `g` | 103 |
| `␣` | 32 |
| `e` | 101 |
| `at` | 261 |
| `s␣` | 256 |
| `f` | 102 |
| `i` | 105 |
| `s` | 115 |
| `h` | 104 |

17 tokens; vocabulary remains 272 entries. Decoding recovers the exact input. Only 16 merges were trained, so many letters still appear as individual tokens.

Run from the edu folder:

```sh
python3 ai-edu/llm-textbook/mini-model/encode.py "the small dog eats fish"
```

Check: why can a new sentence be represented without adding a whole-sentence token?
