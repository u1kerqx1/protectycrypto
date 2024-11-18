import string
import random
import base64
def get_keys():
	return (string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()_+\";:?=-<>./\\[]}}{{" + "абвгдеёжзийклмнопр стуфхцчшщьыъэюя" + "абвгдеёжзийклмнопрстуфхцчшщьыъэюя".upper())[::-1]
def get_hash_keys(version_keys):
	keys = []
	for i in get_keys():
		keys.append("".join(random.choices(get_keys(),k=version_keys)))
	return keys
def encode(text, hash_keys):
	keys = get_keys()
	hashed = ""
	hk = {}
	c = 0
	for i in keys:
		hk[i] = hash_keys[c]
		c += 1
	for i in text:
		hashed += hk[i]
	return base64.b64encode(hashed.encode()).decode()
def decode(hashed_text, hash_keys):
    hashed_text = base64.b64decode(hashed_text).decode()
    keys = get_keys()
    hk = {}
    c = 0
    decoded = hashed_text
    for i in keys:
        #hk[hash_keys[c]] = i
    	decoded = decoded.replace(hash_keys[c], i)
    	c += 1
    return decoded

keys = get_hash_keys(86)
encoded = encode("моя мать шлюха!", keys)
print(f"Hash keys count: {len(keys)}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decode(encoded, keys)}")
input()