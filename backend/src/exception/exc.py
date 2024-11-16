from starlette import status
from starlette.exceptions import HTTPException

BAD_CREDENTIALS = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Bad credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

ENTITY_EXISTS = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Entity exists"
)

FORBIDDEN = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN
)

NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Entity not found"
)

BAD_REQUEST = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST
)