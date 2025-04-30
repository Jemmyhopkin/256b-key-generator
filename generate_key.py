import os
import base64

def generate_key():
    key = os.urandom(32)  # 32 bytes = 256 bits
    encoded_key = base64.b64encode(key).decode('utf-8')
    print(f"Generated 256-bit Key: {encoded_key}")

if __name__ == "__main__":
    generate_key()
