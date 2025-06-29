import random

def generate_key():
    return f"KEY-{random.randint(100000, 999999)}"

new_key = generate_key()

with open("key.txt", "w") as file:
    file.write(new_key)
