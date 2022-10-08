# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.forbidden_error import ForbiddenError  # noqa: F401
from openapi_server.models.not_acceptable_error import NotAcceptableError  # noqa: F401
from openapi_server.models.not_found_error import NotFoundError  # noqa: F401
from openapi_server.models.not_implemented_error import NotImplementedError  # noqa: F401
from openapi_server.models.too_many_requests_error import TooManyRequestsError  # noqa: F401
from openapi_server.models.ulid import Ulid  # noqa: F401
from openapi_server.models.unauthorized_error import UnauthorizedError  # noqa: F401


def test_get_details_for_leaderboard(client: TestClient):
    """Test case for get_details_for_leaderboard

    Retrieve details for a specific leaderboard
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/leaderboards/{leaderboard_id}".format(leaderboard_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_leaderboard_collection(client: TestClient):
    """Test case for get_leaderboard_collection

    Retrieve all leaderboards
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/leaderboards",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_leaderboard_collection_for_game(client: TestClient):
    """Test case for get_leaderboard_collection_for_game

    Retrieve all leaderboards for a specific game
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/games/{game_id}/leaderboards".format(game_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_match_collection_for_leaderboard(client: TestClient):
    """Test case for get_match_collection_for_leaderboard

    Retrieve all matches on a specific leaderboard for a certain game
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/leaderboards/{leaderboard_id}/matches".format(leaderboard_id={'key': openapi_server.Ulid()}),
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

