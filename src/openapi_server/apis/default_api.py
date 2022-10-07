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
from openapi_server.models.unauthorized_error import UnauthorizedError
from openapi_server.security_api import get_token_X-Api-Key

router = APIRouter()


@router.put(
    "/tournaments/{tournament_id}/admins",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Bulk update of admins for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def bulk_update_all_admins_for_tournament(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.put(
    "/tournaments/{tournament_id}/brackets",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Bulk update all brackets for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def bulk_update_all_brackets_for_tournament(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.put(
    "/profiles/{relic_link_id}/settings",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Bulk update of settings for a specific profile from the Relic Link API",
    response_model_by_alias=True,
)
async def bulk_update_all_settings_for_profile(
    relic_link_id: int = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.put(
    "/teams",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Bulk update of teams",
    response_model_by_alias=True,
)
async def bulk_update_all_teams(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.put(
    "/tournaments",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Bulk update of tournaments",
    response_model_by_alias=True,
)
async def bulk_update_all_tournaments(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.put(
    "/users/{user_id}",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Bulk update details for a specific user profile on our platform if it exists",
    response_model_by_alias=True,
)
async def bulk_update_all_user_details(
    user_id: str = Path(None, description="The unique identifier (ULID) we use for users of our API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.put(
    "/users/{user_id}/stats",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Bulk update of stats for a specific user profile on our platform",
    response_model_by_alias=True,
)
async def bulk_update_all_user_stats(
    user_id: str = Path(None, description="The unique identifier (ULID) we use for users of our API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.put(
    "/users",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Bulk update of all users of our platform",
    response_model_by_alias=True,
)
async def bulk_update_all_users(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.post(
    "/tournaments/{tournament_id}/admins",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Create a new admin for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def create_new_admin_for_tournament(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.post(
    "/tournaments/{tournament_id}/brackets",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Create a new bracket for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def create_new_bracket_for_tournament(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.post(
    "/profiles/{relic_link_id}/settings",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Create a new setting for a specific profile from the Relic Link API",
    response_model_by_alias=True,
)
async def create_new_setting_for_profile(
    relic_link_id: int = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.post(
    "/teams",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Create a new team",
    response_model_by_alias=True,
)
async def create_new_team(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.post(
    "/tournaments",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Create a new tournament for a game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def create_new_tournament(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.post(
    "/users",
    responses={
        200: {"description": "Operation succeeded"},
        201: {"description": "Created"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Create a new user for our platform",
    response_model_by_alias=True,
)
async def create_new_user(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.post(
    "/users/{user_id}/stats",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Create a new stat for a specific user profile on our platform",
    response_model_by_alias=True,
)
async def create_new_user_stats(
    user_id: str = Path(None, description="The unique identifier (ULID) we use for users of our API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.post(
    "/users/validate",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def create_new_user_validation(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/tournaments/{tournament_id}/admins",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Retrieve all admins for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def get_admin_collection_for_tournament(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/tournaments/{tournament_id}/brackets",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Retrieve all brackets for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def get_bracket_collection_for_tournament(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/games/{game_id}/definitions",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve all available definitions for a specific game using Relic Link API",
    response_model_by_alias=True,
)
async def get_definition_collection_for_game(
    game_id: str = Path(None, description="The unique identifier (ULID) we use for games that use the Relic Link API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/games/{game_id}",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve details for a game with a specific identifier using Relic Link API",
    response_model_by_alias=True,
)
async def get_details_for_game(
    game_id: str = Path(None, description="The unique identifier (ULID) we use for games that use the Relic Link API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/leaderboards/{leaderboard_id}",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve details for a specific leaderboard",
    response_model_by_alias=True,
)
async def get_details_for_leaderboard(
    leaderboard_id: str = Path(None, description="The unique identifier (ULID) we use for leaderboards of the Relic Link API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/profiles/{relic_link_id}",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve the details for a specific profile from the Relic Link API",
    response_model_by_alias=True,
)
async def get_details_for_profile(
    relic_link_id: int = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/teams/{team_id}",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Retrieve details of a team",
    response_model_by_alias=True,
)
async def get_details_for_team(
    game_id: str = Path(None, description="The unique identifier (ULID) we use for teams that play on games using the Relic Link API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/tournaments/{tournament_id}",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Retrieve details for a tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def get_details_for_tournament(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/users/{user_id}",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve details for a specific user profile on our platform",
    response_model_by_alias=True,
)
async def get_details_for_user(
    user_id: str = Path(None, description="The unique identifier (ULID) we use for users of our API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/games",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve a list of all game identifiers for games using Relic Link API",
    response_model_by_alias=True,
)
async def get_game_identifier_collection(
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
    },
    tags=["default"],
    summary="Retrieve all available information for a specific game using Relic Link API",
    response_model_by_alias=True,
)
async def get_info_collection_for_game(
    game_id: str = Path(None, description="The unique identifier (ULID) we use for games that use the Relic Link API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/tournaments/{tournament_id}/info",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Retrieve all information for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def get_info_collection_for_tournament(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/application",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve a list of available application information",
    response_model_by_alias=True,
)
async def get_information_collection_for_application(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/leaderboards",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve all leaderboards hosted on the Relic Link API",
    response_model_by_alias=True,
)
async def get_leaderboard_collection(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/games/{game_id}/leaderboards",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve all leaderboards for a specific game using Relic Link API",
    response_model_by_alias=True,
)
async def get_leaderboard_collection_for_game(
    game_id: str = Path(None, description="The unique identifier (ULID) we use for games that use the Relic Link API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/games/{game_id}/matches",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve all matches for a specific game using Relic Link API",
    response_model_by_alias=True,
)
async def get_match_collection_for_game(
    game_id: str = Path(None, description="The unique identifier (ULID) we use for games that use the Relic Link API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/leaderboards/{leaderboard_id}/matches",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve all matches on a specific leaderboard for a certain game hosted on the Relic Link API",
    response_model_by_alias=True,
)
async def get_match_collection_for_leaderboard(
    leaderboard_id: str = Path(None, description="The unique identifier (ULID) we use for leaderboards of the Relic Link API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/profiles/{relic_link_id}/matches",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve all matches for a specific profile from the Relic Link API",
    response_model_by_alias=True,
)
async def get_match_collection_for_profile(
    relic_link_id: int = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/teams/{team_id}/matches",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Retrieve a list of matches for a specific team",
    response_model_by_alias=True,
)
async def get_match_collection_for_team(
    game_id: str = Path(None, description="The unique identifier (ULID) we use for teams that play on games using the Relic Link API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/profiles",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve all available profiles from the Relic Link API",
    response_model_by_alias=True,
)
async def get_profile_collection(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/profiles/{relic_link_id}/settings",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Retrieve all settings for a specific profile from the Relic Link API",
    response_model_by_alias=True,
)
async def get_setting_collection_for_profile(
    relic_link_id: int = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/application/statistics",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve a list of only application statistics",
    response_model_by_alias=True,
)
async def get_stat_collection_for_application(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/leaderboards/{leaderboard_id}/stats",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Retrieve all stats on a specific leaderboard for a certain game hosted on the Relic Link API",
    response_model_by_alias=True,
)
async def get_stat_collection_for_leaderboard(
    leaderboard_id: str = Path(None, description="The unique identifier (ULID) we use for leaderboards of the Relic Link API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/profiles/{relic_link_id}/stats",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Retrieve all stats for a specific profile from the Relic Link API",
    response_model_by_alias=True,
)
async def get_stat_collection_for_profile(
    relic_link_id: int = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/teams/{team_id}/stats",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Retrieve a list of stats for a specific team",
    response_model_by_alias=True,
)
async def get_stat_collection_for_team(
    game_id: str = Path(None, description="The unique identifier (ULID) we use for teams that play on games using the Relic Link API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/users/{user_id}/stats",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Retrieve all stats for a specific user profile on our platform",
    response_model_by_alias=True,
)
async def get_stat_collection_for_user(
    user_id: str = Path(None, description="The unique identifier (ULID) we use for users of our API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/application/status",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
        503: {"description": "Service Unavailable"},
    },
    tags=["default"],
    summary="Retrieve only application status",
    response_model_by_alias=True,
)
async def get_status_collection_for_application(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/teams",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Retrieve all available teams",
    response_model_by_alias=True,
)
async def get_team_collection(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/tournaments/{game_id}",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Retrieve all available tournaments for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def get_tournament_details_for_game(
    game_id: str = Path(None, description="The unique identifier (ULID) we use for games that use the Relic Link API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/tournaments",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Retrieve all available tournaments for all games available on the Relic Link platform",
    response_model_by_alias=True,
)
async def get_tournament_identifier_collection(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/users",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Retrieve all users of our platform",
    response_model_by_alias=True,
)
async def get_user_collection(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """Authenticated Endpoint for Administrators or Libre:Match"""
    ...


@router.get(
    "/users/validate",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def get_user_validation_details(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.patch(
    "/tournaments/{tournament_id}/admins",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Update details of admins for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def partial_update_all_admins_for_tournament(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.patch(
    "/profiles/{relic_link_id}/settings",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Update a specific setting for a specific profile from the Relic Link API",
    response_model_by_alias=True,
)
async def partial_update_all_settings_for_profile(
    relic_link_id: int = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.patch(
    "/teams",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Partial update of all teams",
    response_model_by_alias=True,
)
async def partial_update_all_teams(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.patch(
    "/users",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Partially update details for all user profiles",
    response_model_by_alias=True,
)
async def partial_update_all_users(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.patch(
    "/tournaments/{tournament_id}/brackets",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Partial update all brackets for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def partial_update_bracket_for_tournament(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.patch(
    "/tournaments/{tournament_id}",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Partially update a tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def partial_update_tournament_details(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.patch(
    "/tournaments",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Partial update of tournaments",
    response_model_by_alias=True,
)
async def partial_update_tournaments(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.patch(
    "/users/{user_id}",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Update details for a specific user profile on our platform if it exists",
    response_model_by_alias=True,
)
async def partial_update_user(
    user_id: str = Path(None, description="The unique identifier (ULID) we use for users of our API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.patch(
    "/users/{user_id}/stats",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Partially update stats for a specific user profile on our platform",
    response_model_by_alias=True,
)
async def partial_update_user_stats(
    user_id: str = Path(None, description="The unique identifier (ULID) we use for users of our API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.delete(
    "/tournaments/{tournament_id}/admins",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Remove all admins for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def remove_all_admins_for_tournament(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.delete(
    "/tournaments/{tournament_id}/brackets",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Remove all brackets for a specific tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def remove_all_brackets_for_tournament(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.delete(
    "/profiles/{relic_link_id}/settings",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Remove all settings for a specific profile from the Relic Link API",
    response_model_by_alias=True,
)
async def remove_all_settings_for_profile(
    relic_link_id: int = Path(None, description="The unique identifier used by the Relic Link API for a player on their platform"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.delete(
    "/teams",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Remove all teams",
    response_model_by_alias=True,
)
async def remove_all_teams(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.delete(
    "/tournaments",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Remove all tournaments",
    response_model_by_alias=True,
)
async def remove_all_tournaments(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.delete(
    "/users/{user_id}/stats",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Remove all stats for a specific user profile on our platform",
    response_model_by_alias=True,
)
async def remove_all_user_stats(
    user_id: str = Path(None, description="The unique identifier (ULID) we use for users of our API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.delete(
    "/users",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Remove all users from our platform",
    response_model_by_alias=True,
)
async def remove_all_users(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.delete(
    "/tournaments/{tournament_id}",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Remove a tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def remove_tournament_details(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.delete(
    "/users/{user_id}",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    summary="Remove user from our platform if it exists",
    response_model_by_alias=True,
)
async def remove_user(
    user_id: str = Path(None, description="The unique identifier (ULID) we use for users of our API"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.put(
    "/tournaments/{tournament_id}",
    responses={
        501: {"description": "Not Implemented"},
    },
    tags=["default"],
    summary="Update details for a tournament for a specific game available on the Relic Link platform",
    response_model_by_alias=True,
)
async def update_tournament_details(
    tournament_id: str = Path(None, description="The unique identifier (ULID) we use for tournaments"),
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    """"""
    ...


@router.post(
    "/users/login",
    responses={
        200: {"description": "Operation succeeded"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def user_login(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.get(
    "/users/logout",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def user_logout(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...


@router.post(
    "/users/register",
    responses={
        200: {"description": "Operation succeeded"},
        401: {"model": UnauthorizedError, "description": "Unauthorized access."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def user_register(
    token_X-Api-Key: TokenModel = Security(
        get_token_X-Api-Key
    ),
) -> None:
    ...
