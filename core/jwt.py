import time
import jwt
from django.conf import settings

def generate_token(user):
    payload = {
        'user_id': user.id,
        'exp' : int(time.time()) + settings.JWT_ACCESS_TOKEN_LIFETIME,
        'iat' : int(time.time())
    }


    token = jwt.encode(
        payload=payload,
        key=settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGO
    )

    return token

def decode_token(token):
    try:
        return jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=settings.JWT_ALGO
        )
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
        