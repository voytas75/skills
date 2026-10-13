import base64
import hashlib
import re

def verify(head, tracking, advertised, intended, response):
    for sha in (head, tracking, advertised):
        if not re.fullmatch(r"[0-9a-f]{40}", sha):
            raise ValueError("invalid SHA")
    if not head == tracking == advertised:
        raise ValueError("revision mismatch")
    if response["encoding"] != "base64":
        raise ValueError("unsupported representation")
    actual = base64.b64decode(response["content"], validate=True)
    if actual != intended:
        raise ValueError("byte mismatch")
    return hashlib.sha256(actual).hexdigest()

sha = "a" * 40
payload = b"synthetic\r\n"
response = {"encoding": "base64", "content": base64.b64encode(payload).decode()}
assert verify(sha, sha, sha, payload, response) == hashlib.sha256(payload).hexdigest()
for args in [(sha, "b"*40, sha, payload, response), ("bad", sha, sha, payload, response), (sha, sha, sha, b"synthetic\n", response)]:
    try:
        verify(*args)
    except ValueError:
        pass
    else:
        raise AssertionError("mismatch accepted")
print("PASS delivery: SHA syntax/equality and exact bytes; fixtures only, no remote call")
