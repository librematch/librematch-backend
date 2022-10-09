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
from openapi_server.models.not_implemented_error import NotImplementedError
from openapi_server.models.relic_link_id import RelicLinkId
from openapi_server.models.too_many_requests_error import TooManyRequestsError
from openapi_server.models.unauthorized_error import UnauthorizedError
from openapi_server.models.unsupported_media_type_error import UnsupportedMediaTypeError
from openapi_server.security_api import get_token_BasicAuth, get_token_X-Api-Key

router = APIRouter()


@router.put(
    "/profiles/{relic_link_id}/settings",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        415: {"model": UnsupportedMediaTypeError, "description": "Unsupported Media Type"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        501: {"model": NotImplementedError, "description": "Not Implemented"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Profile Administration","Administration"],
    summary="Bulk update of settings for a specific profile from the Relic Link API",
    response_model_by_alias=True,
)
async def bulk_update_all_settings_for_profile(
    relic_link_id: RelicLinkId = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
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
    "/profiles/{relic_link_id}/settings",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        415: {"model": UnsupportedMediaTypeError, "description": "Unsupported Media Type"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        501: {"model": NotImplementedError, "description": "Not Implemented"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Profile Administration","Administration"],
    summary="Create a new setting for a specific profile from the Relic Link API",
    response_model_by_alias=True,
)
async def create_new_setting_for_profile(
    relic_link_id: RelicLinkId = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.get(
    "/profiles/{relic_link_id}/settings",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        501: {"model": NotImplementedError, "description": "Not Implemented"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Profile Administration","Administration","Information"],
    summary="Retrieve all settings for a specific profile",
    response_model_by_alias=True,
)
async def get_setting_collection_for_profile(
    relic_link_id: RelicLinkId = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.patch(
    "/profiles/{relic_link_id}/settings",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        415: {"model": UnsupportedMediaTypeError, "description": "Unsupported Media Type"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        501: {"model": NotImplementedError, "description": "Not Implemented"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Profile Administration","Administration"],
    summary="Update a specific setting for a specific profile from the Relic Link API",
    response_model_by_alias=True,
)
async def partial_update_all_settings_for_profile(
    relic_link_id: RelicLinkId = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.delete(
    "/profiles/{relic_link_id}/settings",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        501: {"model": NotImplementedError, "description": "Not Implemented"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Profile Administration","Administration"],
    summary="Remove all settings for a specific profile",
    response_model_by_alias=True,
)
async def remove_all_settings_for_profile(
    relic_link_id: RelicLinkId = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...