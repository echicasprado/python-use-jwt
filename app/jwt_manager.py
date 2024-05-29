from jwt import encode

def create_token(data: dict):
    token: str = encode(payload=data, key="MY_SECRETE_KEY", algorithm="HS256")
    return token