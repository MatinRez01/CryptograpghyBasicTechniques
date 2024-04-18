from pwn import xor
#I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

#73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d


data = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
for i in range(32):
  s = xor(data, i)
  if(s.decode().startswith("crypto")):
    print(s.decode())
