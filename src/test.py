import struct

a = b'\x00\x00\x80\x00'
print(a)

test =struct.unpack('f',a)
print(test)