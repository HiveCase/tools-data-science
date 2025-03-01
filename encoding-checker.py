import chardet

filename = "roe/sample_superstore.csv"

with open(filename, "rb") as f:
    raw_data = f.read()

result = chardet.detect(raw_data)
print(f"Encoding: {result['encoding']}, Confidence: {result['confidence']}")
