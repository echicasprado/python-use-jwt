from jwt import encode, decode

KEY = "MY_SECRETE_KEY"

def create_token(data: dict):
    token: str = encode(payload=data, key=KEY, algorithm="HS256")
    return token

def validate_token(token:str) -> dict:
    return decode(token,key=KEY,algorithms=["HS256"])