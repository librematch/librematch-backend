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
from openapi_server.models.search_param import SearchParam
from openapi_server.models.steam_id import SteamId
from openapi_server.models.too_many_requests_error import TooManyRequestsError
from openapi_server.models.unauthorized_error import UnauthorizedError
from openapi_server.security_api import get_token_BasicAuth, get_token_X-Api-Key

router = APIRouter()


@router.get(
    "/profiles/search",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Search"],
    response_model_by_alias=True,
)
async def get_profile_information_from_search(
    by_name: SearchParam = Query(None, description="First 10 characters of a search string for name to search a &#x60;profile_id&#x60; for"),
    by_steam_id: SteamId = Query(None, description="The Steam ID to search a &#x60;profile_id&#x60; for"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """Search for a profile by Steam ID or name, returns a single &#x60;profile_id&#x60; usable with other endpoints"""
    ...
