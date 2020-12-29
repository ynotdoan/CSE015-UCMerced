
def encode(t, k):
  '''
  Encodes characters in list t using ASCII and key k.
  '''
  encoded = []
  msg = ""
  for i in t:
    # converts charcter to numeric ASCII form and shifts down by 32
    num = ord(i) - 32
    # increases num by key amount and finds mod95 and shifts up by 32
    p = ((num + k) % 95) + 32
    # converts shifted num back to char and appends to list encoded
    encoded.append(chr(p))
    # adds encoded char to string
    msg += chr(p)
  
  # prints list of encoded message and returns list of encoded char
  print (f"\nEncoded message: {msg}")
  return encoded


def decode(t, k):
  '''
  Decodes characters in list t
  '''
  decoded = []
  msg = ""
  for i in t:
    # converts char to ASCII num and shift down by 32
    num = ord(i) - 32
    # decreases num by key amount and finds mod95 and shifts up by 32
    p = ((num - k) % 95) + 32
    # converts num to char and appends to list decoded
    decoded.append(chr(p))
    # adds decoded char to string
    msg += chr(p)
  
  # prints decoded message in string format and returns list of decoded char
  print (f"\nDecoded message: {msg}")
  return decoded


t = ["A", "B", "C", "a", "b", "c"]
y = ["H", "e", "l", "l", "o", " ", "t", "h", "e", "r", "e"]
k = 7
encode_msg = encode(y, k)
print (encode_msg)

decode_msg = decode(encode_msg, k)
print (decode_msg)
