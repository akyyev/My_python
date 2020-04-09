import zlib
import binascii

data = b'Hello world'
# zlib.compress(data, level=-1)
compressed_data = zlib.compress(data, 3)


print('Original data:', data)
print('Compressed data:', binascii.hexlify(compressed_data))
print('Decompressed data:', zlib.decompress(compressed_data))
