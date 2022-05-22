"""Sign in endpoint."""
from typing import Any, Optional
from datetime import timedelta

from fastapi import APIRouter, Cookie, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import jwt

from app import crud
from app.api import dependencies
from app.schemas import jwt_token
from app.core import security
from app.core.config import settings

router = APIRouter()


@router.post('/sign-in/token', response_model=jwt_token.Token)
async def get_sign_in_token(
        response: Response,
        database: Session = Depends(dependencies.get_database_session),
        form_data: OAuth2PasswordRequestForm = Depends(),
) -> Any:
    """OAuth2 sign-in token."""
    user = crud.user.authenticate(database, email=form_data.username, password=form_data.password)
    if user is None: raise HTTPException(status_code=400, detail='Incorrect email or password')

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_token(user.user_id, expires_delta=access_token_expires)

    refresh_token_expires = timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    refresh_token = security.create_token(user.user_id, expires_delta=refresh_token_expires, refresh=True)

    response.set_cookie(key='jid', value=refresh_token, httponly=True)
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/refresh-token')
async def get_refresh_token(
        response: Response,
        database: Session = Depends(dependencies.get_database_session),
        jid: Optional[str] = Cookie(None),
):
    """OAuth2 refresh token."""
    token = jid
    if token is None: return {'access_token': ''}

    try:
        payload = jwt.decode(token, settings.REFRESH_TOKEN_SECRET, algorithms=settings.ALGORITHM)
    except jwt.JWTError as error:
        raise HTTPException(status_code=401, detail='User is not signed in') from error

    user = crud.user.get(database, obj_id=payload['sub'])
    if user is None: return {'access_token': ''}

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_token(user.user_id, expires_delta=access_token_expires)

    refresh_token_expires = timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    refresh_token = security.create_token(user.user_id, expires_delta=refresh_token_expires, refresh=True)

    response.set_cookie(key='jid', value=refresh_token, httponly=True)
    return {'access_token': access_token, 'token_type': 'bearer'}
