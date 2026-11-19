# Real text to token IDs

This example applies an already-trained tokenizer; it does not train one on the selected sentence.

Verified locally on 2026-11-05 with `tiktoken==0.14.0`, encoding `cl100k_base`. See https://github.com/openai/tiktoken for the library documentation.

1. Choose text: `hello world`.
2. Load the existing tokenizer vocabulary and merge rules.
3. Encode: pieces `hello` and ` world` correspond to IDs `[15339, 1917]`.
4. These IDs are the numerical representation of this text. A real conversation includes additional formatting and context.
5. Decode the IDs: the original `hello world` is recovered exactly.

The leading space belongs to the second token. Changing capitalization or spacing can change token IDs and token count. These results describe this named encoding, not every model or every current ChatGPT configuration.

The inline comparison displays recorded outputs verified by the Python script, not an arbitrary-text browser tokenizer. Select the longer sentence to see subword splitting: ` replay` and `ing`.

## Run your own text
From the folder that contains `ai-edu`:

```sh
.work/llm-tokenizer-venv/bin/python ai-edu/llm-textbook/materials/tokenize_real.py 'Your text here'
```

The project-local environment has the pinned tokenizer installed. If recreating it, create a Python virtual environment and install `tiktoken==0.14.0`.

The first run downloads the public tokenizer vocabulary; subsequent runs use the local cache. Input text is processed locally, without a model API or API key. The script outputs raw token bytes too: individual tokens can split a Unicode character, so their per-token display uses byte escapes when needed. Full decoding recovers the original UTF-8 text.

## Question
Compare `hello world` with `Hello world`: which token changes, and which remains the same?
