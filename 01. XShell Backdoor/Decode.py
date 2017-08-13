import struct

fd=open('Encoded.bin','rb')
data=fd.read()
fd.close()

(xor_key,) = struct.unpack("<L", data[0:4])

print xor_key

decoded_bytes=''
for ch in data[4:]:
	decoded_bytes += chr(ord(ch) ^ (xor_key & 0xff))

	xor_key = ((xor_key << 0x10)  + (xor_key >> 0x10)) & 0xffffffff
	xor_key = ((xor_key * 0xC9BED351) - 0x57A25E37) & 0xffffffff

fd=open('Stage1.bin','wb')
fd.write(decoded_bytes)
fd.close()
