# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.forbidden_error import ForbiddenError  # noqa: F401
from openapi_server.models.not_acceptable_error import NotAcceptableError  # noqa: F401
from openapi_server.models.not_found_error import NotFoundError  # noqa: F401
from openapi_server.models.not_implemented_error import NotImplementedError  # noqa: F401
from openapi_server.models.relic_link_id import RelicLinkId  # noqa: F401
from openapi_server.models.timeframe import Timeframe  # noqa: F401
from openapi_server.models.too_many_requests_error import TooManyRequestsError  # noqa: F401
from openapi_server.models.ulid import Ulid  # noqa: F401
from openapi_server.models.unauthorized_error import UnauthorizedError  # noqa: F401


def test_get_database_dump_collection(client: TestClient):
    """Test case for get_database_dump_collection

    
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/dumps/{timeframe}".format(timeframe={'key': openapi_server.Timeframe()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_stat_collection_for_leaderboard(client: TestClient):
    """Test case for get_stat_collection_for_leaderboard

    Retrieve all stats on a specific leaderboard for a certain game
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/leaderboards/{leaderboard_id}/stats".format(leaderboard_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_stat_collection_for_profile(client: TestClient):
    """Test case for get_stat_collection_for_profile

    Retrieve all stats for a specific profile
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/profiles/{relic_link_id}/stats".format(relic_link_id={'key': openapi_server.RelicLinkId()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_stat_collection_for_team(client: TestClient):
    """Test case for get_stat_collection_for_team

    Retrieve a list of stats for a specific team
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/teams/{team_id}/stats".format(team_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_stat_collection_for_tournament(client: TestClient):
    """Test case for get_stat_collection_for_tournament

    Retrieve all statistics for a specific tournament for a specific game
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{tournament_id}/stats".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_stat_collection_for_user(client: TestClient):
    """Test case for get_stat_collection_for_user

    Retrieve all stats for a specific user profile on our platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/users/{user_id}/stats".format(user_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

