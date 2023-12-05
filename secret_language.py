import random

encode_lang = "abc"

print(f"{random.randint(100, 999)}{encode_lang[::-1][1:]}{encode_lang[::-1][:1]}{random.randint(100, 999)}")