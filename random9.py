import secrets
print("random secure hexadecimaltoken is",secret.token_hex(64))
print("random secure url is",secret.token_urlsafe(64))
