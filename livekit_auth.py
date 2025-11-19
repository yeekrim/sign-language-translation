import time
import jwt  # PyJWT 2.x 필요

API_KEY = "devkey"      # 기존 코드랑 동일
API_SECRET = "secret"   # 기존 코드랑 동일


def create_token(
    identity: str,
    room_name: str
) -> str:
    """
    기존 AccessToken() + VideoGrants 와 동일한 LiveKit JWT 생성기.
    from livekit import api 를 사용하지 않음.
    """

    now = int(time.time())
    exp = now + 60 * 60  # 1시간 유효

    payload = {
        "iss": API_KEY,      # issuer = API Key
        "sub": identity,     # 참가자 identity
        "nbf": now,
        "exp": exp,

        # VideoGrants 와 동일한 grant 구조
        "video": {
            "roomCreate": True,
            "roomJoin": True,
            "room": room_name,
            "canPublish": False,
            "canSubscribe": True,
            "canPublishData": True,
        }
    }

    headers = {
        "kid": API_KEY,
        "typ": "JWT",
        "alg": "HS256"
    }

    token = jwt.encode(payload, API_SECRET, algorithm="HS256", headers=headers)

    # PyJWT 2.x는 문자열을 반환하지만, bytes일 경우 decode 처리
    if isinstance(token, bytes):
        token = token.decode("utf-8")

    return token