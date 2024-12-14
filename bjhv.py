# # import zlib

# # with open('logfile.txt', 'rb') as file:
# #     compressed_data = file.read()
    
# # decompressed_data = zlib.decompress(compressed_data)
# # print(decompressed_data.decode('utf-8', errors='ignore'))


# import gzip

# with open('logfile.txt', 'rb') as file:
#     compressed_data = file.read()

# try:
#     with gzip.GzipFile(fileobj=compressed_data) as f:
#         decompressed_data = f.read()
#         print(decompressed_data.decode('utf-8', errors='ignore'))
# except Exception as e:
#     print(f"Decompression error: {e}")






import base64

with open('logfile.txt', 'r') as file:
    encoded_data = file.read()

decoded_data = base64.b64decode(encoded_data)

# Now try decompressing it with zlib or gzip
try:
    decompressed_data = zlib.decompress(decoded_data)
    print(decompressed_data.decode('utf-8', errors='ignore'))
except zlib.error:
    print("Not zlib compressed, trying gzip...")

    import gzip
    try:
        with gzip.GzipFile(fileobj=decoded_data) as f:
            decompressed_data = f.read()
            print(decompressed_data.decode('utf-8', errors='ignore'))
    except Exception as e:
        print(f"Decompression error: {e}")
