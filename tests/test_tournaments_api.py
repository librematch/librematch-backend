# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.count_param import CountParam  # noqa: F401
from openapi_server.models.forbidden_error import ForbiddenError  # noqa: F401
from openapi_server.models.game_id import GameId  # noqa: F401
from openapi_server.models.match_status import MatchStatus  # noqa: F401
from openapi_server.models.not_acceptable_error import NotAcceptableError  # noqa: F401
from openapi_server.models.not_found_error import NotFoundError  # noqa: F401
from openapi_server.models.not_implemented_error import NotImplementedError  # noqa: F401
from openapi_server.models.since_param import SinceParam  # noqa: F401
from openapi_server.models.too_many_requests_error import TooManyRequestsError  # noqa: F401
from openapi_server.models.ulid import Ulid  # noqa: F401
from openapi_server.models.unauthorized_error import UnauthorizedError  # noqa: F401


def test_get_bracket_collection_for_tournament(client: TestClient):
    """Test case for get_bracket_collection_for_tournament

    Retrieve all brackets for a specific tournament for a specific game
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{tournament_id}/brackets".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_info_collection_for_tournament(client: TestClient):
    """Test case for get_info_collection_for_tournament

    Retrieve all information for a specific tournament for a specific game
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{tournament_id}/info".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_match_collection_for_tournament(client: TestClient):
    """Test case for get_match_collection_for_tournament

    Retrieve all match data for a specific tournament for a specific game
    """
    params = [("status", {'key': openapi_server.MatchStatus()}),     ("game", {'key': openapi_server.GameId()}),     ("count", {'key': openapi_server.CountParam()}),     ("since", {'key': openapi_server.SinceParam()})]
    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{tournament_id}/matches".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
        params=params,
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

