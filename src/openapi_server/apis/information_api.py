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
from openapi_server.models.game_id import GameId
from openapi_server.models.not_acceptable_error import NotAcceptableError
from openapi_server.models.not_found_error import NotFoundError
from openapi_server.models.not_implemented_error import NotImplementedError
from openapi_server.models.relic_link_id import RelicLinkId
from openapi_server.models.too_many_requests_error import TooManyRequestsError
from openapi_server.models.ulid import Ulid
from openapi_server.models.unauthorized_error import UnauthorizedError
from openapi_server.security_api import get_token_BasicAuth, get_token_X-Api-Key

router = APIRouter()


@router.get(
    "/tournaments/{tournament_id}/brackets",
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
    tags=["Information","Tournaments","Tournament Administration"],
    summary="Retrieve all brackets for a specific tournament for a specific game",
    response_model_by_alias=True,
)
async def get_bracket_collection_for_tournament(
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
    "/profiles/{relic_link_id}",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Information"],
    summary="Retrieve the details for a specific profile",
    response_model_by_alias=True,
)
async def get_details_for_profile(
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
    "/tournaments/{tournament_id}",
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
    tags=["Information"],
    summary="Retrieve details for a tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def get_details_for_tournament(
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
    "/users/{user_id}",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Information","User Administration"],
    summary="Retrieve details for a specific user profile on our platform",
    response_model_by_alias=True,
)
async def get_details_for_user(
    user_id: Ulid = Path(None, description="The unique identifier (ULID) we use for users of our API"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/games",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Information"],
    summary="Retrieve a list of all game identifiers for games",
    response_model_by_alias=True,
)
async def get_game_identifier_collection(
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/games/{game_id}/info",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Information"],
    summary="Retrieve all available information for a specific game",
    response_model_by_alias=True,
)
async def get_info_collection_for_game(
    game_id: GameId = Path(None, description="The unique identifier we use for games that use the Relic Link API"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/tournaments/{tournament_id}/info",
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
    tags=["Information","Tournaments","Tournament Administration"],
    summary="Retrieve all information for a specific tournament for a specific game",
    response_model_by_alias=True,
)
async def get_info_collection_for_tournament(
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
    "/leaderboards",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Leaderboards","Information"],
    summary="Retrieve all leaderboards",
    response_model_by_alias=True,
)
async def get_leaderboard_collection(
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
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


@router.get(
    "/teams",
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
    tags=["Information","Teams","Team Administration"],
    summary="Retrieve all available teams",
    response_model_by_alias=True,
)
async def get_team_collection(
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/tournaments",
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
    tags=["Information","Tournament Administration"],
    summary="Retrieve all available tournaments for all games available on the Relic Link platform",
    response_model_by_alias=True,
)
async def get_tournament_identifier_collection(
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...
