import chardet

with open('logfile.txt', 'rb') as file:
    raw_data = file.read()

result = chardet.detect(raw_data)
print(f"Detected encoding: {result['encoding']}")

# Try to decode using the detected encoding
decoded_data = raw_data.decode(result['encoding'], errors='ignore')
print(decoded_data)
