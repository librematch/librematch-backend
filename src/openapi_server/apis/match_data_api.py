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
from openapi_server.models.match_id import MatchId
from openapi_server.models.match_status import MatchStatus
from openapi_server.models.not_acceptable_error import NotAcceptableError
from openapi_server.models.not_found_error import NotFoundError
from openapi_server.models.not_implemented_error import NotImplementedError
from openapi_server.models.relic_link_id import RelicLinkId
from openapi_server.models.since_param import SinceParam
from openapi_server.models.start_param import StartParam
from openapi_server.models.too_many_requests_error import TooManyRequestsError
from openapi_server.models.ulid import Ulid
from openapi_server.models.unauthorized_error import UnauthorizedError
from openapi_server.security_api import get_token_BasicAuth, get_token_X-Api-Key

router = APIRouter()


@router.get(
    "/profiles/{relic_link_id}/ledger",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Match data","Ratings"],
    summary="Retrieve the rating ledger for a specific profile",
    response_model_by_alias=True,
)
async def get_ledger_collection_for_profile(
    relic_link_id: RelicLinkId = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    game: GameId = Query(None, description="Game identifier to query for"),
    start: StartParam = Query(None, description="Starting match"),
    leaderboard_id: Ulid = Query(None, description="Leaderboard identifier"),
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
    "/games/{game_id}/matches",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Match data"],
    summary="Retrieve all matches for a specific game",
    response_model_by_alias=True,
)
async def get_match_collection_for_game(
    game_id: GameId = Path(None, description="The unique identifier we use for games that use the Relic Link API"),
    single_match: MatchId = Query(None, description="Match ID to filter for its details"),
    status: MatchStatus = Query(None, description="Match status identifiers to filter for"),
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
    "/leaderboards/{leaderboard_id}/matches",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Leaderboards","Match data"],
    summary="Retrieve all matches on a specific leaderboard for a certain game",
    response_model_by_alias=True,
)
async def get_match_collection_for_leaderboard(
    leaderboard_id: Ulid = Path(None, description="The unique identifier (ULID) we use for leaderboards of the Relic Link API"),
    status: MatchStatus = Query(None, description="Match status identifiers to filter for"),
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
    "/profiles/{relic_link_id}/matches",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access"},
        403: {"model": ForbiddenError, "description": "Forbidden"},
        404: {"model": NotFoundError, "description": "Entity not found"},
        406: {"model": NotAcceptableError, "description": "Not acceptable"},
        429: {"model": TooManyRequestsError, "description": "Too Many Requests"},
        200: {"model": UnauthorizedError, "description": "Unauthorized access"},
    },
    tags=["Match data"],
    summary="Retrieve all matches for a specific profile",
    response_model_by_alias=True,
)
async def get_match_collection_for_profile(
    relic_link_id: RelicLinkId = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    last_match: bool = Query(None, description="Only show exactly the last available match"),
    status: MatchStatus = Query(None, description="Match status identifiers to filter for"),
    game: GameId = Query(None, description="Game identifier to query for"),
    start: StartParam = Query(None, description="Starting match"),
    count: CountParam = Query(None, description="Number of entries to get"),
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
    "/teams/{team_id}/matches",
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
    tags=["Match data"],
    summary="Retrieve a list of matches for a specific team",
    response_model_by_alias=True,
)
async def get_match_collection_for_team(
    team_id: Ulid = Path(None, description="The unique identifier (ULID) we use for teams that play on games using the Relic Link API"),
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
