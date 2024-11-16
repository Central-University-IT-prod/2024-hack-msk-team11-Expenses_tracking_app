from datetime import datetime, timedelta, timezone
from typing import Any
from dataclasses import dataclass
import jwt
from jwt import PyJWTError

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
REFRESH_TOKEN_EXPIRE_MINUTES = 30
JWT_SECRET_KEY = '{{sensitive_data}}'
ALGORITHM = "HS256"


@dataclass
class JWTData:
    username: str
    issuer: str
    issued_at: datetime
    expire_at: datetime


def generate_jwt(
        username: str,
        issuer: str,
        expires_delta: timedelta = timedelta(weeks=4),
) -> str:
    expire = datetime.now(timezone.utc) + expires_delta
    jwt_data = {
        "sub": username,
        "iat": datetime.now(timezone.utc).timestamp(),
        "iss": issuer,
        "exp": expire.timestamp()
    }
    token = jwt.encode(
        jwt_data,
        key=JWT_SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def decode_jwt(
        token: str
) -> JWTData:
    decoded_jwt: dict[str, Any] = jwt.decode(
        jwt=token,
        key=JWT_SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    if (
            "sub" not in decoded_jwt
            or "iat" not in decoded_jwt
            or "exp" not in decoded_jwt
            or "iss" not in decoded_jwt
    ):
        raise PyJWTError

    jwt_data = JWTData(
        username=decoded_jwt["sub"],
        issuer=decoded_jwt["iss"],
        issued_at=datetime.fromtimestamp(
            decoded_jwt["iat"],
            tz=timezone.utc
        ),
        expire_at=datetime.fromtimestamp(
            decoded_jwt["exp"],
            tz=timezone.utc
        ),
    )

    return jwt_data
