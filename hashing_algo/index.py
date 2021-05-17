import hashlib

message = "Text to hash".encode()

# Hash with MD5 (bad opportunity)
print("MD5:", hashlib.md5(message).hexdigest())

# Hash with SHA-256 & SHA-512
print("SHA-256:", hashlib.sha256(message).hexdigest())
print("SHA-512:", hashlib.sha512(message).hexdigest())

# Hash with SHA-3
print("SHA-3-256:", hashlib.sha3_256(message).hexdigest())
print("SHA-3-512:", hashlib.sha3_512(message).hexdigest())