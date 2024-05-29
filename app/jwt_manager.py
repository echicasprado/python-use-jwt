from jwt import encode, decode

def create_token(data: dict):
    token: str = encode(payload=data, key="MY_SECRETE_KEY", algorithm="HS256")
    return token

def validate_token(token:str) -> dict:
    return decode(token,key="MY_SECRETE_KEY", algorithm=["HS256"])