"""Sign in endpoint."""
from typing import Any
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud
from app.api import dependencies
from app.authentication import token
from app.schemas import jwt_token
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
    if not user: raise HTTPException(status_code=400, detail='Incorrect email or password')

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(user.user_id, expires_delta=access_token_expires)

    refresh_token_expires = timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    refresh_token = token.create_refresh_token(user.user_id, expires_delta=refresh_token_expires)

    response.set_cookie(key='jid', value=refresh_token, httponly=True)
    return {
        'access_token': access_token,
        'token_type': 'bearer',
    }


@router.post('/refresh-token')
async def get_refresh_token():
    """OAuth2 refresh token."""
    pass
