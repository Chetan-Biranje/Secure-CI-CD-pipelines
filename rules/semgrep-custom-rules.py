import hashlib

import jwt

# ruleid: python-hardcoded-jwt-secret
a = jwt.encode({"sub": 1}, "secret", algorithm="HS256")
# ruleid: python-hardcoded-jwt-secret
b = jwt.encode({"sub": 1}, key="password", algorithm="HS256")
# ruleid: python-hardcoded-jwt-secret
c = jwt.encode({"sub": 1}, secret_key="admin", algorithm="HS256")
# ok: python-hardcoded-jwt-secret
d = jwt.encode({"sub": 1}, SECRET_FROM_ENV, algorithm="HS256")

# ruleid: insecure-md5-usage
h = hashlib.md5(b"x").hexdigest()
# ok: insecure-md5-usage
g = hashlib.sha256(b"x").hexdigest()
