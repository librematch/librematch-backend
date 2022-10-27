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
from openapi_server.models.timeframe import Timeframe
from openapi_server.models.too_many_requests_error import TooManyRequestsError
from openapi_server.models.ulid import Ulid
from openapi_server.models.unauthorized_error import UnauthorizedError
from openapi_server.security_api import get_token_BasicAuth, get_token_X-Api-Key

router = APIRouter()


@router.get(
    "/dumps/{timeframe}",
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
    tags=["Database","Statistics"],
    response_model_by_alias=True,
)
async def get_database_dump_collection(
    timeframe: Timeframe = Path(None, description="The timeframe from which to download a database dump"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """Download a database dump from a given timeframe"""
    ...


@router.get(
    "/leaderboards/{leaderboard_id}/stats",
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
    tags=["Leaderboards","Statistics"],
    summary="Retrieve all stats on a specific leaderboard for a certain game",
    response_model_by_alias=True,
)
async def get_stat_collection_for_leaderboard(
    leaderboard_id: Ulid = Path(None, description="The unique identifier (ULID) we use for leaderboards of the Relic Link API"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/profiles/{relic_link_id}/stats",
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
    tags=["Statistics"],
    summary="Retrieve all stats for a specific profile",
    response_model_by_alias=True,
)
async def get_stat_collection_for_profile(
    relic_link_id: RelicLinkId = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/teams/{team_id}/stats",
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
    tags=["Statistics","Teams","Team Administration"],
    summary="Retrieve a list of stats for a specific team",
    response_model_by_alias=True,
)
async def get_stat_collection_for_team(
    team_id: Ulid = Path(None, description="The unique identifier (ULID) we use for teams that play on games using the Relic Link API"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/tournaments/{tournament_id}/stats",
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
    tags=["Statistics","Tournaments","Tournament Administration"],
    summary="Retrieve all statistics for a specific tournament for a specific game",
    response_model_by_alias=True,
)
async def get_stat_collection_for_tournament(
    tournament_id: Ulid = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/users/{user_id}/stats",
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
    tags=["Statistics"],
    summary="Retrieve all stats for a specific user profile on our platform",
    response_model_by_alias=True,
)
async def get_stat_collection_for_user(
    user_id: Ulid = Path(None, description="The unique identifier (ULID) we use for users of our API"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...
