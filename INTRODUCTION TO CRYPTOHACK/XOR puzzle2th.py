from pwn import xor
#I've encrypted the flag with my secret key, you'll never be able to guess it.

#Remember the flag format and how it might help you in this challenge!


#0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104



flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(xor(flag, 'crypto{'.encode()))
# This gives us the key
print(xor(flag, 'myXORkey'.encode()))
# using the output of key, and gussing the 'y' we get the key.