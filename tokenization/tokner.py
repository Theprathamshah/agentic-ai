import tiktoken

tokenr = tiktoken.encoding_for_model("gpt-4o")

text = "Hello, how are you doing today?"

tokens = tokenr.encode(text)
print(tokens)

decoede_values = tokenr.decode(tokens)
print(decoede_values)
