# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.forbidden_error import ForbiddenError
from openapi_server.models.not_acceptable_error import NotAcceptableError
from openapi_server.models.not_found_error import NotFoundError
from openapi_server.models.too_many_requests_error import TooManyRequestsError
from openapi_server.models.unauthorized_error import UnauthorizedError
from openapi_server.models.unsupported_media_type_error import UnsupportedMediaTypeError
from openapi_server.security_api import get_token_BasicAuth, get_token_X-Api-Key

router = APIRouter()


@router.post(
    "/users",
    responses={
        200: {"description": "Operation succeeded"},
        201: {"description": "Created"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        415: {"model": UnsupportedMediaTypeError, "description": "Unsupported Media Type"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Authentication","Account Registration","User Administration"],
    summary="Create a new user for our platform",
    response_model_by_alias=True,
)
async def create_new_user(
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.post(
    "/users/register",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        415: {"model": UnsupportedMediaTypeError, "description": "Unsupported Media Type"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Account Registration"],
    response_model_by_alias=True,
)
async def user_register(
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...
