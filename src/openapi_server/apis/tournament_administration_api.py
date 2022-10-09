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
from openapi_server.models.count_param import CountParam
from openapi_server.models.forbidden_error import ForbiddenError
from openapi_server.models.game_id import GameId
from openapi_server.models.match_status import MatchStatus
from openapi_server.models.not_acceptable_error import NotAcceptableError
from openapi_server.models.not_found_error import NotFoundError
from openapi_server.models.not_implemented_error import NotImplementedError
from openapi_server.models.since_param import SinceParam
from openapi_server.models.too_many_requests_error import TooManyRequestsError
from openapi_server.models.ulid import Ulid
from openapi_server.models.unauthorized_error import UnauthorizedError
from openapi_server.models.unsupported_media_type_error import UnsupportedMediaTypeError
from openapi_server.security_api import get_token_BasicAuth, get_token_X-Api-Key

router = APIRouter()


@router.put(
    "/tournaments/{tournament_id}/admins",
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
    tags=["Administration","Tournament Administration"],
    summary="Bulk update of admins for a specific tournament for a specific game",
    response_model_by_alias=True,
)
async def bulk_update_all_admins_for_tournament(
    tournament_id: Ulid = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.put(
    "/tournaments/{tournament_id}/brackets",
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
    tags=["Administration","Tournament Administration"],
    summary="Bulk update all brackets for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def bulk_update_all_brackets_for_tournament(
    tournament_id: Ulid = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.put(
    "/tournaments",
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
    tags=["Tournament Administration"],
    summary="Bulk update of tournaments",
    response_model_by_alias=True,
)
async def bulk_update_all_tournaments(
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
    "/tournaments/{tournament_id}/admins",
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
    tags=["Administration","Tournament Administration"],
    summary="Create a new admin for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def create_new_admin_for_tournament(
    tournament_id: Ulid = Path(None, description="The unique identifier (ULID) we use for tournaments"),
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
    "/tournaments/{tournament_id}/brackets",
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
    tags=["Administration","Tournament Administration"],
    summary="Create a new bracket for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def create_new_bracket_for_tournament(
    tournament_id: Ulid = Path(None, description="The unique identifier (ULID) we use for tournaments"),
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
    "/tournaments",
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
    tags=["Tournament Administration"],
    summary="Create a new tournament for a game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def create_new_tournament(
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
    "/tournaments/{tournament_id}/admins",
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
    tags=["Administration","Tournament Administration"],
    summary="Retrieve all admins for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def get_admin_collection_for_tournament(
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
    "/tournaments/{tournament_id}/matches",
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
    tags=["Match data","Tournaments","Tournament Administration"],
    summary="Retrieve all match data for a specific tournament for a specific game",
    response_model_by_alias=True,
)
async def get_match_collection_for_tournament(
    tournament_id: Ulid = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    status: MatchStatus = Query(None, description="Match status identifiers to filter for"),
    game: GameId = Query(None, description="Game identifier to query for"),
    count: CountParam = Query(None, description="Number of leaderboard entries to get"),
    since: SinceParam = Query(None, description="Only show matches starting after this Unix timestamp"),
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


@router.patch(
    "/tournaments/{tournament_id}/admins",
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
    tags=["Administration","Tournament Administration"],
    summary="Update details of admins for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def partial_update_all_admins_for_tournament(
    tournament_id: Ulid = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.patch(
    "/tournaments/{tournament_id}/brackets",
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
    tags=["Administration","Tournament Administration"],
    summary="Partial update all brackets for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def partial_update_bracket_for_tournament(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments", regex=r"^[0-7][0-9A-HJKMNP-TV-Z]{25}$", max_length=26),
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.patch(
    "/tournaments",
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
    tags=["Tournament Administration"],
    summary="Partial update of tournaments",
    response_model_by_alias=True,
)
async def partial_update_tournaments(
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
    "/tournaments/{tournament_id}/admins",
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
    tags=["Administration","Tournament Administration"],
    summary="Remove all admins for a specific tournament for a specific game",
    response_model_by_alias=True,
)
async def remove_all_admins_for_tournament(
    tournament_id: Ulid = Path(None, description="The unique identifier (ULID) we use for tournaments"),
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
    tags=["Tournament Administration"],
    summary="Remove all brackets for a specific tournament for a specific game",
    response_model_by_alias=True,
)
async def remove_all_brackets_for_tournament(
    tournament_id: Ulid = Path(None, description="The unique identifier (ULID) we use for tournaments"),
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
    tags=["Tournament Administration"],
    summary="Remove all tournaments",
    response_model_by_alias=True,
)
async def remove_all_tournaments(
    token_BasicAuth: TokenModel = Security(
        get_token_BasicAuth
    ),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...
